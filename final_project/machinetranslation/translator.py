#translator.py
#import json
"""Python version of Module providingFunction."""
import os # [missing-module-docstring]
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishtofrench(englishtext):
     #write the code here
    """This class does from English to French translation"""

    version='2018-05-01'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
                            version=version,
                            authenticator=authenticator)
    language_translator.set_service_url(url)
    translation = language_translator.translate(text=englishtext, model_id="en-fr"
                            ).get_result()
    if englishtext == " ":
        print("Please enter an englishtext to translate.")
    else:
        pass

    return translation.get['translations'][0].get['translation']

def frenchtoenglish(frenchtext):
    #write the code here
    """This class does from French to English translation"""

    version='2018-05-01'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
                            version=version,
                            authenticator=authenticator)
    language_translator.set_service_url(url)

    translation = language_translator.translate(text=frenchtext, model_id="fr-en"
                            ).get_result()
    if frenchtext == " ":
        print("Please enter a frenchtext to translate.")
    else:
        pass

    return translation.get['translations'][0].get['translation']
