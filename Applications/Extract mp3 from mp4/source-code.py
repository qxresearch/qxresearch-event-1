import moviepy
import moviepy.editor


# Get this library installed in your system

# Import your video file
# Media file should be local
video = moviepy.editor.VideoFileClip("")    # Put your file path in here

# Convert video to audio
audio = video.audio
audio.write_audiofile('new_audio.mp3')

