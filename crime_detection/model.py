import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyCFa8RkccW1Qhm1rY2RcJn6l6Z_N8j3W2I")

def detect_crime_from_image(image_path):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")


        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img = img.resize((512, 512))

        prompt = (
            "First, check if there's any visual indication of crime in this image.\n"
            "If yes, classify it as one of: Murder, Theft, Arson, Vandalism, Suspicious Activity.\n"
            "If there's no indication of crime (e.g., a regular portrait, scenery), say: No Crime Detected.\n"
            "Only return the label."
        )

        response = model.generate_content([prompt, img])

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"
