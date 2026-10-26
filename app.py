
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulasi Agilent Cary 100 UV-Vis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Simulasi Agilent Cary 100 UV-Vis")

html_path = Path(__file__).parent / "simulator.html"

if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    components.html(
        html,
        height=900,
        scrolling=True
    )
else:
    st.error("File simulator.html tidak ditemukan.")
