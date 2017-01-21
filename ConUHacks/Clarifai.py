from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

def getImageTags(url):
	output=app.tag_urls([url]
		,model='food-items-v1.0')['outputs'][0]['data']['concepts']
	list=[]
	for name in output:
		list.append(name['name'])
	return list