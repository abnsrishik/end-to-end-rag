from langgraph.graph import StateGraph, START, END
from src.LangGraphAgenticAI.state.state import State
from src.LangGraphAgenticAI.nodes.basic_chatbot import BasicChatBotNode



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot grah using LangGraph.
        This method initializes a chatbot node using the 'BasicChatBotNode' class 
        and integrates it into the graph. THe chatbot node is set as both the
        entry adn exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process) # comes from nodes directory
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def setup_graph(self, usecase: str):
        """
        Sets up the graph fot the selected use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            return self.graph_builder.compile()