import flet as ft
from dataclasses import dataclass

@ft.observable
class ItemState:
    items: list = [
        {"id": 1, "name": "Item 1", "description": "Description 1"},
        {"id": 2, "name": "Item 2", "description": "Description 2"},
        {"id": 3, "name": "Item 3", "description": "Description 3"},
    ]
    current_route: str = "/"
    selected_item_id: int = None

    def go_to_detail(self, item_id: int):
        self.selected_item_id = item_id
        self.current_route = "/detail"
    
    def go_back(self):
        self.selected_item_id = None
        self.current_route = "/"
    
    def get_selected_item(self):
        return next((item for item in self.items if item["id"] == self.selected_item_id), None)
 
state = ItemState()
 
@ft.component
def ItemsList():
    ft.use_state(state)
    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Items")),
            ft.Column([
                ft.ListTile(
                    title=ft.Text(item["name"]),
                    subtitle=ft.Text(item["description"]),
                    on_click=lambda _, id=item["id"]: state.go_to_detail(id),
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                )
                for item in state.items
            ]),
        ],
    )
 
@ft.component
def ItemDetail():
    ft.use_state(state)

    item = state.get_selected_item()
    
    if not item:
        return ft.View(
            route="/detail", 
            controls=[ft.AppBar(
                title=ft.Text("Item not found"),
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: state.go_back()),
            )]
            
        )
    
    return ft.View(
        route="/detail",
        controls=[
            ft.AppBar(
                title=ft.Text("Item Detail"),
                leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: state.go_back()),
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text(f"ID: {item['id']}", size=16),
                    ft.Text(item["name"], size=28, weight=ft.FontWeight.BOLD),
                    ft.Text(item["description"], size=18),
                ], spacing=10),
                padding=30,
            ),
        ],
    )

@ft.component
def App():
    ft.use_state(state)

    if state.current_route == "/detail":
        return [ItemDetail()]
    return [ItemsList()]

def main(page: ft.Page):
    page.title = "Navigation Demo"
    page.window.width = 500
    page.window.height = 800 

    page.render_views(App)
 
# ft.run(main)