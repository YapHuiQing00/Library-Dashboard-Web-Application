import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Perlis Academic Library",
                   page_icon="🏠",
                   layout="wide")

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    <style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

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

            data_currentbooks = pd.read_csv(r"C:\Users\Yap Hui Qing\Documents\Data Learning\Data Engineering\SQIT Library web app project\books_sqit_test.csv")
            data_index = data_currentbooks.set_index('ISBN-13')
            data_title = pd.read_csv(r"C:\Users\Yap Hui Qing\Documents\Data Learning\Data Engineering\SQIT Library web app project\books_sqit_test.csv", usecols=['Title'])
            genre_n = data_currentbooks['Genre'].value_counts().rename_axis('Genre').reset_index(name='Amount')
            price = data_currentbooks[["Price($)"]]
            isbn = data_currentbooks[["ISBN-13"]]

            st.title("🏠 Library Dashboard")
            st.markdown("##")

            number_of_books = len(data_currentbooks)
            st.subheader("Total number of books")
            st.subheader(f"{number_of_books}")

            st.markdown("---")

            fig_book_price = px.bar(
                price,
                y="Price($)",
                x=price.index,
                #orientation="h",
                title="<b>Price of books</b>",
                color_discrete_sequence=["#0083B8"]*len(price),
                template="plotly_white",
            )
            st.plotly_chart(fig_book_price)

            st.markdown("---")

            roi = data_currentbooks[["ROI"]]
            fig_roi = px.scatter(
                roi,
                y="ROI",
                x=price.index,
                #orientation="h",
                title="<b>ROI of the book</b>",
                color_discrete_sequence=["#0083B8"]*len(roi),
                template="plotly_white",
            )
            st.plotly_chart(fig_roi)

            st.markdown("---")

            your_labels = genre_n.Genre
            your_values = genre_n.Amount

            fig_genre_n = px.pie(
                values=your_values,
                names=your_labels,
                title='Genre of books'
            )
            st.plotly_chart(fig_genre_n)

            st.markdown("---")

            language_n = data_currentbooks['Language'].value_counts().rename_axis('Language').reset_index(name='Amount')
            your_labels = language_n.Language
            your_values = language_n.Amount

            fig_language_n = px.pie(
                values=your_values,
                names=your_labels,
                title='Language of books'
            )
            st.plotly_chart(fig_language_n)

            st.markdown("---")

            data_desc = data_currentbooks.sort_values(by='Borrowed', ascending=False)
            data_top5 = data_desc.head(n=5).to_string(index=False)
            st.subheader(f"Top 5 of Borrowed")
            st.text(data_top5)

            st.markdown("---")

            st.subheader("Maps of the book")
            data = [[38, 97], [35, 103], [6, 100]]
            df = pd.DataFrame(data, columns=['lat', 'lon'])

            st.map(df)