from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from pytube import YouTube, Playlist

def down_video():
    try:
        yt = YouTube(linkvar.get())
        status_label.configure(text="Downloading  your video.....")
        root.update() 
        stream = yt.streams.filter(res=res_var.get()).first()
        
        if stream:
            stream.download(output_path=path_var.get())
            status_label.configure(text="Video downloaded successfully!")
        else:
            status_label.configure(text="Resolution not available for this video. Please choose another resolution.")
    except Exception as e:
        status_label.configure(text="Error downloading video: " + "please Check your Video link or path and try again")

def down_Playlist():
    try:
        playlist = Playlist(linkvar.get())
        if not playlist:
            status_label.configure(text="Invalid playlist link. Please enter a valid YouTube playlist link.")
            return
        for video in playlist.videos:
            try:
                status_label.configure(text=f"Downloading {video.title}  ..... ")
                root.update() 
                
                stream = video.streams.filter(res=res_var.get()).first()
                if stream:
                    stream.download(output_path=path_var.get())
                    status_label.configure(text="Downloaded: " + video.title)
                else:
                    status_label.configure(text="Resolution not available for " + video.title + ". Skipping.")
            except Exception as e:
                status_label.configure(text="Error downloading " + video.title + ": " + str(e))
        status_label.configure(text="Your Playlist is Downloaded")
    except Exception as e:
        status_label.configure(text="Error downloading playlist: " + "please Check your Playlist link or path  or Internet Connection and try again")


def open_file_manager():
    try:
        selected_path = filedialog.askdirectory()
        if selected_path:
            path_var.set(selected_path)
    except Exception as e:
        status_label.configure(text="Error selecting path: " + str(e))

def ref_win():
    root.update()
    
root = Tk()
root.title("PlayListicious")
root.geometry("700x620")
root.configure(bg="#1f1f1f")
root.resizable(False, False)

# Styles
rounded = ttk.Style()
rounded.configure("Custom.TButton", foreground="white", font=("Arial", 12, "bold"), background="#ff3333")

path_var = StringVar()

def Download():
    try:
        VorP = vorp.get()
        if not linkvar.get():
            status_label.configure(text="Please enter a valid YouTube video or playlist link.")
        elif not path_var.get():
            status_label.configure(text="Please select a download path.")
        elif VorP == "Video":
            if "/playlist" in linkvar.get():
                status_label.configure(text="Link type mismatch. Please choose 'Playlist' for playlist links.")
            else:
                down_video()
        else:
            if "/watch" in linkvar.get():
                status_label.configure(text="Link type mismatch. Please choose 'Video' for video links.")
            else:
                down_Playlist()
    except Exception as e:
        status_label.configure(text="Error during download: " + str(e))

# Upper label

Label(text="Welcome to PlayListicious", fg="#ff3333", bg="#1f1f1f", font=("Arial", 24)).place(relx=0.5, rely=0.05, anchor="center")

# refresh button

download = Button(root,text="\u27F3" ,compound="left", cursor="hand2", command=ref_win, width=2)
download.place(relx=0.02, rely=0.02)

# Select video or playlist
Label(text="Select Your Link Type", fg="white", bg="#1f1f1f", font=("Arial", 14)).place(relx=0.1, rely=0.2)
vorp = StringVar()
r1 = Radiobutton(root, text="Video", value="Video", variable=vorp, bg="#1f1f1f", fg="white", font=("Arial", 12), selectcolor="#1f1f1f")
r2 = Radiobutton(root, text="Playlist", value="Playlist", font=("Arial", 12, "bold"), variable=vorp, bg="#1f1f1f", fg="white", selectcolor="#1f1f1f")

vorp.set("Video")
r1.place(relx=0.1, rely=0.27)
r2.place(relx=0.3, rely=0.27)

# Taking input of link
Label(text="Enter Link of YouTube Video or Playlist", fg="white", bg="#1f1f1f", font=("Arial", 14)).place(relx=0.1, rely=0.37)
linkvar = StringVar()
link = Entry(root, textvariable=linkvar, width=50, font=("Arial", 12))
link.place(relx=0.1, rely=0.42)

# Resolution
res_var = StringVar()
Label(root, text="Choose Resolution for Your Download", fg="white", bg="#1f1f1f", font=("Arial", 14)).place(relx=0.1, rely=0.52)
resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
res_var.set(resolutions[2])
quality = OptionMenu(root, res_var, *resolutions)
quality.configure(fg="#ff3333", bg="#1f1f1f", width=15, height=1, font=("Arial", 12))
quality.place(relx=0.1, rely=0.57)

# Path entry
Label(root, text="Select Path Where you want to Download ", fg="white", bg="#1f1f1f", font=("Arial", 14)).place(relx=0.1, rely=0.67)
path_entry = Entry(root, textvariable=path_var, width=50, font=("Arial", 12))
path_entry.place(relx=0.1, rely=0.72)
path_button = Button(root, text="Browse", command=open_file_manager)
path_button.configure(fg="#ff3333", bg="#1f1f1f", font=("Arial", 12))
path_button.place(relx=0.65, rely=0.71)

# Download button
# download_icon = Image.open("")
# download_icon = download_icon.resize((35, 35))
# download_icon = ImageTk.PhotoImage(download_icon)

download = ttk.Button(root, text="Download", style="Custom.TButton", compound="left", cursor="hand2", command=Download, width=12)
download.place(relx=0.3, rely=0.8)

# Status label
status_label = Label(root, text="", fg="white", bg="#1f1f1f", font=("Arial", 12),wraplength=600)
status_label.place(relx=0.4, rely=0.9, anchor="center")

root.mainloop()
