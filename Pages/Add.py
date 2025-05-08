import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perlis Academic Library",
                   page_icon="📋",
                   layout="wide")

registered_username = ["Anne", "Benny", "Colin", "Dylan", "Edward"]
registered_password = ["101010", "202020", "303030", "404040", "505050"]

st.sidebar.header("Login")
login_sidebar = st.sidebar.form("fLogin", clear_on_submit=True)
in_username = login_sidebar.text_input("Username: ")
in_password = login_sidebar.text_input("Password: ")

find_button = login_sidebar.form_submit_button()

for i in range(len(registered_username)):
    if registered_username[i] == in_username:
        correct_password = registered_password[i]
        if in_password == correct_password:
            test = True
            st.title("Add Book")
            book_request = pd.read_csv('books_sqit_test.csv')
            st.dataframe(book_request)

            st.sidebar.header("📋 Add a book")
            options_form = st.sidebar.form("options_form", clear_on_submit=True)
            isbn13 = options_form.text_input("ISBN-13")
            book_title = options_form.text_input("Title")
            book_author = options_form.text_input("Author")
            book_genre = options_form.text_input("Genre")
            book_amount = options_form.text_input("Amount")
            book_publisher = options_form.text_input("Publisher")
            book_year = options_form.text_input("Year")
            book_language = options_form.text_input("Language")
            book_price = options_form.text_input("Price($)")
            amount_borrowed = options_form.text_input("Borrowed")
            book_roi = options_form.text_input("ROI")
            add_data = options_form.form_submit_button()

            if add_data:
                new_data = {"ISBN-13":isbn13, 
                            "Title":book_title, 
                            "Author":book_author,
                            "Genre":book_genre,
                            "Amount":book_amount,
                            "Publisher":book_publisher,
                            "Year":book_year,
                            "Language":book_language,
                            "Price($)":book_price,
                            "Language":book_language,
                            "ROI":book_roi,}
                book_request = book_request.append(new_data, ignore_index = True)
                book_request.to_csv("books_sqit_test.csv", index=False)