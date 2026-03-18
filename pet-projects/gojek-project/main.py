import flet as ft
from src.views.home_view import HomeView
from src.components.navigate import NavigationBar

def main(page: ft.Page):
    page.title = "My Flet App"

    page.padding = 0
    page.spacing = 0
    page.scroll = "auto"
    page.window.width = 500
    page.window.height = 1030
    
    page.render(HomeView)

ft.run(main, assets_dir="assets")