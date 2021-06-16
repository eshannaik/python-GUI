from tkinter import *
from tkinter import messagebox,filedialog
from pytube import YouTube
import youtube_dl


top = Tk()
top.geometry("500x400")
top.title("Youtube Downloader")


download_path = StringVar()


#Single Video
def Download():
	url = plid.get()
	download_Folder = download_path.get()
	getVideo = YouTube(url)
	video = getVideo.streams.first()
	video.download(download_Folder)
	messagebox.showinfo(title="Message",message="Your video has been downloaded at :" + download_Folder)
# Full Playlist
def download_full():
	URL=plid.get()
	download_Folder = download_path.get()
	ydl_opts={}
	with youtube_dl.YoutubeDL(ydl_opts)as ydl:
		print(ydl)
		ydl.download([URL])
	messagebox.showinfo(title="Message",message="Your video has been downloaded")
	
#Destination of file
def Browse():
	destination = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
	download_path.set(destination)


l = Label(top,text="Youtube Video Downloader",font=('Arial',18,'bold'))
l.pack(pady=10)

text = Text(top, height = 5, width = 60)
text.pack(padx=5,pady=10)

instructions = "Enter the link of the youtube video or playlist. To download a video to a particular location choose destination using   the Save to buttona dn then click the Download Single video Button. To download a playlist enter the playlist URL       (public playlist) and click download. The playlsit will get downloaded at the same location of this code"
text.insert(END,instructions)

l1 = Label(top,text="Enter playlist URL",font=('Arial',10))
l1.pack(pady=10)

plid = Entry(top,width=300)
plid.pack(pady=10,padx =10)

destination_label = Label(top, text="Destination :", font=('Arial',12))
destination_label.place(x = 20 , y= 250)
   
destination_text = Entry(width = 40,textvariable = download_path) 
destination_text.place(x=120, y=250)

btn = Button(top,text="Save to",command=Browse)
btn.place(x = 400,y=250)

dbs = Button(top,text="Download Single Video",command=Download)
dbs.place(x = 175 , y= 300)

dbf = Button(top,text="Download Entire Playlist",command=download_full)
dbf.place(x = 175 , y= 350)


top.mainloop()
