import streamlit as st
from PIL import Image
import csv
import numpy as np
from streamlit_extras.switch_page_button import switch_page


# st.header("Are you XunZi or MengZi")

#############################################################
##################### INSTANTIATION #########################
#############################################################


# add dictionary of questions
# list of tuples?
# Must be odd number of questions**
qn_d = [("frontpage", "frontpage", "frontpage"),
        ("How do you view the inner beauty (virtuousness) of humans?",
         "Displaying the innate beauty of human nature",
         "Decorating/ beautifying self to hide the innate ugliness of human nature"),  # points refer to bool of 1st value being xunzi
        ("As a parent, how would you help your child build character and moral values?",
         "Create the ideal environment for their growth. Given nourishment, there is nothing that will not grow.",
         "The child’s moral education must be greatly interfered with."),
        ("Do you do good because...",
         "you do it to just spread goodness to others? ",
         "you hope to be treated by others the same way"),
        ("What is a gentleman?",
         "Someone who can overcome and eradicate desire for material interests",
         "Even when he speaks only a little, he is straightforward yet reserved in his use of words. "),
        ("What is ritual used for?",
         "To keep the temporary monarch in check, since they hold absolute moral power",
         "Ritual is required so that the chaotic morally equal but socially divided men in a society become well-ordered."),
        ("Should the king be the one owning most of  the resources or should resources be shared?",
         "Minimally. If the king has enough food, shelter and beauties, the king has been given enough.",
         "Yes! It is the luxuries the king can have that encourages him to follow the way"),
        ("question7",
         "question3_m",
         "question3_x"),
        ("question8",
         "question3_m",
         "question3_x"),
        ("question9",
         "question3_m",
         "question3_x"),
        ("question10",
         "question3_m",
         "question3_x"),
        ("question11",
         "question3_m",
         "question3_x")
        ]
len_qn = len(qn_d)-1
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

#############################################################
################## INSTANTIATION ENDS #######################
#############################################################

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
    # set the higher percentage to be written first
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
        f"## Based on the questions answered, you are: **:red[{compiledResults[philoIdx-1]}% {compiledResults[philoIdx]}]** and **:blue[{compiledResults[(philoIdx+1)%4]}% {compiledResults[(philoIdx+2)%4]}]**!!!")


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

my_bar = st.progress(min(index*int(100/(len(qn_d))), 100))

if index < len(qn_d):
    if index == 0:
        # dummy qn, for the beginning of quiz page to give context
        st.title("Welcome to the Mengzi Xunzi Profiling Game!")
        st.markdown("""
        What type of confucious school of thought to you subscribe to!
        Are you more of a Mengzi or a Xunzi? \n
        Take the quiz to understand more about yourself and get a 
        glimpse of how these philosophers believe you can live life to the fullest!!!
        """)
        moveFwd = st.button("Continue to quiz",
                            key="startQz",  on_click=add_count)
    else:
        # Asking all the questions
        with st.container():

            # add buttons
            question, text1, text2 = qn_d[index]
            st.header(question)
            # assuming always mengzi is btn1, xunzi is btn2
            clicked1 = st.button(
                text1, key="btn1", on_click=countMengzi, use_container_width=True)
            clicked2 = st.button(
                text2, key="btn2", on_click=countXunzi, use_container_width=True)

            # ONLY FOR DEBUGGING PURPOSES
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
    # count is > index of the list, show results of user
    with st.container():

        score = st.session_state.score
        mengScore = st.session_state.mengScore
        xunScore = st.session_state.xunScore
        # write results with tallyResults function
        tallyResults(mengScore, xunScore)

        # buttons go to next "page"
        # Ask users to go to the results page
        st.markdown(
            "Does the world side more with Mengzi or Xunzi? Head over to the Results page to find out more!")
        # might be out of place
        clicked1 = st.button("see all participants",
                             key="btn1",  on_click=add_count)

# else might be out of place
else:
    st.title("Results")
    del st.session_state['count']  # clear all cache from this test run
    del st.session_state['score']
    del st.session_state['xunScore']
    del st.session_state['mengScore']

    ratio = getScore()  # xunzi/total

    col1, col2 = st.columns(2)  # 2 columns layout
    with col1:
        st.title("Mengzi")
        setImage("img/xunzi.png", (1-ratio))
        # st.markdown("Some description")

    with col2:
        st.title("Xunzi")
        setImage("img/mengzi.png", ratio)
        # st.markdown("Some description")

    #############################################################
    ################# RESULTS SEGMENT END #####################
    #############################################################
