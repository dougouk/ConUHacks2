import json

from flask import Flask, request

from .nina import text_to_NLU

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
#    return get_tts(request.get_json()['text'])
    pass

@app.route('/nlu', methods=['POST'])
def nlu():
    ttnlu = text_to_NLU(request.form['text'])
    return json.dumps(ttnlu)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
