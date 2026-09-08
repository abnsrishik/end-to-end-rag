from src.LangGraphAgenticAI.state.state import State
from langchain_core.messages import SystemMessage

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """
    def __init__(self,model):
        self.llm = model
    
    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role" : "user", "content": user_input}])

        # simulate tool-specific logic
        tools_response = f"TOol integration for: {user_input}"

        return {"messages" : [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)
        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            messages = [
                SystemMessage(
                    content=(
                        """
                        Use tavily_search only for web searches. 
                        Always call it with exactly one argument: 
                        query, containing the user's search question.
                        """
                    )
                ),
                *state["messages"],
            ]
            return {"messages": [llm_with_tools.invoke(messages)]}
        
        return chatbot_node

