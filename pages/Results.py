import streamlit as st
from PIL import Image


### Manual HTML CSS ###
title_alignment = """
<style>

.css-1v0mbdj {
    width: 50%;
    justify-content: center;
}

#results, #mengzi, #xunzi {
  text-align: center;
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)
### END OF MANUAL HTML CSS ###

### FUNCTIONS ###


def setImage(pathToImg, caption=None):
    image = Image.open(pathToImg)
    st.image(image, caption)

### START OF WEBPAGE ###


st.title("Results")

col1, col2 = st.columns(2)  # 2 columns layout

with col1:
    st.title("Mengzi")
    setImage("img/sampleperson.png")
    st.markdown("Some description")


with col2:
    st.title("Xunzi")
    setImage("img/sampleperson.png")
    st.markdown("Some description")
