from pathlib import Path
import streamlit as st


st.set_page_config(
    page_title="Tutee - PoC student copilot",
    page_icon="👨‍✈️",
)

st.markdown(Path("README.md").read_text())
