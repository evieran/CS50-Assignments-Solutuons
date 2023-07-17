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
    
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation

def french_to_english(text):
    """
    Translate French text to English.

    Parameters:
    text (str): French text to translate

    Returns:
    str: Translated English text
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    translation = translator.translate(text)
    return translation
