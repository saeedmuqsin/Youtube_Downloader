
from packages.controller import Controller
from packages.model import Video_Model
from packages.view import Youtube_interface
import threading

# creating an instance of the controller
def Main_app():
    Model = Video_Model()
    View = Youtube_interface(Model)
    controller = Controller(Model, View)

    # // application start running 
    View.update()
    View.mainloop()

if __name__== "__main__":
    Main_app()