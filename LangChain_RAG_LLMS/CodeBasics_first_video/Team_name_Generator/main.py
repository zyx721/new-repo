import streamlit as st

from langchain_helper import gen_team_name

st.title("Team name Generator")
event = st.sidebar.selectbox("Pick an event",("Hackathon","Ideathon","Robothon"))

if event :
    response = gen_team_name(event)
    st.header(response['restaurant_name'].strip())
    profile = response['menu_items'].strip().split(',')
    st.write("**Profiles**")
    for item in profile:
        st.write("-",item)
