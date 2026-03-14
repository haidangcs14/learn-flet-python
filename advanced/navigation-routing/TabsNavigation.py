import flet as ft

@ft.observable
class TabsState:
    selected_index: int = 0

state = TabsState()

@ft.component
def TabContent(text: str, icon):
    return ft.Container(
        alignment=ft.Alignment.CENTER,
        expand=True,
        content=ft.Column(
            [
                ft.Icon(icon, size=48, color=ft.Colors.PRIMARY),
                ft.Text(text, size=20),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )

@ft.component
def TabsApp():

    tabs_data = [
        ("Home", ft.Icons.HOME, "Welcome to Home Tab"),
        ("Settings", ft.Icons.SETTINGS, "Configure your settings"),
        ("About", ft.Icons.INFO, "About this app"),
    ]

    return ft.Tabs(
        selected_index=state.selected_index,
        on_change=lambda e: setattr(state, 'selected_index', e.control.selected_index),
        length=len(tabs_data),
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label=name, icon=icon)
                        for name, icon, _ in tabs_data
                    ]
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        TabContent(content, icon)
                        for _, icon, content in tabs_data
                    ],
                ),
            ],
        ),
    )

def main(page: ft.Page):
    page.title = "Tabs Demo"
    page.window.width = 500
    page.window.height = 800 

    page.render(TabsApp)


ft.run(main)