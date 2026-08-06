import streamlit as st
import base64


def header_home():

        with open("assets/logo.png", "rb") as f:
          logo_url = "data:image/png;base64," + base64.b64encode(f.read()).decode()

        st.markdown(f"""
    <div style="display:flex; flex-direction:column; align-items:center; margin-bottom:30px; margin-top:30px">
        <img src="{logo_url}" style="height:100px;">
        <h1 style="text-align:center; font-family:'Outfit',sans-serif;">
    <span style="color:white;">Vision</span>
    <span style="color:#FFD400;">Roll</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)   

