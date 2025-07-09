import streamlit as st
import langchain_helper as lc

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Pakistani", "Chinese", "Spanish", "Arabic", "Turkish", "Italian"))


if cuisine:
    response = lc.generate_res_name_and_items(cuisine)

    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**MENU ITEMS**")
    for item in menu_items:
        st.write("-", item)
 