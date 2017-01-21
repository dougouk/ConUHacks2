import json
import requests

headers = {
    'nmaid': 'Nuance_ConUHack2017_20170119_210049',
    'nmaidkey': '0d11e9c5b897eefdc7e0aad840bf4316a44ea91f0d76a2b053be294ce95c7439dee8c3a6453cf7db31a12e08555b266d54c2300470e4140a4ea4c8ba285962fd',
}

data = {
    'user': 'http_sample',
    'text': 'hello world',
    'tts_type': 'text',
}

voice_data = {
    "sr_audio_file": "http://www.pacdv.com/sounds/voices/hello-4.wav",
    "sr_engine": "MREC"
}

r = requests.post('https://nim-rd.nuance.mobi:9443/nina-webapi/DoSpeechRecognition/', headers=headers, data=json.dumps(voice_data))

# for item in r:
#     print(item)
#     continue

# ******* NLU ****

nlu_headers = {
    'nmaid': 'Nuance_ConUHack2017_20170119_210049',
    'nmaidkey': '0d11e9c5b897eefdc7e0aad840bf4316a44ea91f0d76a2b053be294ce95c7439dee8c3a6453cf7db31a12e08555b266d54c2300470e4140a4ea4c8ba285962fd',
}

nlu_data = {
    "appName": "ConUHacks",
    "cloudModelVersion": "1.0.3",
    "companyName": "ConUDougOuk",
    "nlu_engine": "NLE",
    "text": "I want to choose this one"
}

nlu_r = requests.post("https://nim-rd.nuance.mobi:9443/nina-webapi/NinaDoNLU/", headers=nlu_headers, data=json.dumps(nlu_data))
