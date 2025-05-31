import streamlit as st
from PIL import Image
import tempfile
import os

# --- App Header ---
st.set_page_config(page_title="Personal Stylist AI", layout="centered")
st.title("🧠👗 Personal Stylist AI")
st.markdown("Upload your photo and tell us your fashion preferences — we’ll find the best styles for you!")

# --- API Key Input ---
api_key = st.text_input("🔑 Enter your API Key", type="password")
if not api_key:
    st.warning("Please enter your API key to proceed.")

# --- Image Upload ---
st.subheader("📷 Upload Your Photo")
user_image = st.file_uploader("Choose an image file (JPG/PNG)", type=["jpg", "jpeg", "png"])

# --- Text Input ---
st.subheader("📝 Describe Your Style")
text_input = st.text_area("What kind of clothes do you like?", placeholder="e.g. I like casual streetwear with earthy tones...")

# --- Audio Input ---
st.subheader("🎤 Or Describe with Audio")
audio_file = st.file_uploader("Upload an audio file (MP3/WAV)", type=["mp3", "wav"])

# --- Process Inputs ---
if st.button("👗 Find My Style"):
    if not api_key:
        st.error("API key is required.")
    elif not user_image:
        st.error("Please upload your image.")
    elif not text_input and not audio_file:
        st.error("Please provide either text or audio description.")
    else:
        st.success("Processing your style profile...")

        # Save image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as img_tmp:
            img_tmp.write(user_image.read())
            image_path = img_tmp.name

        st.image(Image.open(image_path), caption="Your Uploaded Photo", use_column_width=True)

        # Display inputs
        if text_input:
            st.markdown("**Your Style Description (Text):**")
            st.write(text_input)
        if audio_file:
            st.markdown("**Your Audio Description:**")
            st.audio(audio_file)

        # ---- FAKE OUTPUT: Replace this section with your actual ML/AI output ----
        st.subheader("🛍️ Recommended Outfits")
        st.markdown("Here are some outfit suggestions based on your preferences:")
        st.image("https://images.unsplash.com/photo-1618354691444-48cdbd411059", caption="Casual Earthy Look")
        st.image("https://images.unsplash.com/photo-1618354309232-efb53cbb3834", caption="Stylish Streetwear")
        # -------------------------------------------------------------------------

        # Clean up temp image
        os.remove(image_path)
