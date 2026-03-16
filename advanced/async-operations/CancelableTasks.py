import flet as ft
import asyncio
 
@ft.observable
class TaskState:
    status: str = "Cancelable Tasks"
    is_running: bool = False
    task = None
    
    def set_status(self, status: str):
        self.status = status
    
    def start(self):
        self.is_running = True
    
    def stop(self):
        self.is_running = False
 
state = TaskState()
 
@ft.component
def CancelableTaskDemo():

    ft.use_state(state)

    async def long_task():
        state.start()
        try:
            for i in range(10):
                state.set_status(f"Processing... {i+1}/10")
                await asyncio.sleep(1)
            state.set_status("Completed! ✅")
        except asyncio.CancelledError:
            state.set_status("Cancelled ❌")
        finally:
            state.stop()
    
    async def start_task(_):
        state.task = asyncio.create_task(long_task())
    
    async def cancel_task(_):
        if state.task:
            state.task.cancel()
    
    return ft.Column([
        ft.Row([
            ft.Button("Start", on_click=start_task, disabled=state.is_running),
            ft.Button("Cancel", on_click=cancel_task, disabled=not state.is_running),
        ]),
        ft.ProgressRing(visible=state.is_running),
        ft.Text(state.status, size=18),
    ], spacing=15)
 
async def main(page: ft.Page):
    page.title = "Cancelable Task"
    page.padding = 30

    page.window.width = 500
    page.window.height = 800

    page.render(CancelableTaskDemo)
 
ft.run(main)