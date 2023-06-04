
from tkinter import*
from math import*
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("300x400")
ancho_boton = 1
alto_boton = 2

#creamos nuestros botones
boton0 = Button(ventana,text="0", width= ancho_boton,heigth=alto_boton).place(x=17,y=180)

Salida = Entry(ventana,font=("arial",20, 'bold'),width=22, bd= 20, insertwidth=4, bg='powder blue', justify = 'rigth').place(x=10, y=60)