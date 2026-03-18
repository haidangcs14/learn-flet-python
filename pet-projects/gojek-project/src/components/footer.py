import flet as ft
from flet import *

@ft.component
def Footer():
    items = [
        {"icon": Icons.MOTORCYCLE, "text": "GoRide"},
        {"icon": Icons.DEPARTURE_BOARD, "text": "GoShop"},
        {"icon": Icons.DEPARTURE_BOARD, "text": "GoCar"},
        {"icon": Icons.RESTAURANT, "text": "GoFood"},
    ]

    return Container(
        margin=20,
        border_radius=50,
        content=Card(
            elevation=30,
            content=Container(
                bgcolor=Colors.WHITE,
                content=Row(
                    controls=[
                        Container(
                            padding=10,
                            content=Column(
                                [
                                    CircleAvatar(
                                        content=Icon(item["icon"], size=30, color=Colors.WHITE),
                                        bgcolor="#00A911"
                                    ),
                                    Text(
                                        item["text"],
                                        weight="bold",
                                        color="grey",
                                        size=20
                                    ),
                                ],
                                alignment="center",
                                horizontal_alignment="center"
                            )
                        )
                        for item in items
                    ],
                    alignment=MainAxisAlignment.SPACE_AROUND
                )
            )
        )
    )