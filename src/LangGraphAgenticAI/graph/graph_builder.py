from langgraph.graph import StateGraph, START, END
from src.LangGraphAgenticAI.state.state import State
from src.LangGraphAgenticAI.nodes.basic_chatbot import BasicChatBotNode
from src.LangGraphAgenticAI.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.LangGraphAgenticAI.nodes.chatbot_with_tool_node import ChatbotWithToolNode


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
    
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilties, and sets up conditional and direct edges between nodes.
        The chatbot pode is set as the entry point.
        """
        ## Define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools=tools)

        ## Define the LLM
        llm = self.llm

        ## Define the chatbot Node
        obj_chatbot_with_tool_node = ChatbotWithToolNode(self.llm)
        chatbot_node = obj_chatbot_with_tool_node.create_chatbot(tools)

        ## Add nodes
        self.graph_builder.add_node("Chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        ## Add Edges
        self.graph_builder.add_edge(START, "Chatbot")
        self.graph_builder.add_conditional_edges("Chatbot", tools_condition) # Define tool conditions //
        self.graph_builder.add_edge("tools", "Chatbot")
        # self.graph_builder.add_edge("Chatbot", END)

        def ai_news_builder_graph(self):
            # added nodes
            self.graph_builder.add_node("fetch_news","")
            self.graph_builder.add_node("summarize_news","")
            self.graph_builder.add_node("save_results","")

            # added edges
            self.graph_builder.add_edge(START, "fetch_news")
            self.graph_builder.add_edge("fetch_news","summarize_news")
            self.graph_builder.add_edge("summarize_news", "save_results")
            self.graph_builder.add_edge("save_results", END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph fot the selected use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()