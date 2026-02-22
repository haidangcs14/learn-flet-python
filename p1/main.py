# import flet as ft
 
# @ft.component
# def Greeting():
#     # State: lời chào hiện tại
#     message, set_message = ft.use_state("Xin chào! 👋")
    
#     def change_greeting(_):
#         set_message("Chào mừng đến với Flet! 🎉")
    
#     return ft.Column([
#         ft.Text(message, size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_100),
#         ft.Button("Nhấn vào đây!", on_click=change_greeting),
#     ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
 
# def main(page: ft.Page):
#     page.title = "Ứng dụng đầu tiên"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.render(Greeting)
 
# ft.run(main)


import flet as ft

@ft.component
def Counter():
    count, set_count = ft.use_state(0)


    def minus_num(_):
        set_count(count - 1)

    def plus_num(_):
        set_count(count + 1)


    return ft.Row(
        [
            ft.IconButton(ft.Icons.REMOVE, on_click=minus_num),
            ft.Text(str(count), size=30),
            ft.IconButton(ft.Icons.ADD, on_click=plus_num)
        ], alignment=ft.MainAxisAlignment.CENTER
    )

ft.run(lambda page: page.render(Counter))