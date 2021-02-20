import moviepy.editor
# Get this library installed in your system


# Import your video file
# Media file should be local
video = moviepy.editor.VideoFileClip("video_trial.mp4")    # Put your file path in here

# Convert video to audio
audio = video.audio

# Writing an audio file...
audio.write_audiofile('new_audio.mp3')  # Rename the "new_audio" to what you want...

print("Your video has been converted into audio. Go and have a look...")
