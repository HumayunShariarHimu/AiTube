from moviepy.editor import *

def make_video(image_path="assets/bg.jpg", audio_path="assets/voice.mp3", output="final_video.mp4"):
    clip = ImageClip(image_path).set_duration(AudioFileClip(audio_path).duration)
    clip = clip.set_audio(AudioFileClip(audio_path))
    clip.write_videofile(output, fps=24)