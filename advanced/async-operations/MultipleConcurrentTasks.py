import flet as ft
import asyncio
 
@ft.observable
class MultiTaskState:
    results: list = []
    is_loading: bool = False
    
    def clear(self):
        self.results = []
        self.is_loading = True
    
    def add_result(self, result: str):
        self.results = self.results + [result]
    
    def complete(self):
        self.is_loading = False
 
state = MultiTaskState()
 
@ft.component
def ResultsList():
    if not state.results:
        return ft.Text("No results yet")
    return ft.Column([
        ft.Text(r, color=ft.Colors.GREEN) for r in state.results 
    ])
 
@ft.component
def MultiTaskDemo():
    ft.use_state(state)
    
    async def fetch_one(name: str, delay: float):
        await asyncio.sleep(delay)
        state.add_result(f"✅ {name} loaded")
    
    async def fetch_all(_):
        state.clear()
        await asyncio.gather(
            fetch_one("Users", 1.0),
            fetch_one("Products", 1.5),
            fetch_one("Orders", 0.8),
        )
        state.add_result("🎉 All done!")
        state.complete()
    
    return ft.Column([
        ft.Button("Fetch All", on_click=fetch_all, disabled=state.is_loading),
        ft.ProgressRing(visible=state.is_loading),
        ResultsList(),
    ], spacing=15)
 
async def main(page: ft.Page):
    page.title = "Multi Task Demo"
    page.padding = 30
    page.window.width = 500
    page.window.height = 800

    page.render(MultiTaskDemo)
 
ft.run(main)