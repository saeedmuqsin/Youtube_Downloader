
import validator_collection as URL_Validator
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkFont

# model.py handles the data logic and having operations perform on the data
class Video_Model:
    def __init__(self):
        self.Link = ""
        self.Type = ""
        self.quality = ""

    def ValidateLink(self, video_link):
        try:
            URL_Validator.url(video_link)

        except Exception:
            CTkMessagebox(title="Tube Save Found URL Error", 
                          message='Link entered is an invalid!\nRe-enter the video URL again',
                          font=CTkFont(size=13, weight='bold')
                          )