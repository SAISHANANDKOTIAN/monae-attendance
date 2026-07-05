import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    
    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            "<h2 style='color:black;'>I'm Student</h2>",
            unsafe_allow_html=True
        )
        st.image("https://img.magnific.com/free-vector/cute-boy-with-backpack-book-cartoon-vector-icon-illustration-people-education-icon-isolated_138676-13454.jpg?semt=ais_hybrid&w=740&q=80", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.markdown(
            "<h2 style='color:black;'>I'm Teacher</h2>",
            unsafe_allow_html=True
        )
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJeM_4IwMwIedxfhF4YcqKL9wh2yoio05zZg&s", width=120)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()
