import streamlit as st


def text_area(head, qns, mengzi, xunzi):
    header = st.subheader(head)
    questions = st.write(qns)
    expander1 = st.expander("Mengzi: ")
    expander1.write(mengzi)
    expander2 = st.expander("Xunzi: ")
    expander2.write(xunzi)


def description():
    all_descriptions = [(
        "Human Nature",
        "Qns: How do you view the inner beauty?\n\nWhen it comes to describing yourself as someone good, do you find yourself saying,\n\nHow is goodness in society incited?",
        """Mengzi claims that humans are innately good. He claims that the natural tendency of humans enables one to do good, and similarly to the main idea of Confucianism is the importance of good moral character, which can then affect the world around that person through 'cosmic harmony'. He explains that one has the impulse to save someone in trouble due to innate humaneness. The only factor that might stop us is 'fear', the lesser nature of humans that causes people to make conscious choices against the urge to save the person in trouble.""",
        """XunZi Claimed “In every case where people desire to become good, it is because their nature is bad.” He explains that people's nature is such that doing good means deviating from who they are. To have the desire to become good shows that humans are innately bad since one desires what one has less. Pg 249, 251 (line135)"""
    ), (
        "Governance",
        "Qns: As a parent, how would you help your child build character and moral values?,\n\nIf a nation falls into turmoil, is it the fault of the people or the monarch?,\n\nWhat is ritual used for?,\n\nIs it necessary for the king to be given luxuries?",
        """MengZi claims “Given nourishment, there is nothing that will not grow.” [6A8] If you worry that your seedlings are not growing, and pull them up, they will wither. [2A2] These reflect Mengzi's belief that a good governing body is one that provides necessary environment while not interfering with individuals. That providing the their people with basic necessities was enough for cultivation of the mind. """,
        """XunZi claims that the child’s moral education must be greatly interfered with. He states that “crooked wood must await steaming and straightening on the shaping frame, and only then does it become straight.” “Blunt metal must await honing and grinding, and only then does it become sharp”. With the imagery of metal bending, likening human nature to metal, we see that Xunzi believes that discipline and rituals are necessary to reshape innate human nature. And that interference is greatly necessary in governance(chpt 23, line 20)""",
    ), (
        "GentleMan/ Ideal Man",
        "Qns: Throughout your life, how do you improve yourself as a person?,\n\nWhat is a gentleman?,\n\nIf you did a mistake or something wrong deliberately do you find yourself more often to\n\nIf you were put on the death sentence for something you didn't do, and were offered a way out but to stay a criminal, would you",
        """Mengzi claims that ““It is only a gentleman who will be able to have a constant mind despite being without a constant means of livelihood.” He believed that a true gentleman is one that would not lose his morals even if he lacked basic necessities like food and water, and even life. He claims that as a gentleman, one would uphold the values and rituals, even if at the cost of one's livelihood because such actions transcend over having a continued livelihood. (book 1A page 11)""",
        """Xunzi believed that anyone has the potential to become a gentleman as long as one is willing to commit. He stated that a gentleman constantly makes the effort to accumulate culture and continues to learn, following the ritual and yi. Comparing a petty man and a gentleman, Xunzi stated that the difference was not because of their incapability to become each other but their decision on who they wanted to become individually. It is the choice of individuals to decide if they want to commit to becoming a gentleman or return to nature and be the petty man they originally were meant to be. (Chp 23, line 38-40), 
        \n XunZi consider’s the well bred gentleman to “[conform] to the proper model as surely as though being regulated by a carpenter's ink-line” (chpt 23, line 322-326) when arguing. Just like the well practiced straight line that is the carpenter's ink-line, Xunzi believes a well bred gentleman to be someone who is disciplined and extremely skilled in following the line. In this case the line refers to the ritual propriety in everything one does in daily life. """,
    ), (
        "Education",
        "Qns: Imagine you have just given a second chance for someone to prove their worth/character, yet he still did something bad, would you still be willing to give him another chance to correct his mistakes on his own?,\nPurpose of education",
        """The goodness of people displayed would mean not departing from one’s nature. Goodness is practiced and cultivated by people naturally. He promotes the manifestation of goodness as though individuals are growing sprouts, likening individuals to gardeners. To grow goodness and become a better person, one needs to master achieving balance. Individuals should provide the space for goodness to develop and intervene in the learning process when required.(book 2A, pg31)""",
        """Goodness is practiced and cultivated by people naturally. He promotes the manifestation of goodness as though individuals are growing sprouts, likening individuals to gardeners. To grow goodness and become a better person, one needs to master achieving balance. Individuals should provide the space for goodness to develop and intervene in the learning process when required. (chapt 23, line 95-100)"""
    )
    ]

    for tuple in all_descriptions:
        head, qns, menzi, xunzi = tuple
        view = text_area(head, qns, menzi, xunzi)


