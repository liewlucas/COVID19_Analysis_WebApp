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
    st.write("***Student ID :*** ",id)

def course(course):
    st.write("***Course :*** ",course)

def loadlottie(url):
    #get url
    r = requests.get(url)

    # if returns error code 200, return none, else return json/ animation file
    if r.status_code != 200:
        return None

    return r.json()


#--- PAGE FUNCTIONS-------
def welcomepage():
    with st.container():
        st.header("Welcome to Team 7's Python Project")
        st.subheader("Tutorial Group: P1")
        st.write("---")
        st.subheader("Group Members:")
        #st.write("Group Members: Thaddeus, Lucas, Tommy, Zhi Yin, Siang Long")
        st.write("###")


    with st.container():
        stu1,stu2,stu3 = st.columns(3, gap= "medium")
        with stu1:
            profilepic("working2.png")
            teamdetails("LUCAS LIEW","2202454")
            course("_Applied Artificial Intelligence_")


        with stu2:
            profilepic("working2.png")
            teamdetails("KWOK YOKE YONG THADDAEUS", "2201966")
            course("_Applied Artificial Intelligence_")

        with stu3:
            profilepic("working2.png")
            teamdetails("CHUA YONG SOON TOMMY", "2203440")
            course("_ICT majoring SE_")


    with st.container():
        st.write("###")
        stu4,stu5,stu6 = st.columns(3,gap="medium")
        with stu4:
            profilepic("working2.png")
            teamdetails("TAY SIANG LONG ","2203190")
            course("_ICT majoring IS_")

        with stu5:
            profilepic("girl.png")
            teamdetails("ANG ZHI YIN", "2203561")
            course("_ICT majoring IS_")

        with stu6:
            st.write("")


def mainpage():
    #st.write("---")
    over1, over2 = st.columns(2, gap="medium")
    with over1:
        st.title("Project Overview")
        st.subheader("_Travelling in a Post Covid World_ ")
        st.write("_Global travel ground to a halt when Covid-19 proliferated. "
                 "Now, as the world heads into a post-pandemic era, global travel is picking up pace once again. "
                 "However, Travelling is not like it used to be, so lets travel safely in a world living with COVID-19._")

    with over2:
        animation = loadlottie("https://assets9.lottiefiles.com/packages/lf20_ogx9s7qo.json")
        st_lottie(animation, height=250)

    st.write("---")

    # with st.expander("Search and Filter"):
    #     userinput = st.text_input("Please Select a Country you would like to See.")
    #df = pd.read_csv('covid-19-daily-figures.csv')
    # df = pd.read_csv("https://covid.ourworldindata.org/data/latest/owid-covid-latest.csv")
    # st.write(df)
    #st.write("---")
    # if userinput:
    #     st.subheader("Interested in " + userinput + "?")
    #     st.write("Feel Free to click the buttons below to see other COVID19 related Data.")
    #     st.write("###")
    with st.container():
        st.header("Our Project Scopes are as Follows:")
        cat1, cat2, cat3 = st.columns(3, gap="medium")

        with cat1:
            st.write("")
            st.image("data.jpg")
            st.subheader("Global Covid Data")
            st.write("_Live Global Covid Datasets are available for users to View and Filter by Countries._")

            st.write(f'''
                        <a target="_self" href="Current_Covid_Situation">
                            <button 
                            style="background-color: #50C878; 
                            color: white; 
                            border: 2px solid #228B22;
                            border-radius: 5px;">
                                Global Covid Statistics
                            </button>
                        </a>
                        ''',
                     unsafe_allow_html=True
                     )
            st.write("###")

        with cat2:
            st.image("rules.jpg", use_column_width=True)
            #st.write("###")
            st.subheader("Travel Advisories")
            st.write("_Travel Advisories for all countries are available and users can filter by Departure and Destination Countries._")
            #st.write("###")
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

        with cat3:

            st.write("###")
            st.image("clinic.jpg",use_column_width=True)
            st.write("###")
            st.write("###")
            st.subheader("Pre-Departure ART Test")
            st.write("_Provides a list of MOH Approved Test Centres in Singapore, "
                     "allowing users to filter based on Location or Clinic Names._")
            st.write(f'''
                                <a target="_self" href="Clinics">
                                    <button 
                                    style="background-color: #0096FF; 
                                    color: white; 
                                    border: 2px solid #6495ED;
                                    border-radius: 5px;">
                                        Pre-Departure ART
                                    </button>
                                </a>
                                ''',
                     unsafe_allow_html=True
                     )









# ------ MAIN CODE START-------

#config
st.set_page_config(page_title="Team 7 INF1002", page_icon=":tada:", layout="wide")


with st.container():
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        animation2 = loadlottie("https://assets4.lottiefiles.com/private_files/lf30_mvurfbs7.json")
        st_lottie(animation2, height=200)

    with col2:
        st.title("COVID-19: Analysed")
        st.write("_This project seeks to provide an all-in-one platform to provide the reliable up-to-date information of the Covid-19 situation in Singapore and abroad._")

    with col3:
        animation = loadlottie("https://assets4.lottiefiles.com/packages/lf20_p2evb1ab.json")
        st_lottie(animation, height=200)



selected = option_menu(
    menu_title=None,
    options=["Welcome", "Project Overview"],
    icons=["house","book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Welcome":
    welcomepage()

elif selected == "Project Overview":
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


