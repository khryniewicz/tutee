from os import getenv
import openai

openai.api_key = getenv("OPENAI_API_KEY")


def summarize(text, model, temperature, max_tokens) -> str:
    response = openai.Completion.create(
        model=model,
        prompt=f"Summarize this for a second-grade student:\n\n{text}",
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return str.lstrip(response.choices[0].text)
