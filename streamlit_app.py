# import module
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import notion_df

from PIL import Image


st.set_page_config(
    page_title="Hello hello",
    page_icon="👋",
)

image = Image.open('cyna.jpg')

st.image(image)

# Title
st.title("Competences ")
st.caption("Nous ....")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')




#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)


st.header("Page 2 - Intrusion detection dashboard")






#df = pd.DataFrame(data)
