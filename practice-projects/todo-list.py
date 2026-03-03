'''
Tạo ứng dụng Todo với các tính năng:
- Thêm task mới
- Đánh dấu hoàn thành/chưa hoàn thành
- Xóa task
- Đếm số task còn lại
- Lọc theo trạng thái
'''
import flet as ft


@ft.observable
class TodoState:
    def __init__(self):
        self.items: list = []
 
    def add_item(self, text: str):
        if text.strip():
            self.items = [
                *self.items,
                {
                    "id": len(self.items),
                    "text": text.strip(),
                    "completed": False
                }
            ]

    def toggle(self, id: int):
        # for item in self.items:
        #     if item["id"] == id:
        #         item["completed"] = not item["completed"]
        #         break
        self.items = [
            {
                **item,
                "completed": not item["completed"]
            } if item["id"] == id else item
            for item in self.items
        ]

    def delete(self, id: int):
        self.items = [item for item in self.items if item["id"] != id]

state = TodoState()

# form to add new todo item
@ft.component
def TodoForm():
    val, set_val = ft.use_state("")

    def add_todo():
        state.add_item(val)
        set_val("")
    
    return ft.Row([
        ft.TextField(
            value=val,
            hint_text="Enter new job...",
            expand=True,
            on_change=lambda e: set_val(e.control.value),
            on_submit=add_todo,
        ),
        ft.Button("Add", icon=ft.Icons.ADD, on_click=add_todo),
    ])

# component to display todo item
@ft.component
def TodoItem(item):

    return ft.ListTile(
        leading=ft.Checkbox(
            value=item["completed"],
            on_change=lambda _: state.toggle(item["id"]),
        ),
        title=ft.Text(
            item["text"],
            style=ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH if item["completed"] else None,
                color=ft.Colors.GREY_500 if item["completed"] else None,
            ),
        ),
        trailing=ft.IconButton(
            ft.Icons.DELETE,
            icon_color=ft.Colors.RED_300,
            on_click=lambda _: state.delete(item["id"]),
        ),
    )

# component to display list of todo items
@ft.component
def TodoList():

    '''
            Vì sao phải làm vậy?
    @ft.observable chỉ đánh dấu object có thể reactive.
    Nhưng component muốn re-render thì phải: subscribe vào state bằng ft.use_state(state)
    
    Nếu không:
        State thay đổi ✔
        UI không biết ✔
    → List không hiển thị ✔
    '''

    ft.use_state(state) # 👈 thêm dòng này để subscribe

    if not state.items:
        return ft.Container(
            content=ft.Text(
                "✨ There are no tasks yet. Add some tasks!",
                color=ft.Colors.GREY_500
            ),
            padding=40,
            alignment=ft.Alignment.CENTER,
        )

    return ft.Column([
        TodoItem(item) for item in state.items
    ])

def main(page: ft.Page):
    page.title = "Todo List App"
    page.window.width = 500
    page.window.height = 800 
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.bgcolor = ft.Colors.GREY_300

    page.render(
        lambda: ft.Column([
            ft.Text("📝 Todo List", size=28, weight=ft.FontWeight.BOLD),
            TodoForm(),
            TodoList(),

        ])
    )
 
ft.run(main)