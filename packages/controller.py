from .view import Youtube_interface
from .model import Video_Model
import pyperclip as clip
from pytube import YouTube
from urllib.error import URLError
from pytube.exceptions import AgeRestrictedError
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox


class Controller:
    def __init__(self, Model:Video_Model, View: Youtube_interface) -> None:
        # created the Model and View in the Controller class.
        self.view = View
        self.model = Model

        # // view functions here.
        self.view.Paste_func(self.paste)
        self.view.SelectDirectory(self.select_directory)
        self.view.Cancel_window(self.close_window)
        self.view.StartDownload(self.Download)

    ## == callback function for pasting url 
    def paste(self, event):
        copied_url = clip.paste()
        self.view.video.Link.set(copied_url)
        self.model.ValidateLink(self.view.video.Link.get())

    ## => callback function for selecting the directory
    def select_directory(self, event):
        self.view.location = filedialog.askdirectory()
        CTkMessagebox(title="Location Saved", message="Location for Video: \n{0}".format(self.view.location), icon="info")
        
    ## closes the window when cancel_button is triggered on the interface
    def close_window(self, event):
        self.view.destroy()

    # --> download starts when the download button is been triggered.
    def Download(self, event):
        if self.view.location == "":
            CTkMessagebox(title="Empty Location", message="Please enter location for the video to be saved.")

        video_url = self.view.video.Link.get() # < -- video_url 
        video_type =  self.view.video.Type.get() # <-- type of the stream whether video or audio format
        video_quality = self.view.video.quality.get() # <-- quality of the stream eg. 240p, 360p etc.
        saved_location = self.view.location # < -- location where stream to be saved.
        

        if video_type == "" or video_quality == "":
            CTkMessagebox(title="Error Occured", message="It seems that stream type or quality has not been selected..", icon="cancel")

        else:
            # --> tracking errors when trying to download..
            try:
                video = YouTube(video_url)
                streams = video.streams

                if video_type == "Audio":
                    filter = streams.get_audio_only(subtype="mp4")

                else:
                    filter = streams.get_by_resolution(video_quality)

            except AgeRestrictedError:
                CTkMessagebox(title="Error Occured!",message=" A1EVQtJJwZA is age restricted, and can't be accessed without logging in.", icon='cancel')

            except URLError:
                CTkMessagebox(title="Error Occured!", message="Please Check URL or It could be a connection problem.", icon="cancel")

            ## -- if No errors downloading can proccessed ..
            else:
                self.view.stream_details.insert(index = "0.0",text="\n\nStream Title: {0}\nStream Type: {1}\nQuality: {2}\nSave location: {3}\nFile-Size: {4} MB".format(video._title, video_type, video_quality,saved_location, filter.filesize_mb))
                filter.download(saved_location)
                CTkMessagebox(title="Success", message="Download is Successfully Done!", icon="check")

    def run_app(self): #.// it runs the instanes of the view class
        self.view.mainloop()
