import streamlit as st

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

