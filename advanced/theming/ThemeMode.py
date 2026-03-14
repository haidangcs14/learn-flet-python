import flet as ft
 
@ft.observable
class ThemeState:
    is_dark: bool = False
    
    def toggle(self):
        self.is_dark = not self.is_dark
 
state = ThemeState()
 
@ft.component
def ThemeToggle():
    return ft.Switch(
        label="Dark Mode",
        value=state.is_dark,
        on_change=lambda _: state.toggle(),
    )
 
@ft.component
def ThemeApp(page: ft.Page):
    ft.use_state(state)

    # Thiết lập theme dựa trên state
    page.theme_mode = ft.ThemeMode.DARK if state.is_dark else ft.ThemeMode.LIGHT
    
    return ft.Column([
        ThemeToggle(),
        ft.Text("Hello Flet!", size=24),
    ])
 
def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 800 
    
    page.render(lambda: ThemeApp(page))
 
ft.run(main)