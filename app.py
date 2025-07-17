
import streamlit as st
from streamlit_option_menu import option_menu

# name = st.text_input("Enter your name")
# age = st.number_input("Enter your age")
# city = st.selectbox("Select your city", ["Mumbai", "Delhi", "Chennai", "Kolkata"])
# points = st.slider("Select your points", 0, 100)
# skills = st.multiselect("Select your skills", ["Python", "Java", "C", "C++"])
# gender = st.radio("Select your gender", ["Male", "Female"])
# st.checkbox("I agree to the terms and conditions")
# st.button("Submit")
# st.write(name)

# st.table({
#  "Name" : "Vinsup",
#  "Age" : 25,
#  "City" : "Mumbai"
# })

with st.sidebar:
    menu = option_menu(
        menu_title="My Project",
        options=["Home", "About", "Contact"],
        icons=['house','file-person','person-lines-fill']
    )

if menu == "Home":
    st.title("Registration Form")
    col1,col2 = st.columns(2)
    with col1:
        st.text_input("name")
    with col2:
        st.text_input("age")
        

elif menu == "About":
    st.title("About")
elif menu == "Contact":
    st.title("Contact")
