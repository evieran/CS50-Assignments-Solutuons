"""
This module provides translation functions for English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(text):
    """
    Translate English text to French.

    Parameters:
    text (str): English text to translate

    Returns:
    str: Translated French text
    """
    try:
        translator = MyMemoryTranslator(source='english', target='french')
        return translator.translate(text)
    except Exception as e:
        print(f"An error occurred: {err}")
        return None

def french_to_english(text):
    """
    Translate French text to English.

    Parameters:
    text (str): French text to translate

    Returns:
    str: Translated English text
    """
    try:
        translator = MyMemoryTranslator(source='french', target='english')
        return translator.translate(text)
    except Exception as e:
        print(f"An error occurred: {err}")
        return None
