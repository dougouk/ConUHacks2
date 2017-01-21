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

r = requests.post('https://nim-rd.nuance.mobi:9443/nina-webapi/TTS/', headers=headers, data=json.dumps(data))
