from tkinter import *

root = Tk()
root.title('Frame')

#                 Agregando márgenes dentro del frame:
# frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=5)


#Agregando un marco(frame) sin texto:
#frame = LabelFrame(root, padx=10, pady=10, borderwidth=10)


#Creando un frame sin marco
frame = Frame(root, padx=10, pady=10, borderwidth=10)


#Con padx colocamos márgenes laterales y pady márgenes vertivales(arriba y abajo)
frame.pack(padx=50, pady=50)


l = Label(frame, text='Estoy dentro de un Frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()