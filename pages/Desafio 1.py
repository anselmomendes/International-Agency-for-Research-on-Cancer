import pandas as pd
import sqlite3
import streamlit as st

st.set_page_config(layout="wide")

con = sqlite3.connect("data/tutorial.db")
attributable = pd.read_sql('select * from attributable', con=con)
preventable = pd.read_sql('select * from preventable', con=con)

st.markdown('### Reúna os dados de câncer incidente em 2012 por país, separados por sexo e região anatômica.')

attributable['Attributable fraction M'] = attributable['paf_obs_m'].apply(lambda x: '0%' if pd.isnull(x) else str(round(x,2)) + '%')
attributable['Attributable fraction F'] = attributable['paf_obs_f'].apply(lambda x: str(round(x,2)) + '%')
attributable['Attributable fraction B'] = attributable['paf_obs_both'].apply(lambda x: str(round(x,2)) + '%')

attributable = attributable[['country', 'continent', 'cancer', 'Attributable fraction M', 'Attributable fraction F', 'Attributable fraction B']]   


st.write(attributable)

#st.table(attributable, )
