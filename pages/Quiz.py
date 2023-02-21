import streamlit as st
from streamlit_extras.switch_page_button import switch_page

### Manual HTML CSS ###
title_alignment = """
<style>
#quiz {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

### END OF MANUAL HTML CSS ###

st.title('Quiz')

st.write("Hello Quiz")

# method to switch page below
# switch_page("Results")
