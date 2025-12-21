import requests
import json
from fastapi import FastAPI

from core.config import API_KEY_EKILEX # API-key Ekilex


def ekilex_word_fetch(word):
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
    
    except Exception as e:
        print('Error:', str(e))
