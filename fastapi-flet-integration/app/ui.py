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
        value="20",
        width=200
    )

    def call_api(_):
        num1 = int(input_a.value)
        num2 = int(input_b.value)

        main_message.value = "Calculating..."
        page.update()

        def make_request():
            response = requests.post(
                                    "http://localhost:8550/api/add", 
                                    json={"a": num1, "b": num2},
                                    timeout=10,
                                )
            data = response.json()
            main_message.value = f"Result: {data['result']}"

            page.update()
        
        page.run_thread(make_request)

    def get_health():
        res = requests.get("http://localhost:8550/api/health")
        data = res.json()

        main_message.value = f"Health status: {data['status']}"
        page.update()
        
    main_message = ft.Text("Enter 2 numbers", size=40)
    
    health_button = ft.Button("Get Health", on_click=lambda e: page.run_thread(get_health))
    calc_button = ft.Button("Calculation", on_click=call_api)

    page.add(
        ft.Row([
            input_a,
            input_b,
            calc_button,
        ]),
        main_message, 
        health_button,
    )