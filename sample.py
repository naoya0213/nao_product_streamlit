import streamlit as st
from PIL import Image
from portrait import portrait

f = st.file_uploader('Upload image file')
if (f):
    with open(f'static\modnet_image\input\\input.jpg', 'wb') as file:
        file.write(f.read())
    file.close()
    st.image(portrait('static\modnet_image\input\\input.jpg'))
# 