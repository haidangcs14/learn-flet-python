import flet as ft
 
@ft.observable
class ThemeState:
    is_dark: bool = False
    primary_color: str = "indigo"
    
    colors_map = {
        "indigo": (ft.Colors.INDIGO, ft.Colors.INDIGO_200),
        "green": (ft.Colors.GREEN, ft.Colors.GREEN_200),
        "purple": (ft.Colors.PURPLE, ft.Colors.PURPLE_200),
        "orange": (ft.Colors.ORANGE, ft.Colors.ORANGE_200),
    }
    
    def toggle_mode(self):
        self.is_dark = not self.is_dark
    
    def set_color(self, color: str):
        self.primary_color = color
    
    def get_primary(self):
        light, dark = self.colors_map.get(self.primary_color, (ft.Colors.INDIGO, ft.Colors.INDIGO_200))
        return dark if self.is_dark else light
 
state = ThemeState()
 
@ft.component
def ColorPicker():
    colors = ["indigo", "green", "purple", "orange"]
    
    return ft.Row([
        ft.Container(
            width=40,
            height=40,
            bgcolor=state.colors_map[c][0],
            border_radius=20,
            border=ft.border.all(3, ft.Colors.WHITE) if state.primary_color == c else None,
            on_click=lambda _, color=c: state.set_color(color),
        )
        for c in colors
    ], spacing=10)
 
@ft.component
def ComponentsPreview():
    return ft.Column([
        ft.Text("Preview", size=20, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Row([
            ft.FilledButton("Filled"),
            ft.Button("Elevated"),
            ft.OutlinedButton("Outlined"),
        ], wrap=True),
        ft.TextField(label="Sample Input"),
        ft.Slider(value=.60),
        ft.ProgressBar(value=0.7),
        ft.Card(
            content=ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text("John Doe"),
                    subtitle=ft.Text("john@example.com"),
                ),
                padding=10,
            ),
        ),
    ], spacing=15)
 
@ft.component
def ThemeSettings():
    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Theme Settings", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Row([
                    ft.Icon(ft.Icons.DARK_MODE if state.is_dark else ft.Icons.LIGHT_MODE),
                    ft.Text("Dark Mode"),
                    ft.Container(expand=True),
                    ft.Switch(
                        value=state.is_dark,
                        on_change=lambda _: state.toggle_mode(),
                    ),
                ]),
                ft.Text("Primary Color", weight=ft.FontWeight.W_500),
                ColorPicker(),
            ]),
            padding=20,
        ),
    )
 
@ft.component
def ThemeSwitcherApp(page: ft.Page):

    ft.use_state(state)

    # Dynamic theme based on state
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=state.get_primary()))
    page.dark_theme = ft.Theme(color_scheme=ft.ColorScheme(primary=state.get_primary()))
    page.theme_mode = ft.ThemeMode.DARK if state.is_dark else ft.ThemeMode.LIGHT

    return ft.Row([
        ft.Container(content=ThemeSettings(), width=300),
        ft.VerticalDivider(),
        ft.Container(content=ComponentsPreview(), expand=True, padding=20),
    ], expand=True)
 
def main(page: ft.Page):
    page.title = "Theme Switcher"
    page.padding = 20
    page.window.width = 750
    page.window.height = 800
    
    page.render(lambda: ThemeSwitcherApp(page))
 
ft.run(main)