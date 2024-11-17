import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="GreenShift - Carbon Footprint Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.logo("../Images/menu.png")

pages = {
    "App Navigations": [
        st.Page("home.py", title="Home", icon='🏠' ,default=True),
        st.Page("developers.py", title="Developers | Team", icon='👨‍🏫'),
    ],
    "Modules": [
        st.Page("user_input.py", title="Calculate My Carbon Footprint", icon='🐾'),
        st.Page("recommendations.py", title="Recommendations",  icon='🤹‍♂️'),
        st.Page("Global_Climate.py", title="Global Carbon Emission",  icon='🏭'),
        st.Page("sustainability.py", title="Sustainable Practices",  icon='🌱')
    ]
}

pg = st.navigation(pages)
pg.run()
