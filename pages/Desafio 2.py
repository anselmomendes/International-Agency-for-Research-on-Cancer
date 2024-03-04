import pandas as pd
import sqlite3
import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")

con = sqlite3.connect("data/tutorial.db")
attributable = pd.read_sql('select * from attributable', con=con)
preventable = pd.read_sql('select * from preventable', con=con)

st.markdown('### Faça uma apresentação gráfica e análise detalhada dos dados.')

attributable['male'] = attributable['paf_obs_m'] * 100
attributable['famele'] = attributable['paf_obs_f'] * 100
attributable['both'] = attributable['paf_obs_both'] * 100

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



#histograma
fig = px.histogram(attributable, x=['male', 'famele'], title='Histograma da distribuição da porcentagem geral das relaçãoes com cancer')
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Qtd',
        titlefont_size=16,
        tickfont_size=14,
),
xaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))

st.plotly_chart(fig, use_container_width=True)

#media por continente
attributable_mean = attributable[['continent', 'male', 'famele', 'both']].groupby(['continent']).mean().reset_index()
fig = px.bar(attributable_mean, x='continent', y=['male', 'famele'], barmode="group", title='Porcentagem média geral da relação por continente')
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))
st.plotly_chart(fig, use_container_width=True)

# media por tipo de cancer
attributable_mean = attributable[['cancer', 'male', 'famele', 'both']].groupby(['cancer']).mean().reset_index()
fig = px.bar(attributable_mean, x='cancer', y=['male', 'famele'], barmode="group", title='Porcentagem média geral da relação por tipo de cancer')
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))
st.plotly_chart(fig, use_container_width=True)


#Rank dos paises com maior taxa de relação.
aux = attributable[['country', 'male', 'famele', 'both']].groupby(['country']).mean()
aux = aux.sort_values(by=['both'], ascending=False).reset_index()
aux = aux.head(20)
fig = px.bar(aux, x='country', y=['both'],  title='Rank dos paises com maior taxa de relação entre cancer e IMC.')# ,barmode="group")
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))
st.plotly_chart(fig, use_container_width=True)