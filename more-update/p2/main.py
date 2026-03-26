import flet as ft
import random

def colorful_blocks():
    return [
        ft.Container(
            alignment=ft.Alignment.CENTER,
            content=ft.Text(str(idx), size=40), 
            expand=True, 
            bgcolor=random.choice(list[ft.Colors](ft.Colors))
        ) 
        for idx in range(1, 201)
    ]

def images() -> list[ft.Image]:
    return [ft.Image(src=f"https://picsum.photos/seed/{idx}/200/300") for idx in range(1, 201)]


@ft.component
def App():
    return ft.GridView(
        controls=images(),
        expand=1,
        runs_count=5,
        child_aspect_ratio=1.5,
        spacing=5.0,
        run_spacing=5,
    )


ft.run(lambda page: page.render(App))