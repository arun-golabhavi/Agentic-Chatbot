from langgraph.graph import StateGraph, START, END
from langgraph_agentic_ai.state.state import State
from langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model) :
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Basic chat bot using lang graph
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.proces)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot",END)
     
    
    def setup_graph(self,usecase:str):
        """
        Selects the chat bot type based on the use case
        """
        if usecase == "Basic Chatbot":
           self.basic_chatbot_build_graph()
        
        return self.graph_builder.compile()
