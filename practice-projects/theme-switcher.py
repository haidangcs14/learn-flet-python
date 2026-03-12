import flet as ft
 
def main(page: ft.Page):
    page.title = "Theme Switcher"
    page.padding = 30
    page.window.width = 400
    page.window.height = 800 
    
    # Theme colors
    colors = [ft.Colors.BLUE, ft.Colors.GREEN, ft.Colors.PURPLE, ft.Colors.ORANGE]
    
    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if e.control.value else ft.ThemeMode.LIGHT
        page.update()
    
    def change_color(color):
        def handler(_):
            page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=color))
            page.dark_theme = ft.Theme(color_scheme=ft.ColorScheme(primary=color))
            page.update()
        return handler
    
    page.add(
        ft.Text("🎨 Theme Switcher", size=28, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        # Dark mode toggle
        ft.Switch(label="Dark Mode", on_change=toggle_theme),
        
        # Color picker
        ft.Text("Primary Color:", weight=ft.FontWeight.W_500),
        ft.Row([
            ft.Container(
                width=50, height=50,
                bgcolor=c,
                border_radius=25,
                on_click=change_color(c),
            )
            for c in colors
        ], spacing=10),
        
        ft.Divider(),
        
        # Preview
        ft.Text("Preview:", weight=ft.FontWeight.W_500),
        ft.ElevatedButton("Elevated Button"),
        ft.FilledButton("Filled Button"),
        ft.TextField(label="Sample Input"),
        ft.Slider(value=.50),
        ft.ProgressBar(value=0.6),
    )
 
ft.run(main)