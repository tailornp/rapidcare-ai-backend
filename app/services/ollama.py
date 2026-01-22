import ollama

def get_llm_response(prompt: str) -> str:
    """
    Get a response from the Ollama LLM model.
    This function sends a prompt to the Ollama chat API using the llama3.2:1b model
    and returns the generated response content.
    Args:
        prompt (str): The input prompt/question to send to the language model.
    Returns:
        str: The generated response content from the language model.
    Raises:
        Exception: If the Ollama API call fails or returns an unexpected response format.
    """
    
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

