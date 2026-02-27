import flet as ft
 
@ft.observable
class TodoState:
    items: list = []
    
    def add(self, text: str):
        self.items.append({"id": len(self.items), "text": text, "done": False})
    
    def toggle(self, id: int):
        for item in self.items:
            if item["id"] == id:
                item["done"] = not item["done"]
                break
 
state = TodoState()
 
@ft.component
def TodoItem(item):
    return ft.ListTile(
        leading=ft.Checkbox(
            value=item["done"],
            on_change=lambda _: state.toggle(item["id"]),
        ),
        title=ft.Text(
            item["text"],
            style=ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH if item["done"] else None
            ),
        ),
    )
 
@ft.component
def TodoList():
    input_ref, set_input = ft.use_state("")
    
    def add_todo(_):
        if input_ref:
            state.add(input_ref)
            set_input("")
    
    return ft.Column([
        ft.Row([
            ft.TextField(
                value=input_ref,
                hint_text="Thêm việc cần làm...",
                expand=True,
                on_change=lambda e: set_input(e.control.value),
                on_submit=add_todo,
            ),
            ft.IconButton(ft.Icons.ADD, on_click=add_todo),
        ]),
        ft.Column([TodoItem(item) for item in state.items]),
    ])
 
def main(page: ft.Page):
    page.title = "Todo App"
    page.render(TodoList)
 
ft.run(main)