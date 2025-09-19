import os, sys
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import Toplevel, messagebox, filedialog
import webview
import yt_dlp
import json

# --- Detect base rute---
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(base_path, "icon.ico")

# Route of ffmpeg_dir
ffmpeg_dir = os.path.join(base_path, "ffmpeg", "bin")

window = Tk()
window.title('Youtube Downloader - JonathanManzanoDiaz')
window.geometry('500x170')
window.resizable(0, 0)
window.iconbitmap(icon_path)

# BUTTON MP4
def download_mp4():
    url = urlInput.get()
    if not (url.startswith('http://youtube.com') or url.startswith('www.youtube.com/') or url.startswith('https://youtu.be/')):
        messagebox.showerror("Error Link", "Invalid link, the valid link start with http o www.")
        return

    # Ventana nueva para elegir resolución
    dwg_mp4 = Toplevel(window)
    dwg_mp4.title('Downloading MP4 Video')
    dwg_mp4.geometry('300x300')
    dwg_mp4.resizable(0, 0)
    
    resolutions = Listbox(dwg_mp4, font=('Arial', 10, 'bold'))
    resolutions.place(x=10, y=80, width=280, height=210)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # FFMPEG DIR

    
    # ADD TO THE LIST BOX
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        info_json = json.dumps(ydl.sanitize_info(info), indent=2, ensure_ascii=False)
        videos = []
        for f in info["formats"]:
            if f.get('ext') == 'mp4':
                formats = f["format_id"]
                quality = f.get("height")
                filesize = f.get("filesize")
                if filesize and quality >= 360:
                    final = f"{quality}p - {filesize / 1000000:.2f}MB"
                    videos.append(formats)
                    resolutions.insert(END, final)
    def view_video():
        webview.create_window('Video Selected', url)
        webview.start()
    
    def do_download_mp4():
        # SELECT FROM LISTBOX
        selected = resolutions.curselection()[0]
        format_id = videos[selected]
        # UPGRADE THE WINDOW DWG_MP4
        dwg_mp4.geometry("300x360")
        folder = filedialog.askdirectory(title="Where do you want to save the video?")
        if not folder:
            return
        # PROGRESS BAR
        progress = Progressbar(dwg_mp4, orient=HORIZONTAL, length=280, mode='determinate')
        progress.place(x=10, y=300)
        progress_label = Label(dwg_mp4, text="Progress: 0%")
        progress_label.place(x=10, y=330)
        # FOLDER THE PROGRAM

        # Hook PROGRESS
        download_done = False
        
        def my_hook(d):
            nonlocal download_done
            if d['status'] == 'downloading':
                percent = float(d['_percent_str'].replace('%', '').strip())
                progress['value'] = percent
                progress_label.config(
                    text=f"Progress: {d['_percent_str']} | Speed: {d['_speed_str']} | ETA: {d['_eta_str']}"
                )
                dwg_mp4.update_idletasks()
            elif d['status'] == 'finished' and not download_done:
                download_done = True
                progress['value'] = 100
                progress_label.config(text="¡Download Completed!")
        
        #OPTS YDL
        ydl_opts = {
            'format': f'{format_id}+bestaudio',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'ffmpeg_location': ffmpeg_dir,
            'merge_output_format': 'mp4',
            'progress_hooks': [my_hook]
        }
        # DOWNLOAD YDL
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    
        messagebox.showinfo("Download Completed", "Video downloaded successfully.")
    
    view_videoBtn = Button(dwg_mp4, font=("Arial", 15, 'bold'), text='View Video', command=view_video)
    view_videoBtn.place(x=20, y=20)
    download_btn = Button(dwg_mp4, font=("Arial", 15, 'bold'), text='Download', command=do_download_mp4)
    download_btn.place(x=170, y=20)
    
def download_mp3():
    url = urlInput.get()
    if not (url.startswith('http://youtube.com') or url.startswith('www.youtube.com/') or url.startswith(
        'https://youtu.be/')):
        messagebox.showerror("Error Link", "Introduce un link válido que empiece con http o www.")
        return
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder = filedialog.askdirectory(title="Where do you want to save the audio?")
    if not folder:
        return
    confirm = messagebox.askokcancel(message="Do you want to continue downloading the mp3?", title="Confirm download")
    if confirm:
        # options de yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'ffmpeg_location': ffmpeg_dir,
            'merge_output_format': 'mp3',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        # Mostrar mensaje al finalizar
        messagebox.showinfo("Download Completed", "Download Completed!.")
    else:
        return
# --- GUI Principal ---
labelTitle = Label(font=('Arial', 20, 'bold'), text='Youtube Downloader')
labelTitle.pack(pady=10)

urlInput = Entry(font=('Arial', 20, 'bold'))
urlInput.config(justify='center')
urlInput.place(x=10, y=55, height=50, width=470)

Button(font=("Arial", 15, 'bold'), text='Download MP4', command=download_mp4).place(x=50, y=115)
Button(font=("Arial", 15, 'bold'), text='Download MP3', command=download_mp3).place(x=280, y=115)

window.mainloop()
