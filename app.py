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

st.markdown("### Upload your pet's photo")

img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
# if img_file_buffer is not None:

#     col1, col2 = st.columns(2)

#     with col1:
#         st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded")

#     with col2:
#         with st.spinner("Analyzing the mood..."):
#             mood, description, fact = predict_emotion(img_file_buffer.getvalue())
#             st.markdown(f"**Mood: {mood}!**")
#             st.markdown(f"*{description}*")
#             st.markdown(f"*{fact}*")

if img_file_buffer is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open(img_file_buffer), caption="Here's the majestic creature")

    # Initialize an empty container for status messages
    status_message = st.empty()

    # Initialize progress bar
    progress = st.progress(0)

    # Loading model simulation
    status_message.text('Waking up the pet psychics from their catnaps...')
    progress.progress(25)
    time.sleep(2)  # Simulating a delay

    # Analyzing image simulation
    status_message.text("Decrypting tail wags and whisker twitches...")
    progress.progress(50)
    time.sleep(2)  # Simulating analysis delay

    # Almost done simulation
    status_message.text('Translating into hooman language...')
    progress.progress(75)
    time.sleep(2)  # Simulating wrapping up processing

    # Predict emotion from the image
    mood, description, fact = predict_emotion(img_file_buffer.getvalue())

    # Update UI with the prediction result
    status_message.text('Voilà! Here’s what your pet is saying.')
    progress.progress(100)
    time.sleep(1)  # Short pause to let user acknowledge completion

    # Clear the status message and progress bar
    status_message.empty()
    progress.empty()

    with col2:
        st.markdown(f"**Mood: {mood}!**")
        st.markdown(f"*{fact}*")
        st.markdown(f"**Signs:** *{description}*")
