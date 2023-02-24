import streamlit as st
from streamlit_extras.switch_page_button import switch_page

### Manual HTML CSS ###
manual_adjustment = """
<style>
.stMarkdown {
  visibility: hidden;
}
</style>
"""
st.markdown(manual_adjustment, unsafe_allow_html=True)

### END OF MANUAL HTML CSS ###

st.title('Quiz')

st.write("Hello Quiz")

# method to switch page below
# switch_page("Results")
st.write("Question 1: sth sth sth isit sth?")
st.button("Option 1")
st.button("Option 2")
