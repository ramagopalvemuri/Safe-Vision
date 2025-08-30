from crime_detection.model import detect_crime_from_image
from accessibility.braille_converter import convert_to_braille
from accessibility.speech_output import speak_text

def main(image_path):
    crime = detect_crime_from_image(image_path)
    print(f"[+] Crime Detection Result: {crime}")
    
    braille = convert_to_braille(crime)
    print(f"[+] Braille Output: {braille}")
    
    print("[+] Speaking the alert...")
    speak_text(crime)

if __name__ == "__main__":
    main("test_media/sample_image.jpg")
