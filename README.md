# VoilApp
Projeto Final - ISEL - LEIM 2020/2021 - 61D - 45144 46296
Tiago Oliveira | Tiago Gil

![Logo](03_Implementacao/resources/footer.png)

## Python

Como base para todas as outras dependências da aplicação é necessário a
presença de Python no sistema com isso as versões recomendadas são 3.7.x,
3.8.x, 3.9.x.


> https://www.python.org/downloads/


## Jupyter Notebook

Para o workspace da aplicação é necessária a instalação de Jupyter Notebook.
Para esse efeito através de linha de comandos com o módulo pip do Python
podemos correr o seguinte para a sua instalação:

> pip install notebook

Para verificar se a instalação foi bem sucedida podemos fazer:

> jupyter notebook

## Voilà

Para permitir o host da aplicação como web application necessitamos do
módulo Voilà que faz a transformação de Jupyter Notebook para web app.
Com isso, podemos proceder à instalação do módulo através da linha de
comandos com:

> pip install voila

Para verificar se a instalação foi bem sucedida podemos fazer:

> voila


## Ipywidgets

O módulo que vai permitir todos os widgets presentes na VoilApp de serem
representados pode ser instalado através da linha de comandos com:

> pip install ipywidgets

## Ipyvuetify

Este módulo é necessário na vertente do menu do editor VoilApp, pode ser
instalado através da linha de comandos com:

> pip install ipyvuetify

E para permitir a sua incorporação com Jupyter Notebook :

> jupyter nbextension enable –py –sys-prefix ipyvuetify

## Markdown

> pip install markdown

## NbFormat

Por fim, o módulo que permite a exportação da aplicação diretamente para
um novo ficheiro .ipynb (Jupyter Notebook) é instalado pela linha de comandos
através de:

> pip install nbformat

Com isto, todas as dependências estão agora instaladas. Nos casos onde
não é apresentada a versão do módulo a instalar é porque versões recentes
irão sempre funcionar, todas as versões que tenham sido lançadas no último
ano.


