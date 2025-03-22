import gradio as gr
from agent_setup import agent

def process_query(query):
    """Process the user query using the agent and return the response"""
    try:
        response = agent.run(query)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
demo = gr.Interface(
    fn=process_query,
    inputs=[
        gr.Textbox(
            label="Enter your query",
            placeholder="e.g., What's the difference between a list and a tuple in Python?",
            lines=3
        )
    ],
    outputs=[
        gr.Textbox(
            label="Agent Response",
            lines=10
        )
    ],
    title="AI Code Assistant",
    description="Ask questions about programming and get detailed answers from the AI agent.",
    theme=gr.themes.Soft(),
    examples=[
        ["What's the difference between a list and a tuple in Python?"],
        ["Explain how to use list comprehension in Python"],
        ["What are decorators in Python and how do they work?"]
    ]
)

if __name__ == "__main__":
    demo.launch(share=False)
