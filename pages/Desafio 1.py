import pandas as pd
import sqlite3
import streamlit as st

con = sqlite3.connect("data/tutorial.db")
attributable = pd.read_sql('select * from attributable', con=con)
preventable = pd.read_sql('select * from preventable', con=con)

st.markdown('### Reúna os dados de câncer incidente em 2012 por país, separados por sexo e região anatômica.')

st.write(attributable)

st.write(preventable)