
import pandas as pd
import sqlite3
import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")

con = sqlite3.connect("data/tutorial.db")

script = '''
select a.continent,
a.cancer,
a.country,
a.region,
a.paf_obs_m as male_att,
a.paf_obs_f as famele_att,
a.paf_obs_both as both_att,
p.paf_obs_m as male_prev,
p.paf_obs_f as famele_prev,
p.paf_obs_both as both_prev,
p.paf_obs_m * a.paf_obs_m as male_diff,
p.paf_obs_f * a.paf_obs_f as famele_diff,
p.paf_obs_both * a.paf_obs_both as both_diff
from attributable a
left join preventable p on a.country = p.country and a.cancer = p.cancer
'''

join = pd.read_sql(script, con=con)
#preventable = pd.read_sql('select * from preventable', con=con)

st.markdown('### Faça uma comparação entre o cenário fração de casos de câncer em 2012 atribuíveis ao excesso de Índice de Massa Corporal (IMC) em países da América do Sul com o cenário previnível.')

join['male_att'] = join['male_att'] * 100
join['famele_att'] = join['famele_att'] * 100
join['both_att'] = join['both_att'] * 100

join['male_prev'] = join['male_prev'] * 100
join['famele_prev'] = join['famele_prev'] * 100
join['both_prev'] = join['both_prev'] * 100

join['male_diff'] = join['male_diff'] * 100
join['famele_diff'] = join['famele_diff'] * 100
join['both_diff'] = join['both_diff'] * 100

join['reduction_male'] = join['male_att'] - join['male_diff']
join['reduction_famele'] = join['famele_att'] - join['famele_diff']
join['reduction_both'] = join['both_att'] - join['both_diff']

#Top 10 maiores impacto na redução do cancer se os indices de IMC tivessem sido mantidos por paises
aux = join[['continent', 'reduction_male', 'reduction_famele', 'reduction_both']].groupby(['continent']).mean()
aux = aux.sort_values(by=['reduction_both'], ascending=False).reset_index()
aux = aux.head(10)
fig = px.bar(aux, x='continent', y=['reduction_both'],  title='Top 10 maiores impacto na redução do cancer se os indices de IMC tivessem sido mantidos por continentes.')# ,barmode="group")
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))
st.plotly_chart(fig, use_container_width=True)

# [America x Media Mundial] Percentual da relação entre IMC e os tipos de cancer por tipo de cancer.
aux = join[['cancer', 'both_att']].groupby(['cancer']).mean()
aux = aux.sort_values(by=['both_att'], ascending=False).reset_index()
aux1 = pd.DataFrame(data=join[join['region'] == 'Latin America & Caribbean'][['cancer', 'both_att']].groupby(['cancer']).mean())
aux1 = aux1.rename(columns={'both_att': 'both_att_ameriacan_south'})
aux = pd.merge(aux, aux1, on='cancer', how='left')


fig = px.bar(aux, x='cancer', y=['both_att', 'both_att_ameriacan_south'], barmode="group",  title='[America x Media Mundial] Percentual da relação entre IMC e os tipos de cancer.')# ,barmode="group")
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))
st.plotly_chart(fig, use_container_width=True)


# [America x Media Mundial] percentual de casos de cancer que poderiam ser reduzidos se os niveis de IMC tivessem se mantidos.'
aux = join[['cancer', 'reduction_both']].groupby(['cancer']).mean()
aux = aux.sort_values(by=['reduction_both'], ascending=False).reset_index()
aux1 = pd.DataFrame(data=join[join['region'] == 'Latin America & Caribbean'][['cancer', 'reduction_both']].groupby(['cancer']).mean())
aux1 = aux1.rename(columns={'reduction_both': 'reduction_both_ameriacan_south'})
aux = pd.merge(aux, aux1, on='cancer', how='left')


fig = px.bar(aux, x='cancer', y=['reduction_both', 'reduction_both_ameriacan_south'], barmode="group",  title='[America x Media Mundial] Percentual de casos de cancer que poderiam ser reduzidos se os niveis de IMC tivessem se mantidos.')# ,barmode="group")
fig.update_layout(bargap=0.1,
    yaxis=dict(
        title='Porcentagem (%)',
        titlefont_size=16,
        tickfont_size=14,
))
st.plotly_chart(fig, use_container_width=True)