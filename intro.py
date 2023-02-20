from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')

l1 = Label(root, text='Hola mundo, este es mi primera etiqueta!')
l2 = Label(root, text='Ciao mundo, este es mi segunda etiqueta!')

#Imprimiéndolo con grilla en vez de con pack:
l1.grid(row = 0, column = 0)
l2.grid(row = 0, column = 1)

root.mainloop()