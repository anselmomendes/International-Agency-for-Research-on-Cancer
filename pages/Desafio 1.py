import pandas as pd
import sqlite3
import streamlit as st

st.set_page_config(layout="wide")

con = sqlite3.connect("data/tutorial.db")
attributable = pd.read_sql('select * from attributable', con=con)
preventable = pd.read_sql('select * from preventable', con=con)

st.markdown('### Reúna os dados de câncer incidente em 2012 por país, separados por sexo e região anatômica.')

attributable['Attributable fraction M'] = attributable['paf_obs_m'].apply(lambda x: '0%' if pd.isnull(x) else str(round(x*100,2)) + '%')
attributable['Attributable fraction F'] = attributable['paf_obs_f'].apply(lambda x: '0%' if pd.isnull(x) else str(round(x*100,2)) + '%')
attributable['Attributable fraction B'] = attributable['paf_obs_both'].apply(lambda x: '0%' if pd.isnull(x) else str(round(x*100,2)) + '%')

#filtros
col1, col2, col3 = st.columns(3)

with col1:
 option1 = st.selectbox(
   "Continent",
   (attributable.continent.unique()),
   index=None,
   placeholder="Select continent...",
)
if option1 is not None:
    attributable = attributable[attributable['continent'] == option1]

with col2:
 option2 = st.selectbox(
   "Country",
   (attributable.country.unique()),
   index=None,
   placeholder="Select Country...",
)
if option2 is not None:
    attributable = attributable[attributable['country'] == option2]

with col3:
 option3 = st.selectbox(
   "Cancer",
   (attributable.cancer.unique()),
   index=None,
   placeholder="Select Cancer...",
)
if option3 is not None:
    attributable = attributable[attributable['cancer'] == option3]

attributable = attributable[['country', 'continent', 'cancer', 'Attributable fraction M', 'Attributable fraction F', 'Attributable fraction B']]   


st.write(attributable)

#st.table(attributable, )
