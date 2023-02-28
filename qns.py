import streamlit as st
from PIL import Image
import csv
import numpy as np
from streamlit_extras.switch_page_button import switch_page


# st.header("Are you XunZi or MengZi")

################ INSTANTIATION #############

# add dictionary of questions
# list of tuples?
# Must be odd number of questions**
qn_d = [
    ("How do you view the inner beauty (virtuousness) of humans?",
     "Displaying the innate beauty of human nature",
     "Decorating/ beautifying self to hide the innate ugliness of human nature",
     -1),  # points refer to bool of 1st value being xunzi
    ("As a parent, how would you help your child build character and moral values?",
     "Create the ideal environment for their growth. Given nourishment, there is nothing that will not grow.",
     "The child’s moral education must be greatly interfered with.",
     -1),
    ("Do you do good because...",
     "you do it to just spread goodness to others? ",
     "you hope to be treated by others the same way",
     -1),
    ("What is a gentleman?",
     "Someone who can overcome and eradicate desire for material interests",
     "Even when he speaks only a little, he is straightforward yet reserved in his use of words. ",
     -1),
    ("What is ritual used for?",
     "To keep the temporary monarch in check, since they hold absolute moral power",
     "Ritual is required so that the chaotic morally equal but socially divided men in a society become well-ordered.",
     -1),
    ("Should the king be the one owning most of  the resources or should resources be shared?",
     "Minimally. If the king has enough food, shelter and beauties, the king has been given enough.",
     "Yes! It is the luxuries the king can have that encourages him to follow the way",
     -1),
    ("question7",
     "question3_m",
     "question3_x",
     -1),
    ("question8",
     "question3_m",
     "question3_x",
     -1),
    ("question9",
     "question3_m",
     "question3_x",
     -1),
    ("question10",
     "question3_m",
     "question3_x",
     -1),
    ("question11",
     "question3_m",
     "question3_x",
     -1)
]
len_qn = len(qn_d)
# maybe store xunzi and mengzi texts in txt files instead
xunzi_text = open("philos_texts/xunzi.txt", "r").read()
mengzi_text = open("philos_texts/mengzi.txt", "r").read()

# add if clause
# add counter for question num
if 'count' not in st.session_state:
    st.session_state['count'] = 0
    count = 0

if 'score' not in st.session_state:
    st.session_state['score'] = 0
    score = 0

if 'xunScore' not in st.session_state:
    st.session_state['xunScore'] = 0
    xunScore = 0

if 'mengScore' not in st.session_state:
    st.session_state['mengScore'] = 0
    mengScore = 0

################ INSTANTIATION END #############

# Adding count to Mengzi/Xunzi


def countMengzi():
    st.session_state.count += 1
    st.session_state.mengScore += 1
    st.session_state.score -= 1


def countXunzi():
    st.session_state.count += 1
    st.session_state.xunScore += 1
    st.session_state.score += 1
    # if xunzi at the bottom, it would add one (it's like hinge loss)


def add_count():
    # count = st.session_state.count
    st.session_state.count += 1


# can try image.resize(width,height) and then load new image
def setImage(pathToImg, ratio, caption=None):
    image = Image.open(pathToImg)
    width, height = image.size
    st.image(image, caption=caption, width=int(width*ratio))


def setScore(scholar):
    with open('scholars.txt', 'w') as f:
        f.write(scholar)
        f.write('\n')


def tallyResults(mengScore, xunScore):
    # percentage profile
    mengStyle = round(mengScore/len_qn*100, 2)
    xunStyle = round(xunScore/len_qn*100, 2)
    compiledResults = [mengStyle, "Mengzi", xunStyle, "Xunzi"]
    philoIdx = -1

    # setScore --> write to csv file
    if xunStyle > mengStyle:
        st.write(xunzi_text)
        setScore("Xunzi")
        philoIdx = 3
    else:
        st.write(mengzi_text)
        setScore("Mengzi")
        philoIdx = 1

    # write the percentage of xunzi mengzi per user
    st.markdown(
        f"Based on the questions answered, you are: **:red[{compiledResults[philoIdx-1]}% {compiledResults[philoIdx]}]** and **:blue[{compiledResults[(philoIdx+1)%4]}% {compiledResults[(philoIdx+2)%4]}]**!!!")


def getScore():
    with open('scholars.txt', 'r') as f:
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

my_bar = st.progress(index*int(100/len(qn_d)))

if index < len(qn_d):
    # add container
    with st.container():

        # add buttons
        question, text1, text2, score = qn_d[index]
        st.header(question)
        clicked1 = st.button(
            text1, key="btn1", on_click=countMengzi)
        clicked2 = st.button(text2, key="btn2", on_click=countXunzi)
        # for debugging purposes
        st.write("Score: " + str(st.session_state.score))
        st.write("Mengzi Score: " + str(st.session_state.mengScore))
        st.write("Xunzi Score: " + str(st.session_state.xunScore))

#############################################################
#################### QUIZ SEGMENT END #######################
#############################################################

#############################################################
################# RESULTS SEGMENT START #####################
#############################################################

# metrics should be addition of both and then a percentage per phil rather than negating one another?
elif index == len(qn_d):
    with st.container():

        score = st.session_state.score
        mengScore = st.session_state.mengScore
        xunScore = st.session_state.xunScore
        # write results
        tallyResults(mengScore, xunScore)

        # buttons go to next "page"
        clicked1 = st.button("see all participants",
                             key="btn1",  on_click=add_count)

else:
    st.title("Results")
    del st.session_state['count']  # clear all cache from this test run
    del st.session_state['score']

    ratio = getScore()  # xunzi/total

    col1, col2 = st.columns(2)  # 2 columns layout
    with col1:
        st.title("Mengzi")
        setImage("img/sampleperson.png", (1-ratio))
        st.markdown("Some description")

    with col2:
        st.title("Xunzi")
        setImage("img/sampleperson.png", ratio)
        st.markdown("Some description")

#############################################################
################# RESULTS SEGMENT END #####################
#############################################################
