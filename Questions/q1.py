import streamlit as st

st.title("q1 title")

st.write("Is X without X still therefore X?")
cc1 = st.button("Still X")
cc2 = st.button("It's Y")

xunMeng = -1  # 0: xunzi, 1: mengzi


# buttons
if cc1:
    testChoice = 0
    xunMeng = 0
    manual_adjustment = """
    <style>
    .css-5uatcg.edgvbvh10.css-1fv8s86.e16nr0p34 {
    background-color: red;
    }
    </style>
    """
    st.markdown(manual_adjustment, unsafe_allow_html=True)
# css-5uatcg edgvbvh10
if cc2:
    testChoice = 1
    xunMeng = 1

st.write("Your choice selected: " + str(xunMeng))
