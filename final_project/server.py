from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    """    Add the values in ``textToTranslate``"""
    textToTranslate.assertEqual(textToTranslate("Hello"),"Bonjour")     
    textToTranslate.assertEqual(textToTranslate("Welcome"),"Bienvenue")
    textToTranslate.assertEqual(textToTranslate("Fin"),"End")
    textToTranslate.assertNotEqual(textToTranslate("None"), '')
    textToTranslate.assertNotEqual(textToTranslate(0), 0)
    #textToTranslate.assertEqual(englishToFrench(""),"erreur")

    return textToTranslate
    #return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    """    Add the values in ``textToTranslate``"""    
    textToTranslate.assertEqual(textToTranslate("Bonjour"),"Hello")     
    textToTranslate.assertEqual(textToTranslate("Bienvenue"),"Welcome")
    textToTranslate.assertEqual(textToTranslate("End"),"Fin")
    textToTranslate.assertNotEqual(textToTranslate("None"), '')
    textToTranslate.assertNotEqual(textToTranslate(0), 0)
    #textToTranslate.assertEqual(frenchToEnglish(""),"erreur")    
    return textToTranslate
    #return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html') #"Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
