#from .nina import get_tts
from flask import Flask, request
app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
#    return get_tts(request.get_json()['text'])
    pass

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
