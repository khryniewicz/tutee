import streamlit as st
from gpt import study_notes


st.set_page_config(
    page_title="Tutee - Study notes",
    page_icon="👨‍✈️",
)

if "study_topic" not in st.session_state:
    st.session_state.study_topic = "French Revolution"

st.title(":memo: Study notes")
st.markdown("Provide a topic and get study notes.")
st.session_state.study_topic = st.text_input(
    label="What are 5 key points I should know when studying...",
    value=st.session_state.study_topic,
)
answer = study_notes(st.session_state.study_topic)
st.text_area(label="There you go", value=answer, height=300)


with st.expander("Under the hood"):
    st.markdown(
        """Based on the OpenAI
        [example](https://beta.openai.com/examples/default-study-notes)."""
    )
