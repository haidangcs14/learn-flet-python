import flet as ft


def main(page: ft.Page):
    async def pick_text_file(_):
        files = await ft.FilePicker().pick_files(with_data=True)
        print(files[0].bytes if files else None)

    page.add(ft.Button("Pick file", on_click=pick_text_file))


ft.run(main)