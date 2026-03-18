import flet as ft
from src.components.header import Header
from src.components.navigate import NavigationBar
from src.components.search_card import SearchCard
from src.components.bagde import Badge
from src.components.footer import Footer

class HomeView(ft.Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            Header(),
            NavigationBar(),
            SearchCard(),
            Badge(),
            Footer()
        ]
