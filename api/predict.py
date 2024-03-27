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
    primary_mood = response_json["prediction"][0].capitalize()
    #mood = response_json.get("prediction").capitalize()
    try:
        secondary_mood = response_json["prediction"][1]
    except IndexError:
        secondary_mood = None
    classification = response_json.get("classification")
    description = mood_explanations.get(primary_mood, {}).get("description")
    fact = mood_explanations.get(primary_mood, {}).get("fact")

    return primary_mood, secondary_mood, classification, description, fact
