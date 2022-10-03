from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Website", page_icon=":runner:", layout="wide")


def load_lottieurl(url):
    result = requests.get(url)
    if result.status_code != 200:
        return None
    return result.json()


# ----- LOAD LOCAL CSS -----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ----- LOAD ASSETS -----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_o6spyjnc.json")
img_lottie = Image.open("images/streamlit_lottie.png")
img_qr = Image.open("images/project-2.png")


# ----- HEADER SECTION -----
with st.container():
    st.subheader("Hi, I am Kaushtubh :wave:")
    st.title("A Cloud SDET Professional II  From India")
    st.write("I am passionate about finding ways to use Python and Powershell to be more efficient and effective in "
             "business setting")
    st.write("[Learn More >](https://kaushtubh-jha.github.io/my-portfolio/)")


# ----- What I Do -----
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I Do")
        st.write("##")
        st.write("""
        I'm technology driven, self-motivated and dedicated professional from Jalandhar, Punjab, working in Cloud Automation and SDET role. 
        - Diversified experience as Quality Analyst and Engineer with testing of stand - alone, client server, web-based Database, Multiple Environments, Cloud. 
        - 5+ years of experience which includes various types of SDET testing, functional, security, performance, automated, acceptance and Selenium testing.
        - Have an experience in wide variety of domains which includes Server, Cloud, IT industry and Security. 
        
        - Extensive experience in implementing QA Methodologies, Test Plans, Test Cases, Test Scenarios and test deliverables for various applications. 
        - Expertise in functional testing, integration testing, regression testing, black box testing, white box testing, unit testing, GUI testing, system, Regression, integration, and UAT testing browser compatibility testing.
        - Excellent understanding of Software Quality Assurance Techniques and strong knowledge of Software Development Life Cycle (SDLC) and Software Testing Life Cycle (STLC). 
        - Skilled in developing and executing test cases for developed automation script with Selenium Suite, Selenium Grid. 
        - Expertise in writing and executing Test Scripts to implement Test Cases, Test Scenarios.
        """)
    st.write("[GitHub Page >](https://github.com/Kaushtubh-Jha)")

    with right_col:
        st_lottie(lottie_coding, height=300, key="coding")


# ----- PROJECTS -----
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(img_lottie)
    with text_col:
        st.subheader("Integrate Lottie Animation Inside Your Streamlit App")
        st.write("""
        Learn how to use Lottie files in Streamlit!
        Animation make web app more engaging and fun, and Lottie files are the easiest way to do it.
        In this GitHub Repository you will find this Web App code. 
        """)
        st.markdown("[Code Link...](https://github.com/Kaushtubh-Jha/Streamlit-Simplet-WebSite)")
with st.container():
    st.write("---")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(img_qr)
        with text_col:
            st.subheader("Data Science Web App for Analysis of Tweets!")
            st.write("""
                Learn how to implement Data Science Webb App using Streamlit!
                This project will describes the sentimental analysis of tweets about US Airlines.
                In this GitHub Repository you will find this Web App code. 
                """)
            st.markdown("[Code Link...](https://github.com/Kaushtubh-Jha/Tweets-Streamlit)")


# ----- CONTACT FORM -----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kaushtubhjha45.kj@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your name" required>
        <input type="email" name="email" placeholder= "Your email" required>
        <textarea name="message" name="email" placeholder= "Your message here..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()

