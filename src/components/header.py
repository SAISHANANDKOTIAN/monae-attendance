import streamlit as st
import base64

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def header_home():
    logo = get_base64("Logo.png")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src="data:image/png;base64,{logo}" style="height:100px;" alt="MONAE Logo">
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>
                """, unsafe_allow_html=True)