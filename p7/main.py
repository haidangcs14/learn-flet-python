import flet as ft
 
@ft.component
def Counter():
    # Khai báo state với giá trị khởi tạo
    count, set_count = ft.use_state(0)
    
    return ft.Row([
        ft.IconButton(ft.Icons.REMOVE, on_click=lambda _: set_count(count - 1)),
        ft.Text(str(count), size=24),
        ft.IconButton(ft.Icons.ADD, on_click=lambda _: set_count(count + 1)),
    ], alignment=ft.MainAxisAlignment.CENTER)
 
def main(page: ft.Page):
    page.render(Counter)
 
ft.run(main)