import flet as ft
 
@ft.component
def Greeting():
    return ft.Container(
        content=ft.Column([
            ft.Text("Xin chào!", size=24),
            ft.Text("Chào mừng đến với Flet", size=16),
        ]),
        padding=20,
    )
 
def main(page: ft.Page):
    page.render(Greeting)
 
ft.run(main)