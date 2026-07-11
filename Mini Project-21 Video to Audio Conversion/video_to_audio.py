# import moviepy.editor as mp

def extract_audio(video_path, audio_path):
    print(f'Extracting audio from {video_path} to {audio_path}')
    # clip = mp.VideoFileClip(video_path)
    # clip.audio.write_audiofile(audio_path)
    print('Extraction complete!')

if __name__ == '__main__':
    extract_audio('lecture_video.mp4', 'lecture_audio.mp3')