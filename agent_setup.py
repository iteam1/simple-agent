import pytz
import yaml
import datetime
from tools.final_answer import FinalAnswerTool
from tools.visit_webpage import VisitWebpageTool
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, load_tool, tool

# Input
model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"

# Define tools by decorator
@tool
def dummy_tool(query:str)->str:
    """A dummy tool that does nothing
    
    Args:
        query (str): The input query to process
        
    Returns:
        str: The processed dummy output
    """
    return f"Dummy tool output: {query}"

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"

# Import a text-to-image generation tool from the Hugging Face Hub
#image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

# Create tool instances
final_answer_tool = FinalAnswerTool()
visit_webpage_tool = VisitWebpageTool()

# Use a Hugging Face Endpoint
model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id=model_id,
custom_role_conversions=None,
)

# Load prompt templates from a YAML file
with open('prompts.yaml', 'r') as f:
    prompt_templates = yaml.safe_load(f)

# Initialize a CodeAgent instance, which will use the model and tools
agent = CodeAgent(model=model,
                tools=[DuckDuckGoSearchTool(),
                       dummy_tool,
                       get_current_time_in_timezone,
                       final_answer_tool,
                       visit_webpage_tool

                ],
                max_steps=6,
                verbosity_level=1,
                grammar=None,
                planning_interval=None,
                name=None,
                description=None,
                prompt_templates=prompt_templates
                )

# Run the agent with a sample query
#response = agent.run("What's the difference between a list and a tuple in Python?")
#print(response)