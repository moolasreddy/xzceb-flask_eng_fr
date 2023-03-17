import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishtofrench(word):
    """This class does from English to French translation"""

    url='https://api.us-east.assistant.watson.cloud.ibm.com/instances/605e1c2d-69b3-4744-98e8-d8a83b57cf9b'
    apikey='qmlTlJLjr7i8qH0qHYTn7B8yF3EF5iLqhjTpLri9TDn-'
    version=''
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version=version,authenticator=authenticator)
    language_translator.set_service_url(url)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    
    if word == " ":
        print("Please enter a word to translate.")
    else:
        pass

    return translation['translations'][0]['translation']

def frenchtoenglish(word):
    """This class does from French to English translation"""

    url='https://api.us-east.assistant.watson.cloud.ibm.com/instances/605e1c2d-69b3-4744-98e8-d8a83b57cf9b'
    apikey='qmlTlJLjr7i8qH0qHYTn7B8yF3EF5iLqhjTpLri9TDn-'
    version=''
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version=version,authenticator=authenticator)
    language_translator.set_service_url(url)
    lt = language_translator
    translation = lt.translate(text=word, model_id="fr-en").get_result()

    if word == " ":
        print("Please enter a word to translate.")
    else:
        pass

    return translation['translations'][0]['translation']
