import moviepy
video = moviepy.editor.VideoFilePath("")
audio=video.audio 
audio.write_audiofile('1.mp3')
