import flet as ft

MIN_VALUE = -30
MAX_VALUE = 30


@ft.component
def Counter(title: str):
    count, set_count = ft.use_state(0)
    step, set_step = ft.use_state(1)
    history, set_history = ft.use_state([])

    # define a func to get the color based on value of count
    def get_color():
        if count > 0:
            return ft.Colors.GREEN
        elif count < 0:
            return ft.Colors.RED
        else:
            return ft.Colors.GREY
    
    def update_value_count(new_val):
        if new_val < MIN_VALUE or new_val > MAX_VALUE:
            return
        set_count(new_val)
        set_history([*history, new_val])

    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text(f"{title}", size=16, color=ft.Colors.GREY_500, weight=ft.FontWeight.W_500),
                
                ft.Container(
                    content=ft.Text(
                        str(count),
                        size=80,
                        weight=ft.FontWeight.BOLD,
                        color=get_color(),
                    ),
                    padding=ft.Padding.symmetric(vertical=20)
                ),

                # Min/Max limit - Giới hạn khoảng cho phép
                ft.Text(f"MIN: {MIN_VALUE} | MAX: {MAX_VALUE}", size=12, color=ft.Colors.GREY_500, weight=ft.FontWeight.W_500),

                # Step input - Cho phép chọn bước nhảy (1, 5, 10)
                ft.Dropdown(
                    label="Step",
                    options=[
                        ft.dropdown.Option(key="1", text="1"),
                        ft.dropdown.Option(key="5", text="5"),
                        ft.dropdown.Option(key="10", text="10"),
                    ],
                    value=str(step),
                    on_select=lambda e: set_step(int(e.control.value)),
                ),

                ft.Divider(),

                ft.Row([
                    ft.IconButton(
                        ft.Icons.REMOVE_CIRCLE,
                        icon_size=50,
                        icon_color=ft.Colors.RED_400,
                        tooltip="Giảm",
                        on_click=lambda _: update_value_count(count - step),
                    ),
                    ft.OutlinedButton(
                        content=ft.Icon(ft.Icons.REFRESH, size=24),
                        style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10),
                        on_click=lambda _: set_count(0),
                    ),
                    ft.IconButton(
                        ft.Icons.ADD_CIRCLE,
                        icon_size=50,
                        icon_color=ft.Colors.GREEN_400,
                        tooltip="Tăng",
                        on_click=lambda _: update_value_count(count + step),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER),

                # --- HISTORY ---
                    ft.Text("HISTORY", size=16, color=ft.Colors.GREY_500, weight=ft.FontWeight.W_500),

                    ft.Container(
                        height=100,
                        content=ft.ListView(
                            controls=[
                                ft.Text(str(v)) for v in reversed(history)
                            ]
                        )
                    )

            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=50,
        ),
        elevation=8,
        width=400,
    )

'''
    Thử thách mở rộng
    - Step input - Cho phép chọn bước nhảy (1, 5, 10)
    - Min/Max limit - Giới hạn khoảng cho phép
    - History - Lưu lịch sử các giá trị
    - Multiple counters - Nhiều counter độc lập
'''

def main(page: ft.Page):
    page.title = "Counter App"
    page.window.width = 1000
    page.window.height = 800 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.CYAN_100

    page.render(
        lambda: ft.Row(
            [
                Counter("Counter 1".upper()),
                Counter("Counter 2".upper()),
            ],alignment=ft.MainAxisAlignment.CENTER,
            spacing=40,
        )
    )
 
ft.run(main)