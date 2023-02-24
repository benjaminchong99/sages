import streamlit as st
import streamlit_book as stb

st.set_page_config(page_title="Sages", layout="wide")
stb.set_chapter_config(path="Questions")

### Manual HTML CSS ###

# .css-dg4u6x.e16nr0p34 writes "Page sth of sth: from_which_file"
manual_adjustment = """
<style>
#quiz {
  text-align: center
}

.st-ck, .st-cp {
    background: rgba(172,177,195,0.25) 100%;
}

.css-dg4u6x.e16nr0p34 {
  visibility: hidden;
}
</style>
"""
st.markdown(manual_adjustment, unsafe_allow_html=True)

### END OF MANUAL HTML CSS ###
