import flet as ft
 
@ft.observable
class NavState:
    selected_index: int = 0
    
    def set_index(self, index: int):
        self.selected_index = index
 
state = NavState()
 
@ft.component
def ContentArea():

    contents = ["🏠 Home Content", "🔍 Search Content", "👤 Profile Content"]
    return ft.Container(
        content=ft.Text(contents[state.selected_index], size=24),
        expand=True,
        alignment=ft.Alignment.CENTER,
    )
 
@ft.component
def BottomNavApp():
    ft.use_state(state)

    return ft.Column([
        ContentArea(),
        ft.NavigationBar(
            selected_index=state.selected_index,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
            ],
            on_change=lambda e: state.set_index(e.control.selected_index),
        ),
    ], expand=True)
 
def main(page: ft.Page):
    page.title = "Bottom Navigation"
    page.window.width = 500
    page.window.height = 800 
    
    page.render(BottomNavApp)
 
ft.run(main)