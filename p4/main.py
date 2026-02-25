import flet as ft


def main(page: ft.Page):
    img = ft.Image(
        src="https://picsum.photos/200",
        width=200,
        height=200,
        border_radius=ft.BorderRadius.all(10),
    )

    page.add(img)

    page.add(ft.Checkbox( label="Tôi đồng ý điều khoản",value=False))

    page.add(ft.Switch(label="Show/Hide Image"))

    page.add(    
        ft.Slider(
            min=0,
            max=100,
            value=50,
            divisions=10,
            label="{value}%",
            on_change=lambda e: print(e.control.value),
        )
    )

    page.add(
        ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="small", label="Nhỏ"),
                ft.Radio(value="medium", label="Vừa"),
                ft.Radio(value="large", label="Lớn"),
            ]),
            on_change=lambda e: print(e.control.value),
        )
    )

    page.add(
        ft.Dropdown(
            options=[
                ft.dropdown.Option(key="option1", text="Option 1"),
                ft.dropdown.Option(key="option2", text="Option 2"),
                ft.dropdown.Option(key="option3", text="Option 3"),
            ],
            on_select=lambda e: print(e.control.value),
        )
    )

    page.add(
        ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.RED, size=40)
    )

    page.add(
        ft.ProgressBar(value=0.3, width=500, height=10)
    )

    page.add(
        ft.ProgressRing()
    )

ft.run(main)