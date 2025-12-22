import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import origins
from services.ekilex import fetch_ekilex_word, fetch_ekilex_word_from_dataset

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ekilex/{word}")
async def get_ekilex_word(word: str):

    data = fetch_ekilex_word(word)
    if data is None:
        return {"message": "Word not found"}

    return data

@app.get("/ekilex/{word}/{dataset}")
async def get_ekilex_word_from_dataset(word: str, dataset: str):

    data = fetch_ekilex_word_from_dataset(dataset, word)
    if data is None:
        return {"message": "Word not found"}

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)