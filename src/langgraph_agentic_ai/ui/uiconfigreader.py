from configparser import ConfigParser

class ConfigReader:
    # Agentic-Chatbot\src\langgraph_agentic_ai\ui\uiconfig.ini
    def __init__(self, config_file='C:\\ArunSourceCode\\Python\\AgenticChatbot_KrishN\\Agentic-Chatbot\\src\\langgraph_agentic_ai\\ui\\uiconfig.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.get_list('DEFAULT', 'LLM_OPTIONS', fallback='Groq')
    
    def get_usecase_options(self): 
         return self.get_list('DEFAULT', 'USECASE_OPTIONS', fallback='Basic Chatbot')
    
    def get_groq_model_options(self):
        return self.get_list('DEFAULT', 'GROQ_MODEL_OPTIONS', fallback='qwen/qwen3-32b')
    
    def get_page_title(self):
        return self.get('DEFAULT', 'PAGE_TITLE', fallback='Chatbot')

    def get(self, section, option, fallback=None):
        value = self.config.get(section, option, fallback=fallback)
        print(value)
        return value

    def get_list(self, section, option, fallback=None):
        value = self.get(section, option, fallback)
        if value:
            return [item.strip() for item in value.split(',')]
        return []