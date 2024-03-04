# Desafio FFM

Nesse projeto foi elaborado uma solução end-to-end passando desde a etapa de scrapy e captura dos dados até a visualização dos dados. Foi feitu a captura e o tratamento das informações e estruturação no banco de dados. A etapa de agrupamento dos dados para construção dos gráficos foram bem importantes para o entendimento dos dados e apresentação dos insight.

A ultima etapa e principal analisou o impacto da relação dos dados de IMC x Cancer e Potencial de Prevenção. Esse tipo de trabalho é muito importante para direcionar tomadas de decisão e eficiencia dos gestores e governantes. O projeto poderia evoluir para um servidor público com dashbaords com os filtros e gráficos de mapas em uma segunda versão. 

##### Criação de um repositório no GIT

~~~powershell
git init
git add .
git commit -m 'criação do projeto'
git remote add origin git@github.com:anselmomendes/desafio_ffm.git
~~~

###### Foi implementado um banco de dados SQLite para estruturar os dados

~~~sql
select a.continent,
a.cancer,
a.country,
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
~~~

###### O desafio apresentado trouxe a seguinte questão:

<p align="center"><img src="https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/01.png" height="400"></p>

# A solução proposta foi apresentada nos seguintes topicos abaixo.

##### 1 - Reúna os dados de câncer incidente em 2012 por país, separados por sexo e região anatômica.

O site apresentava uma area de download dos dados, porem a combinação de arquivos necessários para a aquisição dos dados não é eficiente em vista que o problema pode escalar

~~~
10 (opções de cancer) * 3 (opções de sexo) * 6 (opções de continentes) * 2 (opções de bases) = 360 arquivos.
~~~
Criação do script jupyter de web scraping para download de dados foi feito para aquisição dos dados de forma automatica.

<p align="center"><img src="https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/00.png" height="400"></p>

A saida dos dados na figura abaixo referente ao primeiro item do desafio mostra as informações sobre pais, continente, sexo e tipo do cancer.

<p align="center"><img src="https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/02.png" height="400"></p>

##### 2 - Faça uma apresentação gráfica e análise detalhada dos dados.

Para uma melhor esperiencia foi criado um do projeto na ferramenta no streamlit.

![https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.gif](https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v02.gif)

Foi elaborado gráficos para analise de dados da média de casos de cancer entre o sexo masculino e feminino, comparado as caracteristicas por tipo de cancer, continente. E o rank dos paises com maior indice do mundo.

Lista dos gráficos elaborados

- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/03.png">Histograma da distribuição da porcentagem geral das relaçãoes com cancer</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/04.png">Porcentagem média geral da relação por continente</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/05.png">Porcentagem média geral da relação por tipo de cancer</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/07.png">Rank dos paises com maior taxa de relação entre cancer e IMC</a>

##### 3 - Faça uma comparação entre o cenário fração de casos de câncer em 2012 atribuíveis ao excesso de Índice de Massa Corporal (IMC) em países da América do Sul com o cenário previnível.

![https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.gif](https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.gif)

Fazendo o gruzamento dos dados dos casos de cancer que tiveram relação com o IMC e os dados da porcentagem de casos que poderiam ter sido evitados caso o indice do IMC tivesse se mantido. Foi gerado uma serie de gráficos apresentado os principais impactos na redução desses indices, agrupando por tipo de cancer e região.

Foi possivel observar que as regiões que esse indice poderia ter sido evitado foram continentes onde ouve um grande aumento no IMC dos seus habitantes, relacionado ao IDH desses paises.

Lista dos gráficos elaborados

- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/08.png">Top 10 maiores impacto na redução do cancer se os indices de IMC tivessem sido mantidos por paises.</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/09.png">Top 10 maiores impacto na redução do cancer se os indices de IMC tivessem sido mantidos por continentes.</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/10.png">Top 10 maiores impacto na redução do cancer se os indices de IMC tivessem sido mantidos por tipo de cancer.</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/11.png">Top 10 maiores impacto na redução do cancer se os indices de IMC tivessem sido mantidos por continentes.</a>
- <a href="https://raw.githubusercontent.com/anselmomendes/desafio_ffm/master/imagens/12.png">Histograma da distribuição da porcentagem reduzida do índice de cancer</a>

##### O resultado da saída do estudo se deu em comparar os dados do item 3 com os paises das americas com a media mundial.

![https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.gif](https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/17.png)

- Com esses gráfico abaixo podemos inferir que os casos de cancer na America do Sul está acima da média mundial em relação a todos os tipos de cancer
- O impacto se mantivessemos os indices de IMC seria maior na America do Sul que em relação a média mundial.

