import pytz
import yaml
import datetime
import requests
#from UI import GradioUI
from tools.final_answer import *
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, load_tool, tool

# Input
model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"

# Define tools
@tool
def dummy_tool(query:str)->str:
    """A dummy tool that does nothing"""
    return f"Dummy tool output: {query}"


# Import a text-to-image generation tool from the Hugging Face Hub
#image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

# Create tool instances

# Use a Hugging Face Endpoint
model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id=model_id,
custom_role_conversions=None,
)

# Load prompt templates from a YAML file

# Initialize a CodeAgent instance, which will use the model and tools
agent = CodeAgent(model=model,
                tools=[DuckDuckGoSearchTool(),
                       dummy_tool,
                ],
                max_steps=6,
                verbosity_level=1,
                grammar=None,
                planning_interval=None,
                name=None,
                description=None,
                prompt_templates=None
                )

# Run the agent with a sample query
#response = agent.run("What's the difference between a list and a tuple in Python?")
#print(response)