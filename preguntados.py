# Hacer un juego de preguntas y respuestas
"""from tkinter import*
class Figuras(Tk):
    def __init__(self , *args,**kwargs):
        super(). __init__(*args, **kwargs)
        self.geometry("420x420")
        self.circulo()
    def create_canvas(self,x,y):
        self.canvas = Canvas(self,width=500, height=700)
        self.canvas.place(x=x, y=y)
    def circulo(self):
        self.create_canvas(0,0)
        self.canvas.create_oval(100,100,2000,2000, width=4, fill="cyan")
if __name__ == "__main__":
    app=Figuras()
    app.mainloop()"""
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)