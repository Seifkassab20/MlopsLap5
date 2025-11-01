import gradio as gr
import subprocess
import json

MODEL_NAME = "llama3.1:8b"  # change to your model name

def query_ollama(prompt):
    """
    Sends a prompt to the local Ollama model and returns the generated response.
    """
    try:
        # Run Ollama command and get output
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# Create Gradio interface
iface = gr.Interface(
    fn=query_ollama,
    inputs=gr.Textbox(label="Ask me anything!", lines=4, placeholder="Enter your question or code prompt..."),
    outputs=gr.Textbox(label="Assistant Response", lines=10),
    title="💻 Local AI Assistant",
    description=f"This assistant runs locally using the `{MODEL_NAME}` model through Ollama."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
