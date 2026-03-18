import flet as ft
from flet import *

def Footer():
    return Container(
        margin=20,
        border_radius=50,
        
        content=Card(
            elevation=30,
            content=Container(
                bgcolor=Colors.WHITE,
                content=Row(
                    [
                        Container(
                            padding=10,
                            content=Column([
                                CircleAvatar(
                                    content=Icon(Icons.MOTORCYCLE, size=30, color=Colors.WHITE),
                                    bgcolor="#00A911"
                                ),
                                Text("GoRide",weight="bold",color="grey", size=20),
                            ],alignment="center", horizontal_alignment="center")
                        ),
                        Container(
                            padding=10,
                            content=Column([
                                CircleAvatar(
                                    content=Icon(Icons.DEPARTURE_BOARD, size=30, color=Colors.WHITE),
                                    bgcolor="#00A911"
                                ),
                                Text("GoShop",weight="bold",color="grey", size=20),
                            ],alignment="center", horizontal_alignment="center")
                        ),
                        Container(
                            padding=10,
                            content=Column([
                                CircleAvatar(
                                    content=Icon(Icons.DEPARTURE_BOARD, size=30, color=Colors.WHITE),
                                    bgcolor="#00A911"
                                ),
                                Text("GoCar",weight="bold",color="grey", size=20),
                            ],alignment="center", horizontal_alignment="center")
                        ),
                        Container(
                            padding=10,
                            content=Column([
                                CircleAvatar(
                                    content=Icon(Icons.RESTAURANT, size=30, color=Colors.WHITE),
                                    bgcolor="#00A911"
                                ),
                                Text("GoFood",weight="bold",color="grey", size=20),
                            ],alignment="center", horizontal_alignment="center")
                        ),
                    ]
                ,alignment="spaceAround")
            )
        )

    )