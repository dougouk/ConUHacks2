import json
import http.client

conn = http.client.HTTPConnection("hackaton.ypcloud.io")

#arg: food: str, type of food, location: str, location in form 45.4754418,-73.5863705
#return: dict of business
def get_rest(food, location):
    diction = { "search":[{
   "searchType":"PROXIMITY",
   "collection":"MERCHANT",
   "what": food,
   "where":{
   "type":"GEO",
   "value":location }
   }]}
    payload = json.dumps(diction)
    #payload = "  { \"search\":[{\r\n   \"searchType\":\"PROXIMITY\",\r\n   \"collection\":\"MERCHANT\",\r\n   \"what\": \"burger\",\r\n   \"where\":{\r\n   \"type\":\"GEO\",\r\n   \"value\":\"45.4754418,-73.5863705\" }\r\n   }]}"

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "93188d7e-c08e-6030-30d8-71c5de344938"
        }

    conn.request("POST", "/search", payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)

    for x in json_obj['searchResult'][0]["merchants"]:
        print(x['businessName'])
        print(x['address']['displayLine'])

    return json_obj['searchResult'][0]["merchants"]

def match_menu(restaurants, food):
    food_items = []
    diction = {"pager":{"total":0,"count":5,"total_on_page":0,"total_pages":0,"page":1},"filters":{"lang":"en","show":"deal","merchant_yp_id":"100448116"},"timingInfo":{"sphinx_time":"0.006","total_action_time":"0.05"},"data":[]}
