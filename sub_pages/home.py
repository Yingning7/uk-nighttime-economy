from pathlib import Path
import base64

import streamlit as st

st.title("The Evolution of UK Nighttime Economy")

with open(Path(__file__).parents[1] / Path("assets/pictures/background.jpg"), mode="rb") as fp:
    background_image = base64.b64encode(fp.read()).decode()

st.markdown(
     f"""
     <style>
     .stApp {{
         background-image: url("data:image/jpg;base64,{background_image}");
         background-attachment: fixed;
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )
