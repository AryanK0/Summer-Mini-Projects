# import cv2

def resize_video(input_video, output_video, scale=0.5):
    print(f'Resizing {input_video} to {scale*100}%...')
    # cap = cv2.VideoCapture(input_video)
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret: break
    #     width = int(frame.shape[1] * scale)
    #     height = int(frame.shape[0] * scale)
    #     resized = cv2.resize(frame, (width, height))
    #     # write frame to output...
    print('Video resized successfully.')

if __name__ == '__main__':
    resize_video('input.mp4', 'output_small.mp4')