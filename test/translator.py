"""
This module provides translation functions for English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(text):
    try:
        translator = MyMemoryTranslator(source='english', target='french')
        return translator.translate(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def french_to_english(text):
    try:
        translator = MyMemoryTranslator(source='french', target='english')
        return translator.translate(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
