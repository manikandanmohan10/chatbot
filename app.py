# from flask import Flask, request, render_template 
# from main import chat
# from audio_to_text import get_text

# app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return render_template('home.html')


# # @app.route('/get_input')
# # def get_input():
# #     inp = request.values.get('inp', 'hello')
    
# #     response = chat(inp)
    
    
# #     return render_template('home.html', inp=response)

# @app.route('/')
# def home():
    
#     a = get_text()
#     return a


# @app.route('/get_input')
# def get_input():
#     inp = request.values.get('inp', 'hello')
    
#     response = chat(inp)
    
    
#     return render_template('home.html', inp=response)

from openai import api_key, Client
# from openai.openai_response import  
from flask import Flask, request
import os

app = Flask(__name__)

# Set the API key
api_key(os.getenv('API_KEY'))

# Create a client for the GPT-3 API
client = Client()

@app.route('/')
def generate_text():
  # Get the user's input text
  input_text = request.args.get('input', 'Hello')
  
  # Use the GPT-3 API to generate text based on the input
  response = client.completions(
    engine="text-davinci-002",
    prompt=input_text,
    max_tokens=1024,
    temperature=0.5
  )
  
  # Return the generated text to the user
  return response["choices"][0]["text"]
