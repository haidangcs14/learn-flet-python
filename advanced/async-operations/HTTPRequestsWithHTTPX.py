import flet as ft
import httpx

@ft.observable
class ApiState:
    is_loading: bool = False
    result: str = ""
    error: str = ""

    def start_fetch(self):
        self.is_loading = True
        self.result = ""
        self.error = ""

    def set_result(self, data: str):
        self.is_loading = False
        self.result = data

    def set_error(self, error: str):
        self.is_loading = False
        self.error = error

state = ApiState()

@ft.component
def ApiDemo():
    ft.use_state(state)

    async def fetch_user(e):
        state.start_fetch()
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://jsonplaceholder.typicode.com/users/1"
                )
                data = response.json()
                state.set_result(f"Name: {data['name']}\nEmail: {data['email']}")
        except Exception as e:
            state.set_error(f"Error: {e}")

    controls = [
        ft.Button("Fetch User", on_click=fetch_user),
        ft.ProgressRing(visible=state.is_loading),
    ]

    if state.result:
        controls.append(ft.Text(state.result, selectable=True))

    if state.error:
        controls.append(ft.Text(state.error, color=ft.Colors.RED))

    return ft.Column(controls, spacing=15)


async def main(page: ft.Page):
    page.title = "API Demo"
    page.window.width = 500
    page.window.height = 800
    page.padding = 30
    page.render(ApiDemo)

if __name__ == "__main__":
    ft.run(main)