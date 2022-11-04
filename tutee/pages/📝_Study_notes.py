import streamlit as st
from gpt import study_notes


st.set_page_config(
    page_title="Tutee - Study notes",
    page_icon="👨‍✈️",
)


st.title(":memo: Study notes")
st.markdown("Provide a topic and get study notes.")
topic = st.text_input(
    label="What are 5 key points I should know when studying...",
    value="French Revolution",
)
answer = study_notes(topic)
st.text_area(label="There you go", value=answer, height=300)


with st.expander("Under the hood"):
    st.markdown(
        """Based on the OpenAI
        [example](https://beta.openai.com/examples/default-study-notes)."""
    )
