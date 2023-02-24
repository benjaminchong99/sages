import streamlit as st
from PIL import Image
import csv
import numpy as np

# add progress bar

# st.header("Are you XunZi or MengZi")

################ INSTANTIATION #############

# add dictionary of questions
qn_d = [
    ("How do you view the inner beauty (virtuousness) of humans?", "Displaying the innate beauty of human nature", "Decorating/ beautifying self to hide the innate ugliness of human nature", -1), # points refer to bool of 1st value being xunzi
    ("question", "question 2_x", "question 2_m", 1),
    ("question", "question 3_m", "question 3_x", -1)
    ]   

xunzi_text = """You are a serious and methodical individual who are always focused on your goals. You are the type of character who carefully plans out your moves and always follows the rules, even if it means taking a more difficult path. 

When seeking a lifelong spouse, you find a partner who shares your values and beliefs, and you look for someone who is willing to work hard and follow his lead. 

You often face challenges that test your patience and your ability to adapt to unexpected circumstances. However, in the face of challenges you would always rely on your intelligence and ability to strategize in order to overcome these obstacles.

According to XunZi's interpretation of confucius, he recommends you [continue this later]
"""
mengzi_text = """You are a charismatic and compassionate individual who always puts others first. You are the type of character who is always willing to lend a hand to those in need, even if it means taking a risk. 

When seeking a lifelong spouse, you find a partner who shares your values of kindness and empathy, and you look for someone who is willing to work with you as a team. 

You often face challenges that test your emotional intelligence and your ability to connect with others on a deep level. However, in the face of challenges you would always rely on his natural charm and his ability to inspire others in order to overcome these obstacles.

According to MengZi's interpretation of confucius, he recommends you [continue this later]
"""

# add if clause
# add counter for question num
if 'count' not in st.session_state:
    st.session_state['count'] = 0
    count = 0

if 'score' not in st.session_state:
    st.session_state['score'] = 0
    score = 0

################ INSTANTIATION END #############


def add_top_count(x):
    count = st.session_state.count
    score = st.session_state.score
    st.session_state.count = count + 1
    st.session_state.score = score + x

def add_bottom_count(x):
    count = st.session_state.count
    score = st.session_state.score
    st.session_state.count = count + 1
    st.session_state.score = score - x
    # if xunzi at the bottom, it would add one (it's like hinge loss)

def add_count():
    count = st.session_state.count
    st.session_state.count = count + 1

def setImage(pathToImg, ratio, caption=None):
    image = Image.open(pathToImg)
    width, height = image.size
    st.image(image, caption=caption, width=int(width*ratio))

def setScore(scholar):
    with open('scholars.txt','w') as f:
        f.write(scholar)
        f.write('\n')

def getScore():
    with open('scholars.txt','r') as f:
        full = f.read()
        flist = full.split('\n')

        farray = np.array(flist)
        values, counts = np.unique(farray, return_counts=True)

        return counts[0]/sum(counts)

#############################################################
#################### QUIZ SEGMENT START #####################
#############################################################

# add quiz end page
index = st.session_state.count

my_bar = st.progress(index*int(100/4))

if index < 3:
    # add container
    with st.container():
    
        # add buttons
        question, text1, text2, score = qn_d[index]
        st.header(question)
        clicked1 = st.button(text1, key="btn1", use_container_width=True,on_click=add_top_count, args=[score])
        clicked2 = st.button(text2, key="btn2", use_container_width=True,on_click=add_bottom_count, args=[score])

#############################################################
#################### QUIZ SEGMENT END #######################
#############################################################

#############################################################
################# RESULTS SEGMENT START #####################
#############################################################

elif index == 3: # to be changed to 12
    with st.container():

        score = st.session_state.score
        st.write(xunzi_text if score > 0 else mengzi_text)
        
        setScore("Xunzi" if score > 0 else "Mengzi") # write to csv file
        
        clicked1 = st.button("see all participants", key="btn1", use_container_width=True,on_click=add_count) # buttons go to next "page"

else:
        st.title("Results")
        del st.session_state['count'] # clear all cache from this test run
        del st.session_state['score']

        ratio = getScore() # xunzi/total

        col1, col2 = st.columns(2)  # 2 columns layout
        with col1:
            st.title("Mengzi")
            setImage("img/sampleperson.png",(1-ratio))
            st.markdown("Some description")

        with col2:
            st.title("Xunzi")
            setImage("img/sampleperson.png",ratio)
            st.markdown("Some description")

#############################################################
################# RESULTS SEGMENT END #####################
#############################################################