def qn_d():
    qn_d = [("frontpage", "frontpage", "frontpage"),
            ("How do you view inner beauty?",  # points refer to bool of 1st value being xunzi
             "The nature of an individual is malleable and can be decorated as one chooses, much like a ceramic pot.",
             "The nature of an individual is inherent, and it simply needs to be given the right circumstances to blossom.", 1),
            ("Throughout your life, how do you improve yourself as a person?",
             "Give yourself the space to explore and develop through your trial and errors in life",
             "Read self-help books and implement their recommendations in your daily life", 0),
            ("As a parent, how would you help your child build character and moral values?",
             "The child’s moral education must be greatly interfered with.",
             "Create the ideal environment for their growth. There is nothing that will not grow with nourishment", 1),
            ("If a nation falls into turmoil, is it the fault of the people or the monarch?",
             "The monarch: the monarch has more than sufficient to live off and experience luxuries no one else can. He should then hold himself to the highest moral standard.",
             "The monarch: Despite the people’s vices, the monarch has not enforced sufficient ritual and yi (virtue) in his people. The people are hence not virtuous. Leading to the nation falling into turmoil", 0),
            ("When it comes to describing yourself as someone good, do you find yourself saying",
             "I am ___",
             "I will ___", 0),
            ("How is goodness in society incited?",
             "Goodness in society requires constant and conscious interference by the governing body to produce.",
             "Goodness results from humaneness, and would happen without interference.", 1),
            ("What is a gentleman?",
             "Someone who speaks a little, straightforward yet reserved in his use of words. Someone who is disciplined and always putting in effort in what he does.",
             "Someone who can overcome and eradicate desire for material interests", 1),
            ("What are rituals used for?",
             "Rituals are only used to keep the temporary monarch in check since they hold absolute moral power",
             "Ritual is necessary to maintain order in society. Society is inherently chaotic since men who are morally equal are treated differently. Discontent will eventually arise if not for ritual.", 0),
            ("Is it necessary to give kings luxuries?",
             "Yes! Kings receiving luxuries is the order of society. Therefore the structure of society is maintained. ",
             "Minimally. If the king has enough food, shelter, and beauty, the king has enough.", 1),
            ("Imagine you have just given a second chance for someone to prove their worth/character, yet he still did something bad. Would you still be willing to give him another chance to correct his mistakes on his own?",
             "Yes",
             "No", 0),
            ("If you deliberately did a mistake or something wrong, do you find yourself more often to",
             "Feeling bad and realizing the mistake you have done",
             "Being pointed out by others on your mistake", 0),
            ("If you were on the death sentence for something you didn’t do and were offered a way out, but to stay a criminal. Would you:",
             "No (escape prison, keep your life and stay wronged)",
             "Yes (stay in prison and die knowing you did no wrong)", 1),
            ("Purpose of education",
             "should be holistic and encompass all aspects of human experience, including ethical, intellectual, and physical development",
             "About creating discipline and enforcing order into every individual’s mind from a young age", 0),
            ]
    return qn_d
