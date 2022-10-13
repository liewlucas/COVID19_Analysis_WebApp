#INF1002 Python Project Group 7

#pandas for data processing
import pandas as pd

#streamlit for gui
import streamlit as st

#streamlit option menu
from streamlit_option_menu import option_menu

#imports for animation
import requests
from streamlit_lottie import st_lottie

import urllib

#------ FUNCTIONS ------
def profilepic(image):
    st.image(image, width=100)

def teamdetails(name, id):
    st.subheader(name)
    st.write("Student ID: ",id)

def mainpage():
    st.write("---")
    st.header("COVID19 at a glance")
    with st.expander("Search and Filter"):
        userinput = st.text_input("Please Select a Country you would like to See.")
    df = pd.read_csv('covid-19-daily-figures.csv')
    st.write(df)
    st.write("---")
    if userinput:
        st.subheader("Interested in " + userinput + "?")
        st.write("Feel Free to click the buttons below to see other COVID19 related Data.")
        st.write("###")
        st.write(f'''
            <a target="_self" href="Travel_Advisory">
                <button 
                style="background-color: #FA5F55; 
                color: white; 
                border: 2px solid #E30B5C;
                border-radius: 5px;">
                    Travel Advisories
                </button>
            </a>
            ''',
                 unsafe_allow_html=True
                 )
        st.write("###")
        st.write(f'''
                            <a target="_self" href="Clinics">
                                <button 
                                style="background-color: #87CEEB; 
                                color: white; 
                                border: 2px solid #6082B6s;
                                border-radius: 5px;">
                                    Pre-Departure ART
                                </button>
                            </a>
                            ''',
                 unsafe_allow_html=True
                 )


def welcomepage():
    with st.container():
        st.header("Welcome to Team 7's Python Project")
        st.subheader("Tutorial Group: P1")
        st.write("---")
        st.subheader("Group Members:")
        #st.write("Group Members: Thaddeus, Lucas, Tommy, Zhi Yin, Siang Long")
        st.write("###")


    with st.container():
        a,b,c = st.columns(3, gap= "medium")
        with a:
            profilepic("working2.png")
            teamdetails("LUCAS LIEW","2202454")

        with b:
            profilepic("working2.png")
            teamdetails("KWOK YOKE YONG THADDAEUS", "2201966")

        with c:
            profilepic("working2.png")
            teamdetails("CHUA YONG SOON TOMMY", "2203440")


    with st.container():
        st.write("###")
        a,b,c = st.columns(3,gap="medium")
        with a:
            profilepic("working2.png")
            teamdetails("TAY SIANG LONG ","2203190")

        with b:
            profilepic("girl.png")
            teamdetails("ANG ZHI YIN", "2203561")

        with c:
            st.write("")

def loadlottie(url):
    #get url
    r = requests.get(url)

    # if returns error code 200, return none, else return json/ animation file
    if r.status_code != 200:
        return None

    return r.json()

# ------ MAIN CODE START-------

#config
st.set_page_config(page_title="Team 7 INF1002", page_icon=":tada:", layout="wide")


with st.container():
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        animation2 = loadlottie("https://assets4.lottiefiles.com/private_files/lf30_mvurfbs7.json")
        st_lottie(animation2, height=200)

    with col2:
        st.title("COVID19: Analysed")
        st.write("_This project seeks to provide an all-in-one platform to provide the reliable up-to-date information of the Covid-19 situation in Singapore and abroad._")

    with col3:
        animation = loadlottie("https://assets4.lottiefiles.com/packages/lf20_p2evb1ab.json")
        st_lottie(animation, height=200)



selected = option_menu(
    menu_title=None,
    options=["Welcome", "Covid19 Statistics"],
    icons=["house","book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Welcome":
    welcomepage()

elif selected == "Covid19 Statistics":
    mainpage()


#with st.container():
#    st.write('---')
#    left, right = st.columns(2)
#    with left:
#        # covid daily figures
#        data = pd.read_csv('covid-19-daily-figures.csv')
#        st.table(data)
#    with right:
#        st.write("HELLO THIS IS RIGHT COLUMN")


