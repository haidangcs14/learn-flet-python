import flet as ft
 
@ft.observable
class RouterState:
    current_route: str = "/"

    def go(self, route: str):
        self.current_route = route
 
state = RouterState()
 
@ft.component
def HomeView():
    ft.use_state(state)

    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Home"), bgcolor=ft.Colors.BLUE),
            ft.Container(
                content=ft.Column([
                    ft.Text("🏠 Home Page", size=28, weight=ft.FontWeight.BOLD),
                    ft.Button("Go to Profile", on_click=lambda _: state.go("/profile")),
                    ft.Button("Go to Settings", on_click=lambda _: state.go("/settings")),
                ], spacing=20),
                padding=30,
            ),
        ]
    )

@ft.component
def ProfileView():
    ft.use_state(state)

    return ft.View(
        route="/profile",
        controls=[
            ft.AppBar(
                title=ft.Text("Profile"), 
                bgcolor=ft.Colors.GREEN,
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: state.go("/")),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("👤 Profile Page", size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("User: John Doe"),
                ], spacing=20),
                padding=30,
            ),
        ],
    )

@ft.component
def SettingsView():
    ft.use_state(state)

    return ft.View(
        route="/settings",
        controls=[
            ft.AppBar(
                title=ft.Text("Settings"), 
                bgcolor=ft.Colors.ORANGE,
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: state.go("/")),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("⚙️ Settings Page", size=28, weight=ft.FontWeight.BOLD),
                    ft.Switch(label="Dark Mode"),
                    ft.Switch(label="Notifications"),
                ], spacing=20),
                padding=30,
            ),
        ],
    )
 

@ft.component
def AppRouter():
    ft.use_state(state)

    routes = {
        "/": HomeView,
        "/profile": ProfileView,
        "/settings": SettingsView,
    }
    ViewComponent = routes.get(state.current_route, HomeView)

    return ViewComponent()
 
def main(page: ft.Page):
    page.title = "Navigation Demo"
    page.window.width = 500
    page.window.height = 800 

    page.render_views(AppRouter)
 
ft.run(main)