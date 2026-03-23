import flet as ft
import requests

def build_ui(page: ft.Page):

    # create input fields for 2 nums
    input_a = ft.TextField(
        label="1st Num",
        value="2",
        width=200
    )
    
    input_b = ft.TextField(
        label="2nd Num",
        value="2",
        width=200
    )

    def get_health():
        res = requests.get("http://localhost:8550/api/health")
        data = res.json()

        main_message.value = f"Health status: {data['status']}"
        page.update()
        
    main_message = ft.Text("Enter 2 numbers", size=40)
    
    health_button = ft.Button("Get Health", on_click=lambda e: page.run_thread(get_health))

    page.add(
        main_message, 
        ft.Row([
            input_a,
            input_b,
        ]),
        health_button,
    )