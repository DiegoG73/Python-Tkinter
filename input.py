from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')

e = Entry(root, width=60)
e.pack()
#Agregando texto al input:
e.insert(0, 'Ingresa texto')


#Creando un botón para guardar el texto y generar interactividad con la aplicación:
def click():
    texto = e.get()
    textVariable.set(texto)
    valor = textVariable.get()
    print(valor)
    # l = Label(root, text=texto)
    # l.pack()
    # #Configurando el texto del input para eliminarse cuando clickeemos:
    e.delete(0, END)
    #l.configure(text=texto)


btn = Button(root, text='CLick', command=click)
btn.pack()

textVariable = StringVar()
l = Label(root, textvariable=textVariable)
l.pack()

root.mainloop()