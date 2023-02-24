import streamlit as st
import streamlit_book as stb

st.set_page_config(page_title="Sages", layout="wide")
stb.set_chapter_config(path="Questions")

### Manual HTML CSS ###

####################### COMMENTS FOR STYLE #######################
# .css-dg4u6x.e16nr0p34 writes "Page sth of sth: from_which_file"

manual_adjustment = """
<style>
#quiz {
  text-align: center;
}

.css-dg4u6x.e16nr0p34 {
  visibility: hidden;
}
</style>
"""
st.markdown(manual_adjustment, unsafe_allow_html=True)

### END OF MANUAL HTML CSS ###
