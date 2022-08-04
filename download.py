from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube



def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)




def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()





screen = Tk()
title = screen.wm_title("DC Youtube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#imagem logo
logo_img = PhotoImage(file="yt_logo.png")

logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)


link_field = Entry(screen, width=50)
link_label = Label(screen, text="Digite a URL do Vídeo:", font=("Arial", 15))

path_label = Label(screen, text="Selecione o destino para Download", font=("Arial", 15))
select_btn = Button(screen, text="Selecione", command=select_path)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)


download_btn = Button(screen, text="Download", command=download_file)

canvas.create_window(250, 390, window=download_btn)



screen.mainloop()
