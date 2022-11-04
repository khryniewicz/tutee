import streamlit as st
import wikipedia
from gpt import summarize


st.set_page_config(
    page_title="Tutee - Explain Like I'm 5",
    page_icon="👨‍✈️",
)

with st.sidebar:
    st.title("Parameters")
    model = st.selectbox(
        label="Model",
        options=["text-davinci-002"],
        help="The ID of the model to use for the OpenAI request.",
    )
    temperature = st.slider(
        label="Temperature ",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        format="%g",
        help="Higher values means the model will take more risks.",
    )
    max_tokens = st.number_input(
        label="Max tokens",
        min_value=50,
        max_value=200,
        value=100,
        help="The maximum number of tokens to generate in the completion.",
    )


st.title(":shrug: Explain Like I'm 5")
st.markdown("Proof of Concept for a copilot for students.")
topic = st.text_input("Explain...", "natural language processing")
page = wikipedia.page(topic)
answer = summarize(page.summary, model, temperature, max_tokens)
st.text_area(label="There you go", value=answer, height=250)


with st.expander("Under the hood"):
    st.markdown(
        """To create the summary we check the Wikipedia article related to the
        topic and get it's summary. The prompt for the GPT is: `Summarize this
        for a second-grade student: {wiki_summary}`. Based on the OpenAI
        [example](https://beta.openai.com/examples/default-summarize)."""
    )
    st.text_area(
        label=f"wiki_summary from {page.title}",
        value=page.summary,
        height=250,
        disabled=True,
    )
