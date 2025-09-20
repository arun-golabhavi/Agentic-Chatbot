import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("groq_api_key")
            os.environ["GROQ_API_KEY"]= groq_api_key

            selected_groq_model = self.user_controls_input.get("selected_groq_model")
            if(groq_api_key == '' and os.environ["GROQ_API_KEY"]==''):
                st.error("Please Enter the Groq API key")
            
            print(f"---------------------{selected_groq_model}--------------------")
            llm = ChatGroq(model=selected_groq_model)
            print("---------------------Selected llm--------------------")
        except Exception as e:
            raise ValueError(f"Error Occured With Exception::{e}")
        return llm