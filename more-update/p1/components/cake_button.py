import flet as ft

@ft.component
def CakeButton(health: str, set_health):
    return ft.Button(
        height=100,
        content=ft.Image(
            "sushi.png",
            height=100,
            width=100,
            fit=ft.BoxFit.FIT_HEIGHT,
        ),
        on_click=lambda: set_health(health+1),
    )