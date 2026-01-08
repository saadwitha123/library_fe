import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"   

st.set_page_config(page_title="Library Management", layout="wide")
st.header("📚 Library Management System")

tabs = st.tabs([
    "Books",
    "Users",
    "Add Book",
    "Delete Book"
])


with tabs[0]:
    st.subheader("Search Book by ID")

    book_id = st.text_input("Enter Book ID")

    if st.button("Get Book"):
        res = requests.get(f"{BASE_URL}/book_id/{book_id}")
        if res.status_code == 200:
            st.data_editor(res.json(), width=True)
        else:
            st.error("Book not found")


with tabs[1]:
    st.subheader("All Users")

    res = requests.get(f"{BASE_URL}/users")
    if res.status_code == 200:
        st.data_editor(res.json(), width=True)
    else:
        st.error("Failed to load users")


with tabs[2]:
    st.subheader("Add New Book")

    with st.form("add_book_form"):
        book_id = st.text_input("Book ID")
        book_name = st.text_input("Book Name")
        author_name = st.text_input("Author Name")
        

        submit = st.form_submit_button("Add Book")

        if submit:
            payload = {
                "book_id": book_id,
                "book_name": book_name,
                "author_name": author_name
            }

            res = requests.post(f"{BASE_URL}/add/books", json=payload)

            if res.status_code == 200:
                st.success("Book added successfully")
            else:
                st.error(res.text)


with tabs[3]:
    st.subheader("Delete Book by ID")

    delete_book_id = st.text_input("Book ID to Delete")

    if st.button("Delete Book", type="primary"):
        res = requests.delete(f"{BASE_URL}/book/{delete_book_id}")
        if res.status_code == 200:
            st.success("Book deleted successfully")
        else:
            st.error("Failed to delete book")
