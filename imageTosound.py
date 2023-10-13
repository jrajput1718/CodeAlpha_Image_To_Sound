from PIL import Image
from gtts import gTTS
import pytesseract
import os 
from pytesseract import image_to_string
# from playsound import playsound

def image_to_sound(path_to_image):
    
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)

        result = pytesseract.image_to_string(loaded_image)
        # print(result) 
        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing the code\n", bug)
        return


if __name__ == "__main__":
    image_to_sound("image1.jpg")
    input()