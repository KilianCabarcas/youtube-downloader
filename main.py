import tkinter
import customtkinter
from pytube import YouTube




def StartDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title,text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Download Finished")
    except:
        finishlabel.configure(text="Download Failed",text_color="red")

def on_progress(stream,chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()

    #update
    ProgressBar.set(float(percentage_of_compeletion)/100)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert video link")
title.pack(padx=10,pady=10)

#Link input
url_var=tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#Finished Downloading
finishlabel= customtkinter.CTkLabel(app, text="")
finishlabel.pack()

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

ProgressBar = customtkinter.CTkProgressBar(app, width=400)
ProgressBar.set(0)
ProgressBar.pack(padx=10,pady=10)

#Download button
Download = customtkinter.CTkButton(app,text="Download",command=StartDownload)
Download.pack(padx=10,pady=10)

#Run app mainloop

app.mainloop()