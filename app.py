import streamlit as st
from PIL import Image
import time

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
            > * We will guess the mood and species of your pet! Angry, Happy, Sad or Other...
            > * Try other animals. Even a sheep can show emotions. 🐑
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

st.markdown("### Upload your pet's photo")

img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if img_file_buffer is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(Image.open(img_file_buffer), caption="Here's the majestic creature")
    # Initialize an empty container for status messages
    with col2:
        status_message = st.empty()
        progress = st.progress(0)

    status_message.text('Waking up the pet psychics from their catnaps...')
    progress.progress(25)
    time.sleep(1)

    status_message.text("Decrypting tail wags and whisker twitches...")
    progress.progress(50)
    time.sleep(1)

    status_message.text('Translating into hooman language...')
    progress.progress(75)
    time.sleep(1)

    #Call prediction
    primary_mood, secondary_mood, classification, description, fact = predict_emotion(img_file_buffer.getvalue())

    status_message.text('Voilà! Here’s what your pet is saying.')
    progress.progress(100)
    time.sleep(1)

    status_message.empty()
    progress.empty()

    with col2:
        #To edit the type of output of classification
        animal_type = classification.split("a photo of a ")[-1].capitalize()
        st.markdown(f"**Mood: {primary_mood} {animal_type}!** *{fact}*")
        st.markdown(f"**Signs:** *{description}*")
        if secondary_mood:
            if secondary_mood == "other":
                st.markdown("**Second Opinion:** It is possible that your pet can be in another mood that is not in our range of moods yet. This opinion is based on a close accuracy difference.")
            else:
                # For any secondary mood other than "Other", display it normally
                st.markdown(f"**Second Opinion: {secondary_mood} {animal_type}!** This opinion is based on a close accuracy difference.")
