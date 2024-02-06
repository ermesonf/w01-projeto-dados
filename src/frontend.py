import streamlit as st

class ExcelValidatorUI:
    def __init__(self) -> None:
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de excel"
        )

    def display_header(self):
        st.title("Validador de excel")
        
    def upload_file(self):
        return st.file_uploader("Carrege seu arquivo excel aqui", type=["xlsx"])