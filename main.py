import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv', sep=';')
print(df)
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jfif",width=150)


with col2:
    st.title("Phaneendra Sai Alluru")
    content = """
    Project Management professional with over 8 years of experience delivering consulting projects across the world. Experience in delivering high valued and highly time bounded projects in Architecture, Engineering, Construction and FMCG Sectors. 
• Designed solutions for Process Automation
• Developed enterprise level metrics to cater needs of stakeholders
• Lead teams in developing development centers from scratch
• Designed process to track, report and maintain enterprise level data for premium customers.
    """
    st.info(content)

content2 = """This is a section for my portfolio applications"""
st.write(content2)

col3,empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write("[Source Code](https://www.google.com)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://www.google.com)")