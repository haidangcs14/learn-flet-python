import httpx
import json
from typing import Any
import asyncio

url: str = "http://localhost:11434/api/chat"
num_words = 10
content = f"why did llms become popular in the mid 2020s"
# content = (
#     f"Genarate {num_words} random words. Only show the {num_words} words, no other text",
# )

payload: dict[str, Any] = {
    "model": "llama3.2:latest",
    "messages": [
        {
            "role": "user",
            "content": content,
        }
    ],
    "stream": True,
}


async def simulate_button_presses():
    press_count: int = 0
    try:
        while True:
            await asyncio.sleep(0.2)
            press_count += 1
            print(f"\n[Simulated button press #{press_count}]", flush=True)
    except asyncio.CancelledError:
        print("\n[Button simulation stopped]", flush=True)


async def stream_ollama_response():
    accumulated_text: str = ""

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", url, json=payload) as response:
            chunk_count: int = 1
            async for line in response.aiter_lines():
                if not line:
                    continue
                # print(f"line (chunk): {chunk_count} is type {type(line)}")
                # print(line)

                data: dict[str, Any] = json.loads(line)

                message = data.get("message")

                content = message.get("content")

                if content:
                    accumulated_text += content

                    print("\033[2J\033[H", end="", flush=True)
                    print(accumulated_text, end="", flush=True)

                chunk_count += 1


async def main():
    stream_task = asyncio.create_task(stream_ollama_response())
    button_task = asyncio.create_task(simulate_button_presses())

    await stream_task

    button_task.cancel()

    try:
        await button_task
    except asyncio.CancelledError:
        pass


if __name__ == "__main__":
    asyncio.run(main())
