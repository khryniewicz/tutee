import streamlit as st
import wikipedia

from gpt import summarize

st.sidebar.title("Parameters")
model = st.sidebar.selectbox("Model", ["text-davinci-002"], help="The ID of the model to use for this request.")
temperature = st.sidebar.slider("Temperature ", 0.0, 0.9, 0.2, step=0.05, help="Higher values means the model will take more risks. Try 0.9 for more creative answer, and 0 for well-defined one.")
max_tokens = st.sidebar.number_input("Max tokens", min_value=50, max_value=200, value=100, help="The maximum number of tokens to generate in the completion.")

st.title(":shrug: Explain Like I'm 5")
st.markdown("Proof of Concept for a copilot for students. Check the Wikipedia article about the given topic and generate a summary for a second-grade student using GPT-3. You can modify the parameters in the sidebar.")
page = st.text_input("Explain...", "quantum computing")
with st.spinner("Just a second..."):
    text = str.rstrip(wikipedia.summary(page))
    st.text_area("There you go", summarize(text, model, temperature, max_tokens), height=250)

with st.expander("Wiki text"):
    st.markdown("To create the summary we check the Wikipedia article related to the topic and get it's summary. The prompt for the GPT is: `Summarize this for a second-grade student: {wiki_summary}`")
    st.text_area("wiki_summary", text, height=250, disabled=True)
