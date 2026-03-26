import flet as ft
import requests
import time
from typing import Any, Dict


def main(page: ft.Page):

    page.title = "Oppllama"
    page.padding = 20

    # ollama configuration
    ollama_url = "http://localhost:11434/api/generate"
    model_name = "llama3.2:latest"
    # num_ctx is tokens in prompt + response
    num_ctx = 512
    # num_predict is max tokens in response, assuming 2 chars per token, about 100 chars
    num_predict = 60
    max_chars = 120
    system_prompt = (
        "You are a NPC called Dang in Viet Nam. "
        + f"Keep response to a single line, under {max_chars} chars."
        + "Be friendly and engaging using casual language for "
        + "people in their 20s."
    )

    messages = []

    def send_query(e):
        user_query = query_field.value.strip()
        if not user_query:
            return

        messages.append({"role": "user", "content": user_query})
        update_display()

        try:
            result: Dict[str, Any] = make_request(user_query)

            response_text = result.get("response", "")
            # print("Cory: ", result.get("response", ""))
            messages.append({"role": "assistant", "content": response_text})
            update_display()

            # clear input after adding assistant message
            query_field.value = ""
            page.update()

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Ollama: {str(e)}")
        except Exception as e:
            print(f"Error generating response: {str(e)}")

    def make_request(user_query: str) -> Dict[str, Any]:

        start_time = time.time()

        response = requests.post(
            ollama_url,
            json={
                "model": model_name,
                "system": system_prompt,
                "prompt": user_query,
                "stream": False,
                "options": {
                    "num_ctx": num_ctx,
                    "num_predict": num_predict,
                    "stop": ["\n"],
                },
            },
        )

        elapsed_time = time.time() - start_time

        print(f"Elapsed time: {elapsed_time}")

        response.raise_for_status()
        return response.json()

    def update_display():
        message_controls = []
        for msg in messages:
            message_controls.append(ft.Text(f"{msg["role"]}: {msg['content']}"))
            message_column.controls = message_controls

        page.update()

    query_field = ft.TextField(label="Yo I'm Dang. What's up?", expand=True)
    send_button = ft.Button("Send", on_click=send_query)
    message_column = ft.Column([], scroll=ft.ScrollMode.AUTO, expand=True)

    page.add(
        ft.Column(
            controls=[
                ft.Image(src="cory.png", width=100, height=100),
                ft.Container(
                    message_column,
                    height=400,
                    border=ft.Border.all(1),
                    padding=10,
                    expand=True,
                ),
                ft.Row(
                    controls=[
                        query_field,
                        send_button,
                    ],
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
