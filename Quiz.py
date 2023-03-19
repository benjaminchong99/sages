import streamlit as st
from PIL import Image
import csv
import numpy as np
from Description import description, qn_d

# st.header("Are you XunZi or MengZi")

#############################################################
##################### INSTANTIATION #########################
#############################################################

# add dictionary of questions
# list of tuples?
# Must be odd number of questions**
qn_d = qn_d()

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


def countScore(isXunZi):  # isXunZi is 0 or 1
    st.session_state.count += 1
    st.session_state.mengScore += isXunZi
    st.session_state.xunScore += 1-isXunZi

# can try image.resize(width,height) and then load new image


def setImage(pathToImg, ratio, caption=None):
    image = Image.open(pathToImg)
    width, height = image.size
    st.image(image, caption=caption, width=int(width*ratio))


def add_count():
    st.session_state.count += 1


def setScore(scholar):
    with open('scholars.txt', 'a') as f:
        f.write(scholar)
        f.write("\n")
        f.close()


def tallyResults(mengScore, xunScore):
    # percentage profile
    mengStyle = round(mengScore/len_qn*100, 2)
    xunStyle = round(xunScore/len_qn*100, 2)
    compiledResults = [mengStyle, "Mengzi", xunStyle, "Xunzi"]
    philoIdx = -1

    # setScore --> write to csv file
    # set the higher percentage to be written first
    # write the percentage of xunzi mengzi per user
    st.markdown(
        f"Based on the questions answered, you are: \n## **:red[{compiledResults[philoIdx-1]}% {compiledResults[philoIdx]}]** and **:blue[{compiledResults[(philoIdx+1)%4]}% {compiledResults[(philoIdx+2)%4]}]**")

    if xunScore > mengScore:
        st.markdown(xunzi_text)
        setScore("XunZi")
        philoIdx = 3
    else:
        st.markdown(mengzi_text)
        setScore("MengZi")
        philoIdx = 1


def getScore():
    with open('scholars.txt', 'r') as f:
        full = f.read()
        flist = full.split('\n')

        farray = np.array(flist)
        values, counts = np.unique(farray, return_counts=True)
        # print(counts)

        x = ["MengZi", "XunZi"]
        y = [int(counts[1]), int(counts[2])]
        f.close()
    return x, y

#############################################################
#################### QUIZ SEGMENT START #####################
#############################################################


# add quiz end page
index = st.session_state.count
bar_index = min(len(qn_d), index)

my_bar = st.progress(bar_index*int(100/(len(qn_d))))

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
            # where first question is XunZi
            question, text1, text2, isXunZi = qn_d[index]
            st.header(question)
            # assuming always mengzi is btn1, xunzi is btn2
            clicked1 = st.button(text1, key="btn1", on_click=countScore,
                                 use_container_width=True, args=(1-isXunZi, ))
            clicked2 = st.button(text2, key="btn2", on_click=countScore,
                                 use_container_width=True, args=(isXunZi, ))

            # ONLY FOR DEBUGGING PURPOSES
            # st.write("Mengzi Score: " + str(st.session_state.mengScore))
            # st.write("Xunzi Score: " + str(st.session_state.xunScore))

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

        mengScore = st.session_state.mengScore
        xunScore = st.session_state.xunScore
        # write results with tallyResults function
        tallyResults(mengScore, xunScore)

        # buttons go to next "page"
        # Ask users to go to the results page
        st.markdown(
            ":orange[Does the responses from others side more with Mengzi or Xunzi? Head over to the Results page to find out more!]")
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

    x, y = getScore()  # xunzi/total

    d = {x[0]: y[0], x[1]: y[1]}
    col1, col2, col3 = st.columns(3)  # 2 columns layout
    with col1:
        st.title("Mengzi")
        setImage("img/mengziPortrait.jpg", 0.6)
        # st.markdown("Some description")
    with col2:
        # add bar chart
        st.markdown("\n\n\n")
        st.bar_chart(d)
    with col3:
        st.title("Xunzi")
        setImage("img/xunziPortrait.png", 0.3)
        # st.markdown("Some description")

    # the descriptions of the questions
    st.write("""### About the Philosophers \n\n"
        Mengzi(孟子) and Xunzi(荀子) were both Confucian philosophers that lived in ancient China during the 4th cetury BCE and 3rd century BCE respectively.\n\nMengzi was born in the State of Zou and served as a government official and scholar in the State of Qi during the Warring States period. He is well-known mainly for his claim that “human nature is good.” On the other hand, Xunzi was born in the State of Zhao and studied at the prestigious Jixia Academy, where he studied the major philosophical traditions of his time. He is well-known mainly for having contrasting views from Mengzi and claiming “human nature is bad.” Read on below to learn more about how each philosopher viewed the different topics related to the questions!
        """)
    description()

    #############################################################
    ################# RESULTS SEGMENT END #####################
    #############################################################
