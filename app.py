import streamlit as st
import helper
from PIL import Image



st.set_page_config(
    page_title="vegetable plant diseases",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

user_option=st.selectbox(('Select Options'),['','Upload Picture','Take Picture',],)
if user_option=='':
    st.header('Welcome to Application')
    st.text("""Important Note: This application
    This application predicion vegetable plant diseases (Paper | Patato | Tamatos) Available optons
    this application You can Take Picture From Moble or Upload Picture 
    
    email(mm9hassan@gmail.com)""")

elif user_option=='Upload Picture':
    file=st.file_uploader('Upload Picture',['png', 'jpg'] ,label_visibility='hidden')
    if file is not None:
        
        result=helper.Picture_uploader.predicion(file)
        col1,=st.columns(1)
        with col1:
            st.header(result)

        pic =Image.open(file)
        st.image(pic, caption=result)

elif user_option=='Take Picture':
    image=st.camera_input('Take Picture',label_visibility='hidden')
    if image is not None:
        result=helper.Take_picture_uploader.predicion(image)
        col1,=st.columns(1)
        with col1:
            st.header(result)



      






        



      





