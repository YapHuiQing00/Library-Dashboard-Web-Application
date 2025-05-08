import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import pandasql as ps

data_currentbooks = pd.read_csv('books_sqit_test.csv')


st.sidebar.header("📁Search a book")
find_book = st.sidebar.form("find_book", clear_on_submit=True)
my_book = find_book.text_input("Find your book: ")
if my_book:
	try:
		sql_query = "SELECT * FROM data_currentbooks WHERE [Title] == &my_book& "
		st.subheader('Your book is avalaible in the library.')
	except:
		st.error('No book with that title.')

find_button = find_book.form_submit_button()

st.sidebar.header("Please Filter Here:")
genre = st.sidebar.multiselect(
    "Select your genre:",
    options=data_currentbooks["Genre"].unique(),
    default=data_currentbooks["Genre"].unique())

publisher = st.sidebar.multiselect(
    "Select your publisher:",
    options=data_currentbooks["Publisher"].unique(),
    default=data_currentbooks["Publisher"].unique())

language = st.sidebar.multiselect(
    "Select your language:",
    options=data_currentbooks["Language"].unique(),
    default=data_currentbooks["Language"].unique())

data_currentbooks_selection = data_currentbooks.query(
    "Genre == @genre & Publisher == @publisher & Language == @language")
st.dataframe(data_currentbooks_selection)

data_desc = data_currentbooks.sort_values(by='Borrowed', ascending=False)
data_top5 = data_desc.head(n=5).to_string(index=False)
st.subheader(f"Top 5 of Borrowed")
st.text(data_top5)
