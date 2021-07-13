# welcome
# rename this file extension from .pyw to .py to show console window.

import moviepy      # moviepy - Get this library installed in your system [pip install moviepy].
import moviepy.editor
import tkinter as tk  # import Tkinter module
from tkinter.filedialog import askopenfilename ,asksaveasfilename  # file dialog to get video and audio file paths.

global open_file_path
global save_file_path

# to get file path of video file.
def fileopen():
    global open_file_path
    open_file_path = askopenfilename(
    filetypes=[("All Files", "*.*")]  # Here you can specify different file extensions.
    )
    if not open_file_path:
        return
    open_path.insert(0, open_file_path) # insert the file path to Entry.

# to get file path for audio file to be saved.
def filesave():
    global save_file_path
    save_file_path = (asksaveasfilename(
    filetypes=[("audio file", '*.MP3'),("All files", '*.*')]   # Here you can specify different file extensions.
    ) + ".mp3")
    if not save_file_path:
        return
    save_path.insert(0, save_file_path)  # insert the file path to Entry.

# The main program to convert a video file to audio file.
def file_convert(video_file,audio_file):         # Here video_file and audio_file are the file paths.
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio     # Main convertion from video to audio.
    audio.write_audiofile(audio_file)
    popup = tk.Toplevel()      # A popup window saying completed.
    popup.title("completed!")
    popup_text=tk.Label(popup, text="sucessfully converted and saved to your location \n\n\n credits:qxresearch @ GitHub ",height=10).pack(side=tk.TOP,anchor='nw')
    popup.mainloop()

# The main window to enter video and audio file paths.
uiwindow = tk.Tk()
uiwindow.title("video to audio converter")
main_frame = tk.Frame(uiwindow, height=20,width=80).pack(side=tk.TOP, fill=tk.BOTH)  # A main frame which holds video and audio file paths.
open_label = tk.Label(main_frame, text="enter the path of the video file to be converted:").pack(side=tk.TOP ,anchor='w')
open_path = tk.Entry(main_frame, width=50)  # Entry for video file path.
open_path.pack(side=tk.TOP, fill=tk.BOTH)
open_Button = tk.Button(main_frame, text="Browse..",bg="sky Blue",command = lambda:fileopen()).pack(side=tk.TOP, anchor='e')  # Button to locate video file.
empty_space = tk.Label(main_frame, height=3).pack(side=tk.TOP,fill=tk.BOTH)  # Empty Label for good look.
save_label = tk.Label(main_frame, text="enter the path for the converted audio file to be saved:",height=1).pack(side=tk.TOP ,anchor='w')
save_path = tk.Entry(main_frame, width=50)   # Entry for audio file path.
save_path.pack(side=tk.TOP, fill=tk.BOTH)
save_button = tk.Button(main_frame, text="Browse..",bg="sky Blue", command=lambda:filesave()).pack(side=tk.TOP, anchor='e')  # Button to locate audio file to be saved.
empty_space2 = tk.Label(uiwindow, text="______________________________________________________________________",height=2,fg="green")
empty_space2.pack(side=tk.TOP,fill=tk.BOTH,anchor='s')   # Empty Label for good look.
second_frame = tk.Frame(uiwindow,width=100).pack(side=tk.TOP)   # A second frame which holds cancel and convert Buttons.
convert_button = tk.Button(second_frame, text="convert",bg="pink",borderwidth=4,command=lambda:[file_convert(open_file_path,save_file_path)])
convert_button.pack(side=tk.RIGHT, anchor='ne', padx=5,pady=5)  # The convert Button.
# cancel Button.
cancel_Button = tk.Button(second_frame, text="cancel",bg="pink",borderwidth=4,command=lambda:uiwindow.destroy()).pack(side=tk.RIGHT, anchor='ne',padx=5, pady=5)
uiwindow.mainloop()

'''
comment: The main program [non-graphical interface] is here..
import moviepy
import moviepy.editor
video = moviepy.editor.VideoFileClip('#')  # - path to video file.
audio = video.audio
audio.write_audiofile('#') # - path to audio file.
'''

# qxresearch @ GitHub.
# Thank You.
