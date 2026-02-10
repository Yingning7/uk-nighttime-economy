import streamlit as st

home_page = st.Page("./sub_pages/home.py", title="Home", icon="🏠", default=True)
night_workforce_page = st.Page("./sub_pages/night_workforce.py", icon="👷", title="Night Workforce", default=False)
night_business_page = st.Page("./sub_pages/night_business.py", icon="💼", title="Night Business", default=False)
night_workplaces_page = st.Page("./sub_pages/night_workplaces.py", icon="🏢", title="Night Workplaces", default=False)

pg = st.navigation([home_page, night_workforce_page, night_business_page, night_workplaces_page], position="sidebar", expanded=True)

st.set_page_config(
    page_title="UK Nighttime Economy",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg.run()
