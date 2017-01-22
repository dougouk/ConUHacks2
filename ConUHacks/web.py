import json

from flask import Flask, request
from .nina import text_to_speech, text_to_NLU
from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

def getImageTags(url):
	output=app.tag_urls([url]
		,model='food-items-v1.0')['outputs'][0]['data']['concepts']
	list=[]
	for name in output:
		list.append(name['name'])
	return list


app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    return text_to_speech(request.get_json()['text'])

@app.route('/nlu', methods=['POST'])
def nlu():
    ttnlu = text_to_NLU(request.form['text'])
    return json.dumps(ttnlu)

@app.route('/image', methods=['POST'])
def image():
	print(request.form['imgsrc'])
	return "hi"

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
