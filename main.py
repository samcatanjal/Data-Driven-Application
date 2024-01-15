from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

class api_handling:
    def get_data(self, num):
        response = requests.get('https://api.potterdb.com/v1/books')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()['data'][num]['attributes']
        title = data['title']
        cover = data['cover']
        bg_image = self.load_image(cover)
        return bg_image


    def load_image(self, cover):
        cover_response = requests.get(cover)
        image = Image.open(BytesIO(cover_response.content))
        image = image.resize((300, 350)) 
        bg_image = ImageTk.PhotoImage(image)
        return bg_image

api = api_handling()

class BasePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(width=600, height=650, relx=0.5, rely=0.5, anchor=CENTER)

class BaseFrame(Frame):
    def __init__(self, parent, bg_image=None):
        super().__init__(parent)

        self.place(width=300, height=350, relx=0.5, rely=0.45, anchor=CENTER)

        if bg_image:
            self.bg_image = bg_image
            self.background_label = Label(self, image=bg_image)
            self.background_label.place(relwidth=1, relheight=1)

class FirstPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data(0) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)

        button = Button(self, text="Next", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.second))
        button.place(relx=0.9, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)

class SecondPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data(1) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)

        button = Button(self, text="Back", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.first))
        button.place(relx=0.1, rely=0.1, anchor=CENTER)

        button = Button(self, text="Next", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.third))
        button.place(relx=0.9, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)

class ThirdPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data(2) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)

        button = Button(self, text="Back", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.second))
        button.place(relx=0.1, rely=0.1, anchor=CENTER)

        button = Button(self, text="Next", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.fourth))
        button.place(relx=0.9, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)

class FourthPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data(3) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)


        button = Button(self, text="Back", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.third))
        button.place(relx=0.1, rely=0.1, anchor=CENTER)

        button = Button(self, text="Next", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.fifth))
        button.place(relx=0.9, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)

class FifthPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data(4) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)

        button = Button(self, text="Back", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.fourth))
        button.place(relx=0.1, rely=0.1, anchor=CENTER)

        button = Button(self, text="Next", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.sixth))
        button.place(relx=0.9, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)

class SixthPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data(5) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)

        button = Button(self, text="Back", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.fifth))
        button.place(relx=0.1, rely=0.1, anchor=CENTER)

        button = Button(self, text="Next", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.seventh))
        button.place(relx=0.9, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)

class SeventhPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        bg_image = api.get_data( 6) # retrieving image data
        if bg_image:
            Label(self, image=bg_image).place(relx=0.5, rely=0.5, anchor=CENTER)

    
        button = Button(self, text="Back", width=10, font=("Montserrat", 12), command=lambda: parent.show_page(parent.sixth))
        button.place(relx=0.1, rely=0.1, anchor=CENTER)

        self.main = BaseFrame(self, bg_image)

        view = Button(self, text="Select", width=30, font=("Montserrat", 12))
        view.place(relx=0.5, rely=0.85, anchor=CENTER)


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Harry Potter Books')
        self.geometry('700x750')
        self.resizable(0,0)
        self['bg'] = '#212121'

        self.first = FirstPage(self)
        self.second = SecondPage(self)
        self.third = ThirdPage(self)
        self.fourth = FourthPage(self)
        self.fifth = FifthPage(self)
        self.sixth = SixthPage(self)
        self.seventh = SeventhPage(self)

        self.show_page(self.first)

        self.mainloop()

    def raise_frame(self, frame):
        frame.tkraise()

    def show_page(self, page):
        self.raise_frame(page)

App()