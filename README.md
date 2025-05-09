🧾 MultiLanguage Invoice Extractor

📘 Project Overview

This project is a Streamlit-based AI application that extracts and interprets information from invoice images in multiple languages using Google's Gemini 1.5 Flash model. It enables users to upload invoice images, input custom prompts or questions (in any language), and get relevant information extracted and explained intelligently by the model.

🔍 Key Features

->📸 Upload invoices in image format (JPG, JPEG, PNG).

->🌐 Supports multilingual prompts for versatile document interpretation.

->🧠 Uses Gemini 1.5 Flash to analyze invoices and generate meaningful responses.

->🛡️ Secure input of Google API Key via the Streamlit sidebar.

->⚙️ Lightweight and interactive Streamlit UI for real-time interaction.

⚙️ How It Works
->The user provides their Google API key securely in the sidebar.

->The user uploads an invoice image and optionally enters a question or command (e.g., "Extract the total amount and invoice number").

->On clicking "Tell me about the invoice":

    o The invoice image is converted into a Gemini-compatible input format.

    o A base prompt provides domain context (invoice understanding).

    o The Gemini model processes the image and prompt together and returns a response.

->The extracted invoice details or answers are displayed in real time.

