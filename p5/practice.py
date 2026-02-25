import flet as ft
 
@ft.component
def LoginForm():
    username, set_username = ft.use_state("")
    password, set_password = ft.use_state("")
    message, set_message = ft.use_state("")
    msg_color, set_color = ft.use_state(ft.Colors.BLACK)
    
    def login_clicked(_):
        if not username:
            set_message("Vui lòng nhập username")
            set_color(ft.Colors.RED)
        elif not password:
            set_message("Vui lòng nhập password")
            set_color(ft.Colors.RED)
        else:
            set_message(f"Xin chào, {username}!")
            set_color(ft.Colors.GREEN)
    
    def clear_clicked(_):
        set_username("")
        set_password("")
        set_message("")
    
    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Đăng nhập", size=24, weight=ft.FontWeight.BOLD),
                ft.TextField(
                    label="Username",
                    width=300,
                    value=username,
                    on_change=lambda e: set_username(e.control.value),
                ),
                ft.TextField(
                    label="Password",
                    password=True,
                    width=300,
                    value=password,
                    on_change=lambda e: set_password(e.control.value),
                ),
                ft.Text(message, color=msg_color) if message else ft.Container(),
                ft.Row([
                    ft.FilledButton("Đăng nhập", on_click=login_clicked),
                    ft.OutlinedButton("Xóa", on_click=clear_clicked),
                ]),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
            padding=30,
        ),
        width=350,
    )
 
def main(page: ft.Page):
    page.title = "Login Form"
    page.window.width = 500
    page.window.height = 600 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.render(LoginForm)
 
ft.run(main)