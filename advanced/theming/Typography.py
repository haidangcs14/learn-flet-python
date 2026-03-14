import flet as ft
 
@ft.component
def TypographyDemo():
    return ft.Column([
        ft.Text("Default font", size=16),
        ft.Text("Bold Text", weight=ft.FontWeight.BOLD, size=20),
        ft.Text("Italic Text", italic=True, size=18),
        ft.Text("Colored Text", color=ft.Colors.BLUE, size=18),
    ], spacing=10)
 
def main(page: ft.Page):
    # Thêm custom font (đặt file .ttf trong thư mục assets)
    page.fonts = {
        "Roboto": "fonts/Roboto-Regular.ttf",
        "RobotoBold": "fonts/Roboto-Bold.ttf",
    }
    
    # Hoặc Google Fonts (tự động tải)
    page.fonts = {
        "Kanit": "Kanit",
        "Open Sans": "Open Sans",
    }
    
    page.theme = ft.Theme(font_family="Kanit")
    page.render(TypographyDemo)
 
ft.run(main)