import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os

# Set page tab display
st.set_page_config(
   page_title="Pet Face Expression Recognition",
   page_icon= '🐾',
   layout="wide",
   initial_sidebar_state="expanded",
)

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = 'http://localhost:8000'
load_dotenv()
url = os.getenv('API_URL')


# App title and description
st.header('Pet Face Expression Recognition 🐾')
st.markdown('''
            > Welcome to the Pet Face Expression Recognition tool!
            >Upload a photo of your pet, and let's try to understand their mood.

            > **What you have to do:

            > * Upload a photo of your pet.
            > * We will guess the mood of your pet!
            > * Try other animals. Even a chicken can show happiness 🐣
            ''')

st.markdown("---")

### Create a native Streamlit file upload input
st.markdown("### Upload your pet's photo")
img_file_buffer = st.file_uploader('Upload an image')

def process_image(image_bytes):
    return "Happy"


if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded")

  with col2:
    with st.spinner("Analyzing the mood..."):
      mood = process_image(img_file_buffer.getvalue())
      st.markdown(f"**Mood: {mood}!**")

      '''
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to  API (stream=True to stream response as bytes)
      res = requests.post(url + "/upload_image", files={'img': img_bytes})

      if res.status_code == 200:
        ### Display the image returned by the API
        st.image(res.content, caption="Image returned from API ☝️")
      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.status_code, res.content)
        '''
