import json
import http.client

from flask import Flask, request
from .nina import text_to_speech, text_to_NLU
from clarifai.rest import ClarifaiApp

appp = ClarifaiApp()

def getImageTags(url):
	output=appp.tag_files([url]
		,model='food-items-v1.0')['outputs'][0]['data']['concepts']
	list=[]
	for name in output:
		list.append(name['name'])

	conn = http.client.HTTPConnection("hackaton.ypcloud.io")

	diction = { "search":[{
	"searchType":"PROXIMITY",
	"collection":"MERCHANT",
	"what": food,
	"where":{
	"type":"GEO",
	"value":'45.4754418,-73.5863705' }
	}]}
	payload = json.dumps(diction)
	#payload = "  { \"search\":[{\r\n\"searchType\":\"PROXIMITY\",\r\n\"collection\":\"MERCHANT\",\r\n\"what\": \"burger\",\r\n\"where\":{\r\n\"type\":\"GEO\",\r\n\"value\":\"45.4754418,-73.5863705\" }\r\n}]}"

	headers = {
		'content-type': "application/json",
		'cache-control': "no-cache",
		'postman-token': "93188d7e-c08e-6030-30d8-71c5de344938"
		}

	conn.request("POST", "/search", payload, headers)

	res = conn.getresponse()
	data = res.read().decode("utf-8")
	json_obj = json.loads(data)

	return json_obj['searchResult'][0]["merchants"]


app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    return text_to_speech(request.get_json()['text'])

@app.route('/nlu_next_text', methods=['POST'])
def nlu():
    return json.dumps({'intent':'NEXT_IMAGE'})

@app.route('/nlu_this_test', methods=['POST'])
def nlu():
    return json.dumps({'intent':'THIS_IMAGE'})

@app.route('/nlu', methods=['POST'])
def nlu():
    ttnlu = text_to_NLU(request.form['text'])
    return json.dumps(ttnlu)

@app.route('/image', methods=['POST'])
def image():
	output=getImageTags(request.form['imgsrc'])
	print(output)
	return "hi"

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
