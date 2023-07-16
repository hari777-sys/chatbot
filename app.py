from flask import Flask, render_template, request
from bot import get_chatbot_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat_prompt():
    result = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        result = get_chatbot_response(prompt)
        #chat_history.append((prompt, result))
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
