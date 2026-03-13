import flet as ft
 
@ft.observable
class ThemeState:
    is_dark: bool = False
    primary_color: str = "blue"

    colors = {
        "blue": ft.Colors.BLUE,
        "green": ft.Colors.GREEN,
        "purple": ft.Colors.PURPLE,
        "orange": ft.Colors.ORANGE,
        "red": ft.Colors.RED,
    }
    
    def toggle_mode(self):
        self.is_dark = not self.is_dark
    
    def set_color(self, color: str):
        self.primary_color = color
    
    def get_primary(self):
        return self.colors.get(self.primary_color, ft.Colors.BLUE)
 
state = ThemeState()
 
@ft.component
def ColorPicker():
    ft.use_state(state)

    colors = ["blue", "green", "purple", "orange", "red"]
    color_map = {
        "blue": ft.Colors.BLUE,
        "green": ft.Colors.GREEN,
        "purple": ft.Colors.PURPLE,
        "orange": ft.Colors.ORANGE,
        "red": ft.Colors.RED,
    }
    
    return ft.Row([
        ft.Container(
            width=40,
            height=40,
            bgcolor=color_map[c],
            border_radius=20,
            border=ft.Border.all(3, ft.Colors.WHITE) if state.primary_color == c else None,
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK_26) if state.primary_color == c else None,
            on_click=lambda _, color=c: state.set_color(color),
        )
        for c in colors
    ], spacing=10)
 
@ft.component
def ComponentsPreview():
    return ft.Column([
        ft.Text("Preview Components", size=20, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20),
        
        # Buttons
        ft.Text("Buttons", weight=ft.FontWeight.W_500),
        ft.Row([
            ft.Button("Elevated"),
            ft.FilledButton("Filled"),
            ft.OutlinedButton("Outlined"),
        ], wrap=True),
        
        # Form Elements
        ft.Text("Form Elements", weight=ft.FontWeight.W_500),
        ft.TextField(label="Username", prefix_icon=ft.Icons.PERSON),
        ft.TextField(label="Password", password=True, prefix_icon=ft.Icons.LOCK),
        
        ft.Row([
            ft.Checkbox(label="Remember me", value=True),
            ft.Switch(label="Notifications"),
        ]),
        
        # Slider
        ft.Text("Slider", weight=ft.FontWeight.W_500),
        ft.Slider(value=60, min=0, max=100),
        
        # Progress
        ft.Text("Progress", weight=ft.FontWeight.W_500),
        ft.ProgressBar(value=0.7),
        
        # Card
        ft.Text("Card", weight=ft.FontWeight.W_500),
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text("John Doe"),
                        subtitle=ft.Text("john@example.com"),
                    ),
                    ft.Row([
                        ft.TextButton("EDIT"),
                        ft.TextButton("DELETE"),
                    ], alignment=ft.MainAxisAlignment.END),
                ]),
                padding=10,
            ),
        ),
    ], spacing=15, scroll=ft.ScrollMode.AUTO)
 
@ft.component
def ThemeSettings():
    ft.use_state(state)
    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Theme Settings", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                
                # Mode toggle
                ft.Row([
                    ft.Icon(ft.Icons.LIGHT_MODE if not state.is_dark else ft.Icons.DARK_MODE),
                    ft.Text("Dark Mode"),
                    ft.Container(expand=True),
                    ft.Switch(
                        value=state.is_dark,
                        on_change=lambda _: state.toggle_mode(),
                    ),
                ]),
                
                # Color picker
                ft.Text("Primary Color", weight=ft.FontWeight.W_500),
                ColorPicker(),
            ]),
            padding=20,
        ),
    )
 
@ft.component
def ThemeSwitcherApp(page: ft.Page):
    ft.use_state(state)

    def update_theme():
        page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=state.get_primary())
        )
        page.dark_theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=state.get_primary())
        )
        page.theme_mode = ft.ThemeMode.DARK if state.is_dark else ft.ThemeMode.LIGHT
        page.update()

    ft.use_effect(update_theme, [state.is_dark, state.primary_color])

    return ft.Row([
        ft.Container(
            content=ThemeSettings(),
            width=300,
        ),
        ft.VerticalDivider(),
        ft.Container(
            content=ComponentsPreview(),
            expand=True,
            padding=20,
        ),
    ], expand=True)
'''
Thử thách mở rộng
- Save preference - Lưu theme vào client storage
- System theme - Theo theme của hệ điều hành
- Custom fonts - Đổi font family
- More colors - Color picker đầy đủ hơn
'''    

def main(page: ft.Page):
    page.title = "Theme Switcher"
    page.padding = 20
    page.window.width = 850
    page.window.height = 830
    
    page.render(lambda: ThemeSwitcherApp(page))
    
 
ft.run(main)