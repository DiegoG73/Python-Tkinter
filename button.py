from tkinter import *

root = Tk()
root.title('Hola mundo')

l = Label(root, text='Hola mundo')
#Agregando funcionalidad a nuestro botón
def click():
    l.pack()

btn = Button(root, text='Click me', command=click, fg='#000', background='purple')


btn.pack()

root.mainloop()