import flet as ft
from flet import *

@ft.component
def SearchCard():

    search, set_search = ft.use_state("")

    return ResponsiveRow([
        Container(
            bgcolor="#FFFFFF",
            border_radius = BorderRadius.only(top_left=30,top_right=30),
            padding=0,
            margin = Margin.symmetric(vertical=-30),
            content=Column(col={"sm":12,"md":12,"lg":12},
                controls=[
                    # FOR INPUT SEARCH LUNCH
                    Container(
                        bgcolor="#FCFCFC",
                        border_radius=30,
                        content=Row([
                            TextField(
                                value=search,
                                border="none",
                                prefix_icon=Icons.SEARCH,
                                label="Search Lunch ? ",
                                on_change=lambda e: (set_search(e.control.value), print(search)),
                            ),
                            ft.Row([
                                IconButton(
                                    icon=Icons.ACCOUNT_CIRCLE,
                                    icon_color=Colors.GREEN,
                                    icon_size=30
                                ),
                                ft.Text("Hello")
                            ]),
                            
                        ])
                    ),
                    # FOR BLUE CARD,
                    Card(
                        elevation=30,
                        content=Container(
                            border_radius=30,
                            bgcolor="#01ADD5",
                            content=Row([
                                Container(
                                    margin=10,
                                    height=70,
                                    padding=10,
                                    width=120,
                                    border_radius=10,
                                    bgcolor=Colors.WHITE,
                                    content=Column([
                                        Text("Gopay", weight=FontWeight.BOLD, size=15),
                                        Text("Rp.7.029", weight=FontWeight.BOLD, size=17),
                                        Text("Tap to Top Up", size=11),
                                        ],alignment=Alignment.CENTER,spacing=0)
                                ),
                                    # FOR CHILD ICON
                                Column([
                                    Icon(ft.Icons.BOLT, color=Colors.WHITE, size=30),
                                    Text("Pay",color=Colors.WHITE, size=15, weight=FontWeight.BOLD)
                                ]),
                                Column([
                                    Icon(ft.Icons.ADD_BOX, color=Colors.WHITE, size=30),
                                    Text("Top Up",color=Colors.WHITE, size=15, weight=FontWeight.BOLD)
                                ]),
                                Column([
                                    Icon(ft.Icons.DRAG_INDICATOR,color=Colors.WHITE, size=30),
                                    Text("More",color=Colors.WHITE, size=15, weight=FontWeight.BOLD)
                                ]),
                            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)
                        )
                    )
                ])
            )
        ])