import tkinter.messagebox
from tkinter import *
form = Tk()
form.geometry('350x210')
form.title('Register')


def getvals():
    tkinter.messagebox.showinfo("Success", "Registration Complete")


Label(form, text="Yandalar's Registration Form", font="Monserrat 14").grid(row=0, column=3)
Label(form, text="", font="Monserrat 6").grid(row=1, column=3)

username = Label(form, text='Username')
name = Label(form, text='Name')
email = Label(form, text='E-Mail')
phone = Label(form, text='Phone')
country = Label(form, text='Country')

username.grid(row=2, column=2)
name.grid(row=3, column=2)
email.grid(row=4, column=2)
phone.grid(row=5, column=2)
country.grid(row=6, column=2)

usernamevalue = StringVar
namevalue = StringVar
emailvalue = StringVar
phonevalue = StringVar
countryvalue = StringVar
checkvalue = IntVar

usernameentry = Entry(form, textvariable = usernamevalue)
nameentry = Entry(form, textvariable = namevalue)
emailentry = Entry(form, textvariable = emailvalue)
phoneentry = Entry(form, textvariable = phonevalue)
countryentry = Entry(form, textvariable = countryvalue)

usernameentry.grid(row=2, column=3)
nameentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
phoneentry.grid(row=5, column=3)
countryentry.grid(row=6, column=3)

rememberbutton = Checkbutton(text='Remember me?', variable = checkvalue)
rememberbutton.grid(row=7, column=3)

Button(text='Submit', command=getvals).grid(row=8, column=3)

form.mainloop()