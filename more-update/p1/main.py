import flet as ft
from components import Header, HealthDisplay, CakeButton


@ft.component
def App():
    health, set_health = ft.use_state(5)

    return ft.Column(
        controls=[
            Header(text="Header here"),
            ft.Row(
                controls=[
                    HealthDisplay(health),
                    CakeButton(health, set_health),
                ],
                spacing=100,
            ),
        ]
    )


if __name__ == "__main__":
    ft.run(lambda page: page.render(App), assets_dir="assets")
