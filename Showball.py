from tkinter import *
import math
import winsound
import time
import random
    
def iniciar():
        showball()
    
    
def clique(event):
    print (event.x, event.y)

def desenhaBola(x1, y1, x2, y2, queCor, queTag):
    mapa.create_oval(x1, y1, x2, y2, \
                     fill=queCor,tags='bola')

def desenhaTexto(x, y, queTexto):
    mapa.create_text(x, y,text=queTexto, font=("Arial","32"),tags='texto', fill='red')

def showball():
    delta = 5
    x1 = 0
    R = random.randint(100, 255)
    G = random.randint(100, 255)
    B = random.randint(100, 255)
    diametro = 10
    while True:

        if x1 + diametro > 600:
            x1 = 600 -diametro
            delta = delta * -1

        if x1 < 0:
            x1 = 0
            delta = delta * -1           

        x2 = x1 + diametro

        y1 = 0
        x2 = x1 + diametro
        y2 = y1 + diametro
        desenhaBola(x1, y1, x2, y2, '#%02x%02x%02x' % (R,G,B),'bola')
        desenhaTexto(x2,y2,"SHOWBALL")
        mapa.update()
        time.sleep(0.03)
        mapa.delete('bola')
        mapa.delete('texto')
        x1 += delta
        diametro += delta
    
#INTERFACE PRINCIPAL
root=Tk()
root.title('Showball')
options=Frame(root,bg='black')
options.pack(fill='x',expand=True)
botao1=Button(options,text='GO!',command=iniciar)
botao1.pack(side='left',fill='x',expand=True)

mapa=Canvas(root,width=600,height=400)
mapa.pack()
mapa.bind("<ButtonRelease-1>", clique)
mainloop()
