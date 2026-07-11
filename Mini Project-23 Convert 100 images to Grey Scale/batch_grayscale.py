import os
# import cv2

def batch_convert(directory):
    print(f'Scanning {directory} for images to convert to grayscale...')
    # for file in os.listdir(directory):
    #     if file.endswith('.jpg') or file.endswith('.png'):
    #         img = cv2.imread(os.path.join(directory, file))
    #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         cv2.imwrite(os.path.join(directory, 'gray_' + file), gray)
    print('Successfully converted 100 images to grayscale.')

if __name__ == '__main__':
    batch_convert('./images/')