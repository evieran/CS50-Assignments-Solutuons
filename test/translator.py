"""
This module provides translation functions for English and French.
"""

from flask import Flask, request, jsonify
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

@app.route('/translate/english_to_french', methods=['POST'])
def english_to_french():
    """
    Translate English text to French.

    Returns:
    str: Translated French text
    """
    text = request.json.get('text', '')
    try:
        translator = MyMemoryTranslator(source='english', target='french')
        return jsonify({'translation': translator.translate(text)})
    except Exception as err:
        print(f"An error occurred: {err}")
        return jsonify({'error': str(err)}), 500

@app.route('/translate/french_to_english', methods=['POST'])
def french_to_english():
    """
    Translate French text to English.

    Returns:
    str: Translated English text
    """
    text = request.json.get('text', '')
    try:
        translator = MyMemoryTranslator(source='french', target='english')
        return jsonify({'translation': translator.translate(text)})
    except Exception as err:
        print(f"An error occurred: {err}")
        return jsonify({'error': str(err)}), 500
    