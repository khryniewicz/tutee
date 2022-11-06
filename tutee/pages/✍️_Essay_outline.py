import streamlit as st
from gpt import essay_outline


st.set_page_config(
    page_title="Tutee - Essay outline",
    page_icon="👨‍✈️",
)

if "essay_topic" not in st.session_state:
    st.session_state.essay_topic = "tech entrepreneurs"

st.title(":writing_hand: Essay outline")
st.markdown("Generate an outline for a research topic.")
st.session_state.essay_topic = st.text_input(
    label="Create an outline for an essay about...",
    value=st.session_state.essay_topic,
)
answer = essay_outline(st.session_state.essay_topic)
st.text_area(label="There you go", value=answer, height=300)


with st.expander("Under the hood"):
    st.markdown(
        """Based on the OpenAI
        [example](https://beta.openai.com/examples/default-essay-outline)."""
    )
