import flet as ft

@ft.component
def HealthDisplay(health: str):
    health = str(health)

    return ft.Row(
        controls=[
            ft.Icon(ft.Icons.FAVORITE, size=100, color="red"),
            ft.Text(value=health, size=100, color="pink"),
        ]
    )