import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(text):
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation

def french_to_english(text):
    translator = MyMemoryTranslator(source='fr', target='en')
    translation = translator.translate(text)
    return translation