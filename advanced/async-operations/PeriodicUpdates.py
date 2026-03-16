import flet as ft
import asyncio
from datetime import datetime
 
@ft.observable
class ClockState:
    time: str = ""
    is_running: bool = True
    
    def update_time(self):
        self.time = datetime.now().strftime("%H:%M:%S")
 
state = ClockState()
 
@ft.component
def Clock():
    ft.use_state(state)

    # Background task for clock updates
    async def update_clock():
        while state.is_running:
            state.update_time()
            await asyncio.sleep(1)

    def start_clock():
        asyncio.create_task(update_clock())
    
    ft.use_effect(start_clock, [])

    return ft.Column([
        ft.Text("Current Time:", size=20),
        ft.Text(state.time, size=48, weight=ft.FontWeight.BOLD),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
 
async def main(page: ft.Page):
    page.title = "Clock"
    page.window.width = 500
    page.window.height = 800
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.render(Clock)
 
ft.run(main)