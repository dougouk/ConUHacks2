import json
import requests

headers = {
    'nmaid': 'Nuance_ConUHack2017_20170119_210049',
    'nmaidkey': '0d11e9c5b897eefdc7e0aad840bf4316a44ea91f0d76a2b053be294ce95c7439dee8c3a6453cf7db31a12e08555b266d54c2300470e4140a4ea4c8ba285962fd',
}

text_data_test = {
    'user': 'http_sample',
    'text': 'hello world',
    'tts_type': 'text',
}

voice_data_test = {
    "sr_audio_file": "http://www.pacdv.com/sounds/voices/hello-4.wav",
    "sr_engine": "MREC"
}

def text_to_speech(text):
    text_data = {
        'user': 'http_sample',
        'text': text,
        'tts_type': "text",
    }

    tts_r = requests.post("https://nim-rd.nuance.mobi:9443/nina-webapi/TTS/", headers=headers, data=json.dumps(text_data))

    return tts_r.content

# ************* SPEECH TO TEXT

# speech_url must be mp4, wav, or aac
def speech_to_text(speech_url):
    voice_data = {
        "sr_audio_file": speech_url,
        "sr_engine": "NTE"
    }

    stt_r = requests.post('https://nim-rd.nuance.mobi:9443/nina-webapi/DoSpeechRecognition/', headers=headers, data=json.dumps(voice_data))

    return stt_r
# for item in r:
#     print(item)
#     continue

# ******* NLU ****

nlu_headers = {
    'nmaid': 'Nuance_ConUHack2017_20170119_210049',
    'nmaidkey': '0d11e9c5b897eefdc7e0aad840bf4316a44ea91f0d76a2b053be294ce95c7439dee8c3a6453cf7db31a12e08555b266d54c2300470e4140a4ea4c8ba285962fd',
}

def text_to_NLU(text):
    nlu_data = {
        "appName": "ConUHacks",
        "cloudModelVersion": "1.0.3",
        "companyName": "ConUDougOuk",
        "nlu_engine": "NLE",
        "text": text
    }

    nlu_r = requests.post("https://nim-rd.nuance.mobi:9443/nina-webapi/NinaDoNLU/", headers=nlu_headers, data=json.dumps(nlu_data))

    res = nlu_r.json()
    if 'QueryResult' in res and 'results' in res['QueryResult']:
        return res['QueryResult']['results'][0]
    else:
        return {'literal': 'I did not understand that'}
