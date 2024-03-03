# Desafio FFM
### Criação de um repositório no GIT

~~~powershell
git init
git add .
git commit -m 'criação do projeto'
git remote add origin git@github.com:anselmomendes/desafio_ffm.git
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

<video height="400" controls>
  <source src="imagens/v01.mp4" type="video/mp4">
</video>

<video height="400" controls>
  <source src="[imagens/v02.mp4](https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.mp4)" type="video/mp4">
</video>

![]([imagens/v01.mp4](https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.mp4)https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.mp4)

<video src='[your URL here](https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.mp4)https://github.com/anselmomendes/desafio_ffm/blob/master/imagens/v01.mp4' width=180/>

  
Criação das paginas para resolução dos itens do desafio
