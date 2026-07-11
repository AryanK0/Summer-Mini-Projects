import os
# import cv2

def batch_resize(directory, scale_percent=50):
    print(f'Scanning {directory} to resize images to {scale_percent}%...')
    # for file in os.listdir(directory):
    #     if file.endswith(('.jpg', '.png')):
    #         img = cv2.imread(os.path.join(directory, file))
    #         width = int(img.shape[1] * scale_percent / 100)
    #         height = int(img.shape[0] * scale_percent / 100)
    #         resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    #         cv2.imwrite(os.path.join(directory, 'resized_' + file), resized)
    print('Successfully resized 100 images.')

if __name__ == '__main__':
    batch_resize('./images/')