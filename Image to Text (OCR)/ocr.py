def extract_text(image_path):
    # import pytesseract
    # from PIL import Image
    print(f'Extracting text from {image_path}...')
    # text = pytesseract.image_to_string(Image.open(image_path))
    return 'Mock Extracted Text from OCR.'

if __name__ == '__main__':
    print(extract_text('receipt.png'))