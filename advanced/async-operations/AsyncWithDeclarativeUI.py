import flet as ft
import asyncio

@ft.observable
class LoadingState:
    is_loading: bool = False
    status: str = "Ready"
    
    def start_loading(self):
        self.is_loading = True
        self.status = "Loading..."
    
    def finish_loading(self, message: str):
        self.is_loading = False
        self.status = message

state = LoadingState()

@ft.component
def AsyncDemo():
    ft.use_state(state)

    async def fetch_data(_):
        state.start_loading()
        await asyncio.sleep(2)  # Simulate API call
        state.finish_loading("Data loaded! ✅")
    
    return ft.Column([
        ft.Button("Fetch Data", on_click=fetch_data),
        ft.ProgressRing(visible=state.is_loading),
        ft.Text(state.status),
    ], spacing=15)

async def main(page: ft.Page):
    page.title = "Async Demo"

    page.window.width = 500
    page.window.height = 800

    page.padding = 30
    page.render(AsyncDemo)

if __name__ == "__main__":
    ft.run(main)