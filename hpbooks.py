import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Harry Potter Books')
        self.geometry('700x750')
        self.resizable(0,0)

        self.one = FirstPage(self) # putting all pages in app
        self.two = SecondPage(self)
        self.three = ThirdPage(self)
        self.four = FourthPage(self)
        self.five= FifthPage(self)
        self.six = SixthPage(self)
        self.seven = SeventhPage(self)

        self.show_page(self.one) # initially shows first page

    def raise_frame(self, frame): # frame switching using tkraise
        frame.tkraise()

    def show_page(self, page): # indicate which page to raise (for button command purposes)
        self.raise_frame(page)

class APIHandling:
    @staticmethod # acts as a function that can be used in other classes (without calling instance)
    def getData():
        url = 'https://api.potterdb.com/v1/books' # url of api
        response = requests.get(url)
        data = response.json() # reads data as json file
        return data # saves data
    
    @staticmethod
    def get_image(url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img # saves image

class BasePage(tk.Frame): # template page
    def __init__(self, parent):
        super().__init__(parent)

        self['bg'] = "#212121"
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=700, height=750) # fills whole window

    def display_img(self, img_url): # display image settings
        img = APIHandling.get_image(img_url)
        img = img.resize((300, 350))
        img = ImageTk.PhotoImage(img)

        img_label = tk.Label(self, image=img)
        img_label.image = img
        img_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

class PopUp(tk.Toplevel): # pop up window
    def __init__(self, parent, data):
        super().__init__(parent)

        self.title('Book Details')
        self.geometry('750x750')
        self.resizable(0,0)
        self['bg'] = '#333333'

        self.data = data # gets data from parent window (pages)

        self.display_details()
    def display_details(self):
        title = self.data['attributes']['title'] # fetching each info
        author = self.data['attributes']['author']
        summary = self.data['attributes']['summary']
        date = self.data['attributes']['release_date']
        pages = self.data['attributes']['pages']
        dedication = self.data['attributes']['dedication']

        title_label = tk.Label(self, text=f'{title}', font=("Montserrat", 16), bg='#333333', fg='#FFFFFF') # puting info into labels
        author_label = tk.Label(self, text=f'{author}', font=("Montserrat", 12), bg='#333333', fg='#FFFFFF')
        summary_label = tk.Label(self, text=f'{summary}', font=("Montserrat", 12), bg='#333333', fg='#FFFFFF', wraplength=500)
        date_label = tk.Label(self, text=f'Release Date: {date}', font=("Montserrat", 12), bg='#333333', fg='#FFFFFF')
        pages_label = tk.Label(self, text=f'Pages: {pages}', font=("Montserrat", 12), bg='#333333', fg='#FFFFFF')
        dedication_label = tk.Label(self, text=f'{dedication}', font=("Montserrat", 12), bg='#333333', fg='#FFFFFF', wraplength=600)

        title_label.pack(side='top', anchor='w', padx=20, pady=40) # widget layout
        author_label.pack(side='bottom', anchor='center', pady=25)
        summary_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        date_label.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
        pages_label.place(relx=0.85, rely=0.8, anchor=tk.CENTER)
        dedication_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

 
class FirstPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData() # data fetching

        next = tk.Button(self, text="Next", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.two))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][0]))
        
        next.place(relx=0.85, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)
        
        self.display() # display image

    def showbook(self, book): # function for opening pop up window
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][0]['attributes']['cover'] # gets image from api image url
        self.display_img(cover)

class SecondPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData()

        back = tk.Button(self, text="Back", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.one))
        next = tk.Button(self, text="Next", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.three))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][1]))

        next.place(relx=0.85, rely=0.1, anchor=tk.CENTER)
        back.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)

        self.display()

    def showbook(self, book):
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][1]['attributes']['cover']
        self.display_img(cover)

class ThirdPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData()

        back = tk.Button(self, text="Back", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.two))
        next = tk.Button(self, text="Next", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.four))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][2]))

        next.place(relx=0.85, rely=0.1, anchor=tk.CENTER)
        back.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)

        self.display()

    def showbook(self, book):
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][2]['attributes']['cover']
        self.display_img(cover)

class FourthPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData()

        back = tk.Button(self, text="Back", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.three))
        next = tk.Button(self, text="Next", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.five))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][3]))

        next.place(relx=0.85, rely=0.1, anchor=tk.CENTER)
        back.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)

        self.display()

    def showbook(self, book):
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][3]['attributes']['cover']
        self.display_img(cover)

class FifthPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData()

        back = tk.Button(self, text="Back", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.four))
        next = tk.Button(self, text="Next", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.six))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][4]))

        next.place(relx=0.85, rely=0.1, anchor=tk.CENTER)
        back.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)

        self.display()

    def showbook(self, book):
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][4]['attributes']['cover']
        self.display_img(cover)

class SixthPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData()

        back = tk.Button(self, text="Back", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.five))
        next = tk.Button(self, text="Next", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.seven))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][5]))

        next.place(relx=0.85, rely=0.1, anchor=tk.CENTER)
        back.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)

        self.display()

    def showbook(self, book):
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][5]['attributes']['cover']
        self.display_img(cover)

class SeventhPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = APIHandling.getData()

        back = tk.Button(self, text="Back", font=('Montserrat', 14), width=10, bg='#333333', fg='#fff', command=lambda: parent.show_page(parent.six))
        select = tk.Button(self, text="Select", font=('Montserrat', 16), width=20, bg='#333333', fg='#fff', command=lambda: self.showbook(self.data['data'][6]))

        back.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        select.pack(side="bottom", pady=150)

        self.display()

    def showbook(self, book):
        pop_up = PopUp(self, book)

    def display(self):
        cover = self.data['data'][6]['attributes']['cover']
        self.display_img(cover)

app = App() # making class as an app/window
app.mainloop() # run