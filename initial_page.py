import streamlit as str
import pandas as pd
import plotly.express as px
#configuração do site
str.set_page_config(layout="wide")
#importar as tabelas
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
#Filtro dos preços
price_max = df_top_100_books["book price"].max()
price_min = df_top_100_books["book price"].min()

filter_price = str.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top_100_books[df_top_100_books["book price"] <= filter_price]
#filtro de ano 
year_max = df_top_100_books["year of publication"].max()
year_min = df_top_100_books["year of publication"].min()
filter_year = str.sidebar.slider("Filter Year", year_min, year_max, year_max)
df_books = df_top_100_books[df_top_100_books["year of publication"] <= filter_year]
#tabela geral
df_books
#gráficos 
fig = px.bar(df_top_100_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])
#definir as colunas no site e alinhar os gráficos
col1, col2 = str.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)