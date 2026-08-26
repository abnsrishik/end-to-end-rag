from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages
from typing import Annotated

class State(BaseModel):
    """Represent the structure of the state used in the graph"""
    messages: Annotated[list, add_messages]

