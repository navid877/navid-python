from moviepy.editor import *
from tkinter import *
from tkinter.filedialog import *
 
path = askopenfilename()

video = VideoFileClip(path)

aud = video.audio

aud.write_audiofile("ok.mp3")

print("Done....")




