import streamlit as st
import plotly 
def page1():
    st.title('About My Self')
    st.write('Hello Iam Bhargav, I was Graduated B.tech on June 2022. Till now I am developing my skills from sources like Courseera, analytics vidya & youtube etc., I can Build & evaluate ML & DL Models using packages like sklearn and tensorflow. There sare some projects I worked on, you can find these on my Github.')
     
    st.markdown('---')
    
    st.write('[LinkedIn](https://www.linkedin.com/in/bhargav-nagireddy/)')
    st.write('[GitHub](https://github.com/bhargav3233)')
def page2():
    st.write('This is page 2')

# Define the pages dictionary
PAGES = {
    "About Me": page1,
    "Word Cloud": page2
}

# Define the main function
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
