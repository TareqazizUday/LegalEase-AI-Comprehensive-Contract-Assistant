import openai

class CallAIAgent:
    def __init__(self, api_key):
        """Initialize with user-provided OpenAI API key."""
        openai.api_key = api_key  # Use the dynamically provided API key

    def analyze_contract(self, contract_text):
        """Analyzes a contract using the OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a legal assistant. Analyze the contract and provide a summary of key points, risks, and obligations."},
                    {"role": "user", "content": f"Analyze the following contract:\n\n{contract_text}"}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"

    def generate_contract(self, requirements):
        """Generates a contract based on user input."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a legal assistant. Generate a contract based on the user's requirements."},
                    {"role": "user", "content": f"Generate a legal contract based on the following requirements:\n\n{requirements}"}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"

    def suggest_improvements(self, contract_text):
        """Suggests improvements for a contract."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a legal assistant. Suggest improvements for the following contract."},
                    {"role": "user", "content": f"Suggest improvements for the following contract:\n\n{contract_text}"}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"

    def answer_legal_query(self, question):
        """Answers general legal queries."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a legal assistant. Answer the user's legal question."},
                    {"role": "user", "content": f"Answer the following legal question:\n\n{question}"}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"
