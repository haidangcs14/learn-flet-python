import flet as ft
import asyncio
import httpx
import json


async def main(page: ft.Page):

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
    streaming_text_control = None

    async def send_query(e):
        user_query = query_field.value.strip()
        if not user_query:
            return

        messages.append({"role": "user", "content": user_query})
        await update_display()

        # disable button during streaming
        send_button.disabled = True
        query_field.disabled = True
        page.update()

        # clear input
        query_field.value = ""
        page.update()

        # start streaming
        asyncio.create_task(stream_response(user_query))

    async def stream_response(user_query: str):

        nonlocal streaming_text_control

        try:
            # store assistant message
            messages.append({"role": "assistant", "content": ""})

            # create text control for streaming
            streaming_text_control = ft.Text("assistant: ", size=14)
            message_column.controls.append(streaming_text_control)
            page.update()

            # use async httpx client for streaming
            async with httpx.AsyncClient(timeout=30.0) as client:
                async with client.stream(
                    "POST",
                    ollama_url,
                    json={
                        "model": model_name,
                        "system": system_prompt,
                        "prompt": user_query,
                        "stream": True,
                        "options": {
                            "num_ctx": num_ctx,
                            "num_predict": num_predict,
                            "stop": ["\n"],
                        },
                    },
                ) as response:
                    response.raise_for_status()
                    # process streaming
                    accumulated_text = ""
                    async for line in response.aiter_lines():
                        if line:
                            try:
                                chunk = json.loads(line)
                                if "response" in chunk:
                                    token = chunk["response"]
                                    accumulated_text += token

                                    # update streaming text control
                                    if streaming_text_control:
                                        streaming_text_control.value = (
                                            f"assistant: {accumulated_text}"
                                        )
                                        page.update()
                                    # check if response is done
                                    if chunk.get("done", False):
                                        break
                            except json.JSONDecodeError:
                                continue
                # update the mess in the list for persistence
                if messages and messages[-1]["role"] == "assistant":
                    messages[-1]["content"] = accumulated_text
        except httpx.RequestError as e:
            print(f"Error connecting to Ollama: {str(e)}")
            if (
                streaming_text_control
                and streaming_text_control in message_column.controls
            ):
                message_column.controls.remove(streaming_text_control)
                await update_display()
                send_button.disabled = False
                query_field.disabled = False
                streaming_text_control = None
                page.update()
        finally:
            # re-enable controls
            send_button.disabled = False
            query_field.disabled = False
            streaming_text_control = None
            page.update()

    async def update_display():
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
