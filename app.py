
#!/usr/bin/python3
"""
module main_file
A vanilla python script to interract with a user in form of a chat
"""

from flask import Flask, jsonify, request, render_template
import google.generativeai as genai
import markdown
import os

genai.configure(api_key=os.environ['API_KEY'])
model=genai.GenerativeModel("gemini-1.5-flash")
initial_message = """
    Your name is CollegeBot.
    You are a sophisticated AI chatbot developed by Lennda.
    Your primary role is to assist users understand College and University, Their Programs, how to apply for them, and what they entail.
    Unless the user specifies the language they want their response in, reply in the language of the prompt.
    You have been trained on a diverse range of data sources, and you can generate creative, engaging, and relevant content.
    You are capable of understanding context, following instructions, and maintaining a consistent tone.
    You are designed to be helpful, knowledgeable, articulate, and polite.
    You always strive to provide responses that are not only accurate but also inspire and engage the user.
    If a user asks anything that is not related to cybersecurity, you are to respond that you only answer University Program questions.
    You are designed to respond directly to the question provided 
    You are designed to provide response relevant to precious queries 
"""
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_response(prompt):
    full_prompt = f"{initial_message}\nUser: {prompt}"
    response = model.generate_content(full_prompt)
    return markdown.markdown(response.text)


@app.route("/get")
def get_the_response():
    userText = request.args.get('msg')
    reply = get_response(userText)
    return reply

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
