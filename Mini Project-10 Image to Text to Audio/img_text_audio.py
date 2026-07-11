# import pytesseract
# from PIL import Image
# import pyttsx3

def process_image(image_path):
    print(f'Extracting text from {image_path} using Tesseract...')
    # text = pytesseract.image_to_string(Image.open(image_path))
    text = 'Sample extracted text from image.'
    print(f'Extracted Text: {text}')
    
    print('Converting text to audio...')
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
    print('Audio playback finished.')

if __name__ == '__main__':
    process_image('sample_image.jpg')