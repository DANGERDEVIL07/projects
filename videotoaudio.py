import moviepy.editor as mp 

clip = mp.VideoFileClip(r"closer.mp4")

clip.audio.write_audiofile(r"audio.mp3")
