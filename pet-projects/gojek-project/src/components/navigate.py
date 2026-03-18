import flet as ft
from flet import *

# @ft.component

def NavigationBar():
    return ft.Container(
        border_radius = BorderRadius.only(top_left=30,top_right=30),
        bgcolor="#0896BA",
        padding=20,
        height=100,
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            ink=True,
                            on_click=lambda e: print("test"),
                            content=Row([
                                Icon(icon=ft.Icons.MENU,color="white",size=20),
                                Text("Promosi",size=15,color="White")
                                ],spacing=10)
                        ),
                        Container(
                            ink=True,
                            on_click=lambda e: print("test"),
                            content=Row([
                                Icon(icon=ft.Icons.HOME,color="white",size=20),
                                Text("Home",size=15,color="White")
                                ],spacing=10)
                        ),
                        Container(
                            ink=True,
                            on_click=lambda e: print("test"),
                            content=Row([
                                Icon(icon=ft.Icons.MESSAGE,color="white",size=20),
                                Text("Chat",size=15,color="White")
                                ],spacing=10)
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY)
            ],alignment=ft.CrossAxisAlignment.START
        ))