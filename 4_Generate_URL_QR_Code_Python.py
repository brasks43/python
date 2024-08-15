#I used this to generate QR codes to embed into survey letters or emails
#You can just as easily import a dataframe and loop through individual URLs for respondents that have individualized survey links

import qrcode
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import Tk

Tk().withdraw()
# Link for website
input_data = input('Please enter the Qualtrics URL and hit Enter: ')

#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

img.save('qualtrics_url.png') #Change this as needed
