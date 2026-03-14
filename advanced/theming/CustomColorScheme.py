import flet as ft
 
# Định nghĩa themes
LIGHT_THEME = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=ft.Colors.PURPLE,
        secondary=ft.Colors.ORANGE,
        surface=ft.Colors.WHITE,
        # background=ft.Colors.GREY_100,
        error=ft.Colors.RED,
    ),
)
 
DARK_THEME = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=ft.Colors.PURPLE_200,
        secondary=ft.Colors.ORANGE_200,
        surface=ft.Colors.GREY_900,
        # background=ft.Colors.BLACK,
    ),
)
 
@ft.observable
class ThemeState:
    is_dark: bool = False
    
    def toggle(self):
        self.is_dark = not self.is_dark
 
state = ThemeState()
 
@ft.component
def ButtonsPreview():
    return ft.Row([
        ft.FilledButton("Filled"),
        ft.Button("Elevated"),
        ft.OutlinedButton("Outlined"),
    ], wrap=True)
 
@ft.component
def ThemeDemo(page: ft.Page):

    ft.use_state(state)
    
    page.theme_mode = ft.ThemeMode.DARK if state.is_dark else ft.ThemeMode.LIGHT

    return ft.Column([
        ft.Switch(
            label="Dark Mode",
            value=state.is_dark,
            on_change=lambda _: state.toggle(),
        ),
        ft.Divider(),
        ft.Text("Buttons Preview", weight=ft.FontWeight.BOLD),
        ButtonsPreview(),
    ], spacing=20)
 
def main(page: ft.Page):
    page.title = "Theme Demo"

    page.window.width = 500
    page.window.height = 800 

    page.theme = LIGHT_THEME
    page.dark_theme = DARK_THEME
    page.padding = 30
    page.render(lambda: ThemeDemo(page))
 
ft.run(main)