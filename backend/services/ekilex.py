import json
import requests

from core.config import API_KEY_EKILEX # API-key Ekilex

# Fetch word data from Ekilex
def fetch_ekilex_word(word):
    try:
        # Sent request to Ekilex API for word searching
        response = requests.get(
            f'https://ekilex.ee/api/word/search/{word}',
            headers={
                'ekilex-api-key': API_KEY_EKILEX
            }
        )

        # Check requset status
        if response.status_code != 200:
            raise Exception(f"Request error: {response.status_code} {response.reason}")

        # Parse JSON response
        data = response.json()
    
        # Check if there are results
        if not data:
            print('Word not found')
            return

        results = data.get('words', [])

        filtered_words = []
        for words in results:
                filtered_words.append({
                    'wordId': words.get('wordId'),
                    'wordValue': words.get('wordValue'),
                    'datasetCodes': words.get('datasetCodes', []),
                })

        # Return filtered word data
        return filtered_words
    
    except Exception as e:
        print('Error:', str(e))


# Fetch word data from specific dataset
def fetch_ekilex_word_from_dataset(dataset, word):
    try:
        response = requests.get(
            f'https://ekilex.ee/api/meaning/search/{word}/{dataset}',
            headers={
                'ekilex-api-key': API_KEY_EKILEX
            }
        )

        if response.status_code != 200:
            raise Exception(f"Request error: {response.status_code} {response.reason}")

        data = response.json()
        results = data.get('results', [])

        filtered_words = []

        for meaning in results:
            for w in meaning.get('meaningWords', []):
                filtered_words.append({
                    'wordId': w.get('wordId'),
                    'wordValue': w.get('wordValue'),
                    'lang': w.get('lang'),
                    'datasetCodes': w.get('datasetCodes', []),
                })

        return filtered_words

    except Exception as e:
        print(f'Error with {dataset}:', str(e))
        return []
