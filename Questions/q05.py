import streamlit as st

st.title("q5 title")

st.write("Is X without X still therefore X?")
cc1 = st.button("Still X")
cc2 = st.button("It's Y")

xunMeng = -1  # 0: xunzi, 1: mengzi

hide_next_button = """
<style>

.css-1dwbmt0.e1tzin5v0, css-5uatcg.edgvbvh10:hover {
    pointer-events:none;
}
</style>
"""
st.markdown(hide_next_button, unsafe_allow_html=True)

# buttons
if cc1:
    testChoice = 0
    xunMeng = 0
    manual_adjustment = """
    <style>
    .css-1dwbmt0.e1tzin5v0, css-5uatcg.edgvbvh10:hover {
    pointer-events:auto;
    }
    </style>
    """
    st.markdown(manual_adjustment, unsafe_allow_html=True)
# css-5uatcg edgvbvh10
if cc2:
    testChoice = 1
    xunMeng = 1
    manual_adjustment = """
    <style>
    .css-1dwbmt0.e1tzin5v0, css-5uatcg.edgvbvh10:hover {
    pointer-events:auto;
    }
    </style>
    """
    st.markdown(manual_adjustment, unsafe_allow_html=True)

st.write("Your choice selected: " + str(xunMeng))