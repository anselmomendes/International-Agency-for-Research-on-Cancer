import pandas as pd
import sqlite3
import streamlit as st

con = sqlite3.connect("data/tutorial.db")
attributable = pd.read_sql('select * from attributable', con=con)
preventable = pd.read_sql('select * from preventable', con=con)

st.markdown('''### __CASE 1:__

Case para Seleção de Especialista em dados - Análise da Fração de Casos de Câncer Atribuíveis ao Índice de Massa Corporal (IMC) em 2012 na América do Sul.)

##### __Introdução:__

Você foi contratado para liderar uma análise que visa entender a fração de casos de câncer em 2012 atribuíveis ao excesso de Índice de Massa Corporal (IMC) em países da América do Sul. O objetivo é comparar essa fração entre os diferentes países da região.

##### __Contexto:__

Utilizaremos dados para analisar a carga de câncer atribuível ao excesso de peso corporal em diferentes países. Os dados estão disponíveis para ambos os sexos e abrangem todos os tipos de câncer em várias regiões anatômicas. Disponível em: https://gco.iarc.fr/causes/obesity/tools-map

### __Desafio:__

##### __Coleta de Dados:__

- Reúna os dados de câncer incidente em 2012 por país, separados por sexo e região anatômica.

- Faça uma apresentação gráfica e análise detalhada dos dados.

- Faça uma comparação entre o cenário fração de casos de câncer em 2012 atribuíveis ao excesso de Índice de Massa Corporal (IMC) em países da América do Sul com o cenário previnível.
''')