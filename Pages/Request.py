import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perlis Academic Library",
                   page_icon="🔍",
                   layout="wide")

st.title("Request Book")
book_request = pd.read_csv('books_request_sqit.csv')
st.dataframe(book_request)

st.sidebar.header("📕Request a book")
options_form = st.sidebar.form("options_form", clear_on_submit=True)
user_id = options_form.text_input("User_ID")
user_type = options_form.text_input("User_Type")
username = options_form.text_input("Name")
user_email = options_form.text_input("Email")
user_contact = options_form.text_input("Contact")
isbn13 = options_form.text_input("ISBN-13")
book_title = options_form.text_input("Title")
input_date = options_form.text_input("Date")
add_data = options_form.form_submit_button()

if add_data:
    new_data = {"User_ID":user_id, 
                "User_Type":user_type, 
                "Name":username, 
                "Email":user_email, 
                "Contact":user_contact, 
                "ISBN-13":isbn13, 
                "Title":book_title, 
                "Date":input_date}
    book_request = book_request.append(new_data, ignore_index = True)
    book_request.to_csv("books_request_sqit.csv", index=False)