import streamlit as st
import base64

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def header_home():
    logo = get_base64("Logo1.png")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src="data:image/png;base64,{logo}" style="height:100px; border-radius:25%" alt="MONAE Logo">
            <h1 style='text-align:center; color:#E0E3FF'>MONAE</h1>
        </div>
                """, unsafe_allow_html=True)

def header_dashboard():
    logo = get_base64("Logo1.png")

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src="data:image/png;base64,{logo}" style="height:85px; border-radius:25%" alt="MONAE Logo">
            <h2 style='text-align:left; color:#5865F2'>MONAE</h1>
        </div>
                """, unsafe_allow_html=True)