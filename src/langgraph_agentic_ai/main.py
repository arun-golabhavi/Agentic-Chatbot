import streamlit as st

from .ui.streamlitui.loadui import LoadStreamlitUI
from langgraph_agentic_ai.LLMs.groqllm import GroqLLM
from langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from langgraph_agentic_ai.ui.streamlitui.display_results import DisplayResultsStreamlit

def load_langgraph_agenticai_app():
    """
     Loads and runs the Langgraph AgenticAI application with Streamlit UI.
     This function initializes the UI, handles user input, configures the LLM model,
     sets up the graph based on the selected use case and displays the output
    """
    ## load ui
    ui = LoadStreamlitUI()
    user_input = ui.display_sidebar()

    if not user_input:
        st.error("Error: Failed to load user input from UI.")
        return
    user_message = st.chat_input("Enter your message")
    print(f'user_message:{user_message}')
    if (user_message):
        try:
            ## Configure the llm
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
           
            if not model:
                st.error("Error: LLM model can not be initialized")
                return
            
            # initialize the graph
            usecase = str(user_input.get("selected_usecase"))
            if not usecase:
                st.error("Error: No use case selected")
            print(f"------------UseCase:{usecase}---------")
            # Graph builder
            graph_builder = GraphBuilder(model)
            try:
                 graph = graph_builder.setup_graph(usecase)
                 print(f"------------graph:{graph.nodes}---------")
                 DisplayResultsStreamlit(usecase=usecase,graph=graph,user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph Set Up failed: {e}")
                return

        except Exception as e:
            raise ValueError(f"Error in calling LLM:{e}")