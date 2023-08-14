# view.py present a user interface of the application

from customtkinter import *
from PIL import Image
from .model import Video_Model

class Youtube_interface(CTk):
    def __init__(self, model:Video_Model):
        CTk.__init__(self)

        self.title('Tube Save')
        self.iconbitmap(r"packages\images\Youtube-icon.ico")
        self.geometry("650x650") # it specify the size of the interface
        self.resizable(False, False) # show that if the window is resizable

        # // video model that holds details holds details about the video
        self.video = model

        # sets the theme of the interface to dark mode
        set_appearance_mode("dark")

        # sets the background image of the interface
        bg_image = CTkImage(Image.open(r'packages\images\background_image.jfif'), size=(1500, 1000))
        interface_bg = CTkLabel(master=self, image=bg_image).pack()

        # big container that contains other widgets
        main_container = CTkFrame(master=interface_bg, width=550, height=620,)
        main_container.place(rely=0.5, relx=0.5, anchor= CENTER)

        #// -- >  video url entry widget
        CTkLabel(main_container,text='Stream URL :', font=CTkFont(size=15)).place(x=30, y=30)
        self.video.Link = StringVar()
        video_url_entry = CTkEntry(main_container,width=400,height=40, placeholder_text="Type the video URL here.", textvariable=self.video.Link).place(x=120,y=25)

        # -- > paste button >>
        pastebtn_img = CTkImage(Image.open(r"packages\images\pastebtnimg.png"), size=(20, 20))
        self.pasteBtn = CTkButton(master=main_container,text="Paste ", width=75, height=10, image=pastebtn_img, fg_color='#66C3FF', hover_color="#66C3FF")
        self.pasteBtn.place(x=430, y=30.5)

        # ===> select the video type that you want in the option menu widget
        self.video.Type = StringVar()
        CTkLabel(main_container,text="Type: ", font=CTkFont(size=15, weight='bold')).place(x=30, y=100)
        type_option_menu = CTkOptionMenu(main_container, width=150,values=['Video', 'Audio'],variable=self.video.Type,dropdown_hover_color='white')
        type_option_menu.place(x=85, y=100)

        #=== > select the quality of the video you want
        self.video.quality =  StringVar()
        CTkLabel(main_container, text='Quality: ', font=CTkFont(size=15)).place(x=270, y=100)
        quality_video_menu = CTkOptionMenu(main_container, width=170, values=['240p', '360p','480p', '720p', '1080p'], variable=self.video.quality)
        quality_video_menu.place(x = 340, y=100)

        # === > Takes the directionary location where video is going to be saved
        self.location = ""
        CTkLabel(main_container, text="Save To: ", font=CTkFont(size=15, weight='bold')).place(x=30, y=170)
        self.directory_btn=CTkButton(main_container, text="Choose location", width=300, fg_color='#0EAD69', hover_color='#8B8B89')
        self.directory_btn.place(x=150, y=170)

        # ===> Download button if a user presses video starts downloading 
        download_image = CTkImage(Image.open(r'packages\images\download-icon.png'), size=(50, 40))
        self.download_button = CTkButton(main_container,text="Download", height=45,width=200,fg_color='#0EAD69', hover_color='#8B8B89', font=CTkFont(size=15, weight='bold'), image=download_image)
        self.download_button.place(x=50, y=250)
        
        # // canceling button widget // 
        closed_image = CTkImage(Image.open(r'packages\images\close-icon.png'), size=(30, 40))
        self.cancel_button = CTkButton(main_container,text="Cancel", height=45, width=200, fg_color='#FB3640', hover_color='#8B8B89',image=closed_image,font=CTkFont(size=15, weight='bold'))
        self.cancel_button.place(x=300, y=250)

        CTkLabel(main_container, text="Stream Details: ", font=CTkFont(size=14)).place(x=40,y=340)
        self.stream_details = CTkTextbox(main_container, width=440, height=140,font=CTkFont(size=12))
        self.stream_details.place(x = 40, y=370)

        # --> Disclaimer note
        message = "PLEASE TAKE NOTICE !!!. Don't try to click the Cancel Button when download is start.\n Download of video start after clicking the Download Button.You will be notify \nafter a successful download."
        CTkLabel(main_container,text=message,font=CTkFont(weight='bold', size=11)).place(x=20, y=520)
        
        # developer of interface 
        CTkLabel(main_container, text="Developed By Saeed Muhsin.", font = CTkFont(family='Work Sans', size = 15, weight='bold',  slant="italic")).place(x=170,y=570)
        


    # == > function that pastes the URL in the stream entry
    def Paste_func(self, callback:callable):
        self.pasteBtn.bind("<Button-1>", callback)

    # == > function retrieves the directory selected by the user where streams is going be saved..
    def SelectDirectory(self, callback:callable):
        self.directory_btn.bind("<Button-1>", callback)

    # == > function that cancel or closes the windows 
    def Cancel_window(self, callback):
        self.cancel_button.bind("<Button-1>", callback)

    # == > function called to start downloading youtube stream
    def StartDownload(self, callback:callable):
        self.download_button.bind("<Button-1>",callback)

