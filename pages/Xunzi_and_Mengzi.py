import streamlit as st
from PIL import Image


#############################################################
################## MANUAL CSS SETTINGS ######################
#############################################################
st.markdown('''
<style>
h1{color: red;}
a{text-decoration: none;}
</style>
''', unsafe_allow_html=True)

#############################################################
#################### START OF CONTENT #######################
#############################################################

# add reference to which questions asked in the quiz

st.title("More about [Xunzi](#xunzi) and [Mengzi](#mengzi)")

st.markdown("""
or a [TLDR comparison](#comparison-table)

Xunzi
---
""")

st.image("img/xunziPortrait.png", width=250)
st.markdown("""
Xunzi 荀子 was a Confucian philosopher around the 4th century BCE in China. Xunzi is well-known for his claim that “human nature is bad.”
\n
#### On the innate nature of a person: \n
Xunzi 
#### On the goodness of a person: \n

#### On being a gentleman: \n

#### On ritual: \n

#### On the success of a monarch/governing system: \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n


Mengzi
---
""")
st.image("img/mengziPortrait.jpg", width=250)
st.markdown("""
Mengzi (or Mencius) was a Confucian philosopher around the 4th century BCE in China. He was born in the state of Zou and served as a government official and scholar in the State of Qi during the Warring States period. Mengzi is well-known for his claim that “human nature is good.” ...


#### On the innate nature of a person: \n

#### On the goodness of a person: \n

#### On being a gentleman: \n

#### On ritual: \n

#### On the success of a monarch/governing system: \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n

Comparison Table
---
| | Xunzi | Mengzi |
| --- | --- | --- |
| Innate Nature | content | content |
| Goodness | content | content |
| Gentleman | content | content |
| Ritual | content | content |
| Monarch | content | content |

""")
