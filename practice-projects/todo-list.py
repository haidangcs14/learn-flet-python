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
        self.filter: str = "all" # all, active, completed

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

    def set_filter(self, filter: str):
        self.filter = filter

    def get_filtered_items(self):
        if self.filter == "active":
            return [item for item in self.items if not item["completed"]]
        elif self.filter == "completed":
            return [item for item in self.items if item["completed"]]
        return self.items
    
    def get_remaining_count(self):
        return len([item for item in self.items if not item["completed"]])

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
            prefix_icon=ft.Icons.ADD_TASK,
        ),
        ft.FilledButton("Add", icon=ft.Icons.ADD, on_click=add_todo),
    ])

# component to display filter options
@ft.component
def FilterTabs():

    ft.use_state(state)

    return ft.Row([
        ft.Text(f"{state.get_remaining_count()} remaining tasks", 
                color=ft.Colors.GREY_600, size=14),
        ft.Container(expand=True),
        ft.SegmentedButton(
            selected=[state.filter],
            on_change=lambda e: state.set_filter(list(e.control.selected)[0]),
            segments=[
                ft.Segment(value="all", label=ft.Text("All")),
                ft.Segment(value="active", label=ft.Text("Active")),
                ft.Segment(value="completed", label=ft.Text("Completed")),
            ],
        ),
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

    filtered = state.get_filtered_items()

    if not filtered:
        msg = "✨ There are no tasks yet." if state.filter != "all" else "✨ Add some tasks !!!"
        return ft.Container(
            content=ft.Text(msg, color=ft.Colors.GREY_500, size=16),
            padding=40,
            alignment=ft.Alignment.CENTER,
        )

    return ft.Column([
        TodoItem(item) for item in filtered
    ])

# main component
@ft.component
def TodoApp():
    return ft.Container(
        content=ft.Column([
            ft.Text("📝 Todo List", size=28, weight=ft.FontWeight.BOLD),
            TodoForm(),
            ft.Container(height=10),
            FilterTabs(),
            ft.Divider(),
            TodoList(),
        ]),
        padding=20,
        width=500,
    )

def main(page: ft.Page):
    page.title = "Todo List App"
    page.window.width = 500
    page.window.height = 800 
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.bgcolor = ft.Colors.GREY_300

    page.render(TodoApp)
 
ft.run(main)