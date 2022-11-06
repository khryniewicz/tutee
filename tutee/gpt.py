from os import getenv
from re import sub
import openai
from streamlit import cache

openai.api_key = getenv("OPENAI_API_KEY")


def process_response(response):
    return str.lstrip(sub("\n\n", "\n", response.choices[0].text))


@cache(persist=True)
def essay_outline(topic: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Create an outline for an essay about {topic}:\n",
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return process_response(response)


@cache(persist=True)
def study_notes(topic: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"What are 5 key points I should know when studying {topic}?\n",
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return process_response(response)


@cache(persist=True)
def summarize(text, model, temperature, max_tokens) -> str:
    response = openai.Completion.create(
        model=model,
        prompt=f"Summarize this for a second-grade student:\n\n{text}",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return process_response(response)
