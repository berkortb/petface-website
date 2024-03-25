import requests
from utils.params import mood_explanations


def predict_emotion(image_bytes):
    api_url = "https://petface-chgqr6jdlq-ew.a.run.app/predict/"
    files = {"img_file": image_bytes}
    print("reached with file")
    response = requests.post(api_url, files=files)
    response_json = response.json()
    print(response.status_code)
    print(response.json())
    mood = response_json.get("prediction").capitalize()
    description = mood_explanations.get(mood, {}).get("description")
    fact = mood_explanations.get(mood, {}).get("fact")

    return mood, description, fact
