from  langgraph_agentic_ai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot node implementation
    """

    def __init__(self, model):
        self.llm = model

    def proces(self, state:State) -> dict:
        """
        Process the input state and generates the response
        """
        return {"messages": self.llm.invoke(state["messages"])}