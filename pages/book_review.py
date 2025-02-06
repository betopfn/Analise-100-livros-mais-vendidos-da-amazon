import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
#importar as tabelas
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
#separar os nomes dos livros sem repetições
books = df_top_100_books["book title"].unique()
#coloca-los dentro de uma sidebar
book = st.sidebar.selectbox("Books", books)
#aparecer o livro escolhido pela sidebar na tela    
df_books = df_top_100_books[df_top_100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]



book_title = df_books["book title"].iloc[0]
book_genre = df_books["genre"].iloc[0]
book_price = f"${df_books['book price'].iloc[0]}"
book_rating = df_books["rating"].iloc[0] 
book_year = df_books["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year )

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")   
    message.write(row[5])                             
                          
                             
                             
                    