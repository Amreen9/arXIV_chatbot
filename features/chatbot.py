import os
import google.generativeai as genai
from flask import jsonify

api_key = os.getenv("api_key")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def chat_bot(prompt):
    try:
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        print(f"Chatbot Terminal:\nUser: {prompt}")
        
        file_path = r"C:\Users\baenu\source\repos\NIC7\full_text.txt"
        file_content = read_file_content(file_path)
        if file_content is None:
            return jsonify({"response": "Unable to read the file content."}), 500

        hidden_prompt = f"Analyze this text: {file_content}\n Answer user's questions based on this. If the text does not define an answer for user's question, generate an answer to user's question by yourself."
        combined_prompt = f"{hidden_prompt}\n\nUser's question: {prompt}.Answer short and concise."

        response = chat.send_message(combined_prompt, stream=True)
        
        if not response:
            return jsonify({"response": "Chatbot is temporarily unavailable. Please try again"}), 500

        response_text = ""
        for chunk in response:
            if hasattr(chunk, 'text'):
                response_text += chunk.text

        formatted_response = response_text.replace('*','<strong>').replace('**', '<strong>').replace('\n', '<br>')
        
        print("Bot response fetched\n")
        
        return jsonify({"response": formatted_response}), 200
    except Exception as e:
        return jsonify({"response": "An error occurred while processing your request."}), 500