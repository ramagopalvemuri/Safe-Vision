import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crime_detection.model import detect_crime_from_image
from accessibility.braille_converter import text_to_braille
from accessibility.speech_output import speak_text

st.set_page_config(page_title="SafeVision - Smart Crime Alert", layout="centered")
st.title("🔐 SafeVision: Inclusive Smart Crime Alert System")

uploaded_file = st.file_uploader("Upload a Crime Scene Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    img_path = "temp_uploaded_image.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state["uploaded_image_path"] = img_path

if st.button("Analyze Crime"):
    with st.spinner("Analyzing image..."):
        result = detect_crime_from_image(img_path)
        st.session_state["last_result"] = result
        st.success("✅ Analysis complete!")

if "last_result" in st.session_state:
    result = st.session_state["last_result"]
    st.success(f"🕵️ Result: {result}")

    if st.button("🔊 Speak Alert", key="speak_alert"):
        st.write("🔊 Speaking now...")
        speak_text(result)
    st.success("✅ Alert spoken successfully!")

    if st.button("Convert to Braille"):
        braille = text_to_braille(result)
        st.code(braille, language="text")
        st.success("✅ Braille conversion successful!")
