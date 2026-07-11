# import cv2

def video_to_grayscale(input_video, output_video):
    print(f'Converting {input_video} to grayscale video at {output_video}...')
    # cap = cv2.VideoCapture(input_video)
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter(output_video, fourcc, 20.0, (640, 480), isColor=False)
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret: break
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     out.write(gray)
    # cap.release()
    # out.release()
    print('Conversion complete!')

if __name__ == '__main__':
    video_to_grayscale('input.mp4', 'output_gray.avi')