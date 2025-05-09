import streamlit as st
from PIL import Image
import google.generativeai as genai

# Streamlit App Config
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")

# Sidebar: Secure API Key Input
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

# Input prompt and file uploader
input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

# Display uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the invoice")

# Prompt to guide the model
input_prompt = """
You are an expert in understanding invoices.
You will receive input images as invoices &
you will have to answer questions based on the input image.
"""

# Helper function: Convert uploaded image to Gemini input format
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Generate response using Gemini
def get_gemini_response(api_key, input_text, image, prompt):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Handle Submit
if submit:
    if not api_key:
        st.error("Please enter your Google API key in the sidebar.")
    elif not uploaded_file:
        st.warning("Please upload an invoice image.")
    else:
        try:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(api_key, input_prompt, image_data, input_text)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
