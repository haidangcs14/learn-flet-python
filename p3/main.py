import flet as ft

@ft.component
def AppLayout():
    col = ft.Column(
        [
            ft.Container
                (
                    content=ft.Text(value="HEADER", text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE), 
                    bgcolor=ft.Colors.BLUE, 
                    width=400, 
                    height=50
                ),
            ft.Row
                (
                    controls=[
                        ft.Container
                            (
                                content=ft.Text(value="SIDEBAR", text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE), 
                                bgcolor=ft.Colors.GREY,
                                expand=True, 
                            ),
                        ft.Container
                            (
                                content=ft.Text(value="MAIN", text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE), 
                                bgcolor=ft.Colors.BLUE, 
                                expand=2,
                            ),
                    ],
                    expand=True,
                ),
            ft.Container
                (
                    content=ft.Text(value="FOOTER", text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE), 
                    bgcolor=ft.Colors.BLUE, 
                    width=400, 
                    height=50
                ),

        ]
    )

    return col

def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 600

    page.title = "Flet app demo"

    page.render(AppLayout)


if __name__ == "__main__":
    ft.run(main)
