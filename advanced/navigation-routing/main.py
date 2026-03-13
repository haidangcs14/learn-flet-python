import flet as ft
 
@ft.observable
class RouterState:
    route: str = "/"
 
state = RouterState()
 
@ft.component
def HomeView():
    ft.use_state(state)
    return ft.View(
        [
            ft.AppBar(title=ft.Text("Home")),
            ft.Text("Welcome to Home!", size=24),
            ft.Button(
                "Go to Settings",
                on_click=lambda _: setattr(state, 'route', '/settings'),
            ),
        ]
    )
 
@ft.component
def SettingsView():
    ft.use_state(state)

    return ft.View(
        [
            ft.AppBar(title=ft.Text("Settings")),
            ft.Text("Settings Page", size=24),
            ft.Button(
                "Back to Home",
                on_click=lambda _: setattr(state, 'route', '/'),
            ),
        ]
    )
 

@ft.component
def Router():
    ft.use_state(state)
    
    if state.route == "/settings":    
        return [SettingsView()]
    else:
        return [HomeView()]
 
def main(page: ft.Page):
    page.title = "Navigation Demo"
    page.window.width = 500
    page.window.height = 800 

    page.render_views(Router)
 
ft.run(main)