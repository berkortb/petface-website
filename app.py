import streamlit as st
from PIL import Image

from utils.params import animals
from api.predict import predict_emotion

st.set_page_config(
    page_title="Pet Face Expression Recognition",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded",
)


# App title and description
st.header("🐾Pet Face Expression Recognition 🐾")
st.markdown(
    """
            > Welcome to the Pet Face Expression Recognition tool!
            > Upload a photo of your pet, and let's try to understand their mood.

            > **What you have to do:**

            > * Upload a photo of your pet.
            > * We will guess the mood of your pet!
            > * Try other animals. Even a chicken can show happiness 🐣
            """
)


def display_animal_row(animals_row):
    cols_img = st.columns(7)
    cols_desc = st.columns(7)

    for i, animal in enumerate(animals_row):

        with cols_img[i]:
            st.image(animal["image"], width=100)

        with cols_desc[i]:
            st.write(animal["description"])


animals_chunks = [animals[x : x + 7] for x in range(0, len(animals), 7)]

for chunk in animals_chunks:
    display_animal_row(chunk)


# def process_image(image_bytes):
#     api_url = "https://petface-chgqr6jdlq-ew.a.run.app/predict/"
#     files = {"file": image_bytes}

#     response = requests.post(api_url, files=files)
#     response_json = response.json()
#     mood = response_json.get("prediction")
#     description = mood_explanations.get(mood, {}).get("description")
#     fact = mood_explanations.get(mood, {}).get("fact")

#     return mood, description, fact

st.markdown("### Upload your pet's photo")

img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if img_file_buffer is not None:

    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded")

    with col2:
        with st.spinner("Analyzing the mood..."):
            mood, description, fact = predict_emotion(img_file_buffer.getvalue())
            st.markdown(f"**Mood: {mood}!**")
            st.markdown(f"*{description}*")
            st.markdown(f"**Random Fact:** {fact}")
