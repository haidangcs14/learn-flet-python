import flet as ft
from flet import *

@ft.component
def NavigationBar():

    items = [
        {"icon": ft.Icons.MENU, "label": "Promosi"},
        {"icon": ft.Icons.HOME, "label": "Home"},
        {"icon": ft.Icons.MESSAGE, "label": "Chat"},
    ]

    selected, set_selected = ft.use_state("Home")

    def nav_item(item):
        is_active = item["label"] == selected

        return Container(
            ink=True,
            on_click=lambda e, label=item["label"]: set_selected(label),
            content=Row(
                [
                    Icon(
                        icon=item["icon"],
                        color="yellow" if is_active else "white",
                        size=20
                    ),
                    Text(
                        item["label"],
                        size=15,
                        color="yellow" if is_active else "white"
                    )
                ],
                spacing=10
            )
        )

    return Container(
        border_radius=BorderRadius.only(top_left=30, top_right=30),
        bgcolor="#0896BA",
        padding=20,
        height=100,
        content=Column(
            controls=[
                Row(
                    controls=[nav_item(i) for i in items],
                    spacing=0,
                    alignment=MainAxisAlignment.SPACE_EVENLY
                )
            ],
            alignment=CrossAxisAlignment.START
        )
    )