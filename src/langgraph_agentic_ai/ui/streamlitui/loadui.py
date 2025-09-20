import streamlit as st
import os
from ..uiconfigreader import ConfigReader

class LoadStreamlitUI:
    def __init__(self):
        self.config_reader = ConfigReader()
        self.user_controls={}
        self.page_title = str(self.config_reader.get_page_title())
        self.llm_options = self.config_reader.get_llm_options()
        self.usecase_options = self.config_reader.get_usecase_options()
        self.groq_model_options = self.config_reader.get_groq_model_options()
        self.setup_page()

    def setup_page(self):
        st.set_page_config(page_title= "🤖 "+ self.page_title, layout="wide")
        st.title("🤖 "+ self.page_title)

    def display_sidebar(self):
        st.sidebar.title("Configuration")
        selected_llm = st.sidebar.selectbox("Select LLM", self.llm_options)
        selected_usecase = st.sidebar.selectbox("Select Use Case", self.usecase_options)
        self.user_controls["selected_llm"]=selected_llm
        self.user_controls["selected_usecase"]=selected_usecase
        if selected_llm == "Groq":
            selected_groq_model = st.sidebar.selectbox("Select Groq Model", self.groq_model_options)
            self.user_controls["selected_groq_model"]=selected_groq_model
            self.user_controls["groq_api_key"] = st.session_state["GROQ_API_KEY"] = st.sidebar.text_input("API Key", type="password")
            if not self.user_controls["groq_api_key"]:
                st.sidebar.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
        return  self.user_controls          
