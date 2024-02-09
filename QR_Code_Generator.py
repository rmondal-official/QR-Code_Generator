# importing
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle


# Designing GUI
a_root = Tk()
a_root.geometry("550x300")
a_root.title("Qrcode Generator")
a_root.resizable(False, False)
# a_root.wm_iconbitmap("your_icon_image.ico")
style = ThemedStyle()  # using ttkthemes
style.set_theme('adapta')
a_root.config(bg="skyblue")


def click():  # defining function of Click button
    if cat.get() == 1:
        url = pyqrcode.create(show.get())
        url.png("now.png", scale=1)
        url.show()
    else:
        url = pyqrcode.create(show.get())
        url.show()


show = StringVar()
cat = IntVar()


Label(a_root, bg='skyblue').pack()
f = ttk.Frame(a_root, borderwidth=3, relief=SUNKEN)
f.pack()
ttk.Label(f, text=' QRCode Generator ', font="broadway 30 italic").pack()
Label(a_root, bg="skyblue").pack()


f = Frame(a_root, bg="skyblue")
f.pack()
Label(f, text="Enter url / number :  ", font="Calibri 15 italic", bg="skyblue").pack(side=LEFT)
ttk.Entry(f, textvariable=show, font="Calibri 14 italic", width=30).pack(side=LEFT)
Label(f, text="     ", bg="skyblue").pack()


f = Frame(a_root, bg="skyblue")
f.pack()
Checkbutton(f, text="To save the QRCode image as png file", variable=cat, bg="skyblue", font="calibri 13 italic").pack()
Button(f, text="Click Me", font="calibri 13 italic", command=click).pack(ipadx=40)


a_root.mainloop()
# Completed