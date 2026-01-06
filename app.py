import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")

st.set_page_config(page_title="Krishna")
st.title(" Speak to Krishna")
st.subheader("Your Voice-First Spiritual Guide")

if not AGENT_ID:
    st.error("Error: AGENT_ID not found. Please check your .env file.")
else:
    widget_html = f"""
    <div>
        <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
    </div>
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    """
    st.components.v1.html(widget_html, height=250)

st.markdown(""" You can ask Krishna anything! """)
