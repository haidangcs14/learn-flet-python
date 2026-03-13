import flet as ft
import json

@ft.observable
class ThemeState:
    theme_mode: str = "system"
    primary_color: str = "blue"
    font_family: str = "Poppins"

    colors = {
        "blue": ft.Colors.BLUE,
        "green": ft.Colors.GREEN,
        "purple": ft.Colors.PURPLE,
        "orange": ft.Colors.ORANGE,
        "red": ft.Colors.RED,
    }
    
    def toggle_mode(self, mode: str):
        self.theme_mode = mode
    
    def set_color(self, color: str):
        self.primary_color = color
    
    def get_primary(self):
        return self.colors.get(self.primary_color, ft.Colors.BLUE)
    
    def set_font(self, font: str):
        self.font_family = font
 
state = ThemeState()
 
def get_theme_icon():
    icons = {
        "light": ft.Icons.LIGHT_MODE,
        "dark": ft.Icons.DARK_MODE,
        "system": ft.Icons.LAPTOP,
    }
    return icons.get(state.theme_mode, ft.Icons.PALETTE)

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

                # dropdown to choice theme mode
                ft.Row([
                    ft.Icon(get_theme_icon()),
                    ft.Text("Theme Mode"),
                ]),
                ft.Dropdown(
                    width=200,
                    value=state.theme_mode,
                    options=[
                        ft.dropdown.Option(key="light", text="Light", leading_icon=ft.Icons.LIGHT_MODE),
                        ft.dropdown.Option(key="dark", text="Dark", leading_icon=ft.Icons.DARK_MODE),
                        ft.dropdown.Option(key="system", text="System", leading_icon=ft.Icons.LAPTOP),
                    ],
                    on_select=lambda e: state.toggle_mode(e.control.value),
                ),

                # Color picker
                ft.Text("Primary Color", weight=ft.FontWeight.W_500),
                ColorPicker(),

                # dropdown to choice font family
                ft.Row([
                    ft.Icon(ft.Icons.FONT_DOWNLOAD),
                    ft.Text("Font Family"),
                ]),
                ft.Dropdown(
                    value=state.font_family,
                    options=[
                        ft.dropdown.Option("Poppins"),
                        ft.dropdown.Option("Roboto"),
                        ft.dropdown.Option("Montserrat"),
                        ft.dropdown.Option("JetBrainsMono"),
                    ],
                    on_select=lambda e: state.set_font(e.control.value),
                )
            ]),
            padding=20,
        ),
    )
 
@ft.component
def ThemeSwitcherApp(page: ft.Page):
    ft.use_state(state)

    async def save_preferences():
        await page.shared_preferences.set(
            "theme",
            json.dumps({
                "mode": state.theme_mode,
                "color": state.primary_color,
                "font": state.font_family
            })
        )

    def update_theme():
        page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=state.get_primary()),
            font_family=state.font_family
        )
        page.dark_theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=state.get_primary()),
            font_family=state.font_family
        )
        
        theme_modes = {
            "light": ft.ThemeMode.LIGHT,
            "dark": ft.ThemeMode.DARK,
            "system": ft.ThemeMode.SYSTEM
        }

        page.theme_mode = theme_modes[state.theme_mode]

        page.update()

        page.run_task(save_preferences)

    ft.use_effect(update_theme, [state.theme_mode, state.primary_color, state.font_family])

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

async def load_preferences(page: ft.Page):

    data = await page.shared_preferences.get("theme")

    if data:
        theme = json.loads(data)
        state.theme_mode = theme["mode"]
        state.primary_color = theme["color"]
        state.font_family = theme["font"]
    
    print(state.font_family)

async def main(page: ft.Page):
    page.title = "Theme Switcher"
    page.padding = 20
    page.window.width = 850
    page.window.height = 830


    page.fonts = {
        "Poppins": "fonts/Poppins-Regular.ttf",
        "Roboto": "fonts/Roboto-Regular.ttf",
        "Montserrat": "fonts/Montserrat-Regular.ttf",
        "JetBrainsMono": "fonts/JetBrainsMono-Regular.ttf",
    }
    
    await load_preferences(page)

    page.render(lambda: ThemeSwitcherApp(page))
    
ft.run(main)
