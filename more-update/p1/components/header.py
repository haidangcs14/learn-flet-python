import flet as ft

@ft.component
def Header(text: str):
    return ft.Text(text, size=40)