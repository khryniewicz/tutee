import streamlit as st
from gpt import essay_outline


st.set_page_config(
    page_title="Tutee - Essay outline",
    page_icon="👨‍✈️",
)


st.title(":writing_hand: Essay outline")
st.markdown("Generate an outline for a research topic.")
topic = st.text_input(
    label="Create an outline for an essay about...",
    value="Nikola Tesla and his contributions to technology",
)
answer = essay_outline(topic)
st.text_area(label="There you go", value=answer, height=300)


with st.expander("Under the hood"):
    st.markdown(
        """Based on the OpenAI
        [example](https://beta.openai.com/examples/default-essay-outline)."""
    )
