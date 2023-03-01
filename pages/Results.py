import streamlit as st
from PIL import Image


#############################################################
####################### MANUAL CSS ##########################
#############################################################


# .css-1v0mbdj image
title_alignment = """
<style>

.css-1v0mbdj {
    justify-content: center;
}

body {
  text-align: center;
}

</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#############################################################
####################### FUNCTIONS ###########################
#############################################################


def setImage(ratioOfPhil, caption=None):
    image1 = Image.open("img/xunziPortrait.jpg")
    image2 = Image.open("img/mengziPortrait.jpg")
    width, height = image1.size
    # crop dimensions
    cropLen = int(width*ratioOfPhil)

    image3 = image1.crop((0, 0, cropLen, height))
    image4 = image2.crop((cropLen, 0, width, height))

    overalImg = Image.new('RGB', (image3.width + image4.width, image3.height))
    overalImg.paste(image3, (0, 0))
    overalImg.paste(image4, (image3.width, 0))
    st.image(overalImg, caption)
    # st.image(image4, caption)

#############################################################
#################### START OF WEBPAGE #######################
#############################################################


st.title("As of right now, the world stands...")
setImage(0.4)
# insert profiling descriptor here
st.markdown("Some description")
