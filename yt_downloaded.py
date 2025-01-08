#gui and youtube modules
import tkinter
import customtkinter
from pytube import YouTube
from yt_dlp import YoutubeDL
import os

def startDownload():
    
    yt_dlp_Link = link.get()
    if not yt_dlp_Link.strip():
            finishLabel.configure( text = "Error: The URL cannot be empty.", text_color='red')
            return
    
    # Create a 'downloads' directory relative to the script
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        
     
    try:
        ydl_opts = {
            'format':'best',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            } 
    
        #download the video
        with YoutubeDL(ydl_opts) as yt_dlp_object:
            yt_dlp_object.download([yt_dlp_Link])
        
        finishLabel.configure(text="Downloaded", text_color = "green")
    except Exception as e:
        finishLabel.configure(text=f"{e}", text_color="red")
    

#desinging the ui - System Settings
customtkinter.set_appearance_mode("dark") #dark mode light mode
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk(); #initilise the app
app.geometry("800x600")
app.title("Youtube Downloader App")

# Top Navbar
navbar = customtkinter.CTkFrame(app, height=50, fg_color="black", corner_radius=0)
navbar.pack(fill="x", side="top")
title_label = customtkinter.CTkLabel(navbar, text="YouTube Downloader", font=("Arial", 18), text_color="white")
title_label.pack(side="left", padx=20, pady=10)

#UI elements
title = customtkinter.CTkLabel(app, text = "Insert Youtube Link Here:", text_color="red") #customtinkinter. makes ui links
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#download button
download = customtkinter.CTkButton(app, text="DOWNLOAD", fg_color= "red", command=startDownload)
download.pack(padx=20,pady=20)

#finish downloading
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

# Footer
footer = customtkinter.CTkFrame(app, height=50, fg_color="black", corner_radius=0)
footer.pack(fill="x", side="bottom")

footer_label = customtkinter.CTkLabel(footer, text="© Custom YouTube Downloader | Made by @mayowa.oluwasanmi", text_color="white")
footer_label.pack(side="right", padx=10, pady=10)

#run the app
app.mainloop()