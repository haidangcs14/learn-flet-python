import flet as ft
import asyncio

@ft.observable
class ProgressState:
    progress: float = 0
    status: str = "0%"
    is_running: bool = False
    
    def update(self, value: float):
        self.progress = value
        self.status = f"{int(value * 100)}%"
    
    def complete(self):
        self.is_running = False
        self.status = "Done! ✅"
    
    def start(self):
        self.is_running = True
        self.progress = 0

state = ProgressState()

@ft.component
def ProgressDemo():

    ft.use_state(state)

    async def start_process(_):
        state.start()
        for i in range(101):
            state.update(i / 100)
            await asyncio.sleep(0.03)
        state.complete()
    
    return ft.Column([
        ft.ProgressBar(value=state.progress, width=300),
        ft.Text(state.status, size=18),
        ft.Button(
            "Start", 
            on_click=start_process,
            disabled=state.is_running,
        ),
    ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

async def main(page: ft.Page):
    page.title = "Progress Demo"
    page.window.width = 500
    page.window.height = 800

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.render(ProgressDemo)

if __name__ == "__main__":
    ft.run(main)