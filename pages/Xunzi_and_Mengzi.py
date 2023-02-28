import streamlit as st


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
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n
Lorem \n


Mengzi
---
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
