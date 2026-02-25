import flet as ft

@ft.component
def RegistrationForm():
    name, set_name = ft.use_state("")
    email, set_email = ft.use_state("")
    password, set_password = ft.use_state("")
    agreed, set_agreed = ft.use_state(False)

    def handle_submit(_):
        if name and email and password and agreed:
            print(f"Registered: {name}, {email}")

    name_input = ft.TextField(
            label="Họ và tên",
            prefix_icon=ft.Icons.PERSON,
            value=name,
            on_change=lambda e: set_name(e.control.value),
            )
    

    email_input = ft.TextField(
            label="Email",
            prefix_icon=ft.Icons.EMAIL,
            value=email,
            on_change=lambda e: set_email(e.control.value),
            )
    

    password_input = ft.TextField(
            label="Mật khẩu",
            prefix_icon=ft.Icons.LOCK,
            value=password,
            on_change=lambda e: set_password(e.control.value),
            )
    
    
    return ft.Column(
        controls=[
            name_input,
            email_input,
            password_input,
            ft.Checkbox(
                label="Đồng ý điều khoản",
                value=agreed,
                on_change=lambda _: set_agreed(not agreed),
            ),
            ft.Row([
                ft.FilledButton("Đăng ký", icon=ft.Icons.CHECK, on_click=handle_submit),
                ft.OutlinedButton("Hủy"),
            ]),
        ],
        spacing=20,
    )

def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 600 
    page.render(RegistrationForm)

if __name__ == "__main__":
    ft.run(main)
