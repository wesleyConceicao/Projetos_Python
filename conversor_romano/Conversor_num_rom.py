from _03c_int2roman import int2roman
from _03a_roman2int import roman2int
from tkinter import *

class janelaRomanos(Tk):
    def __init__(self):
        super(janelaRomanos, self).__init__()


        #janela principal:
        self.title("Romano")
        self.geometry("350x200")
        
        #frame topo
        self.frameTopo = Frame(self)
        self.frameTopo.pack(side=TOP, fill="x")
        
        #label romanos
        self.label1 = Label(self.frameTopo, text="Romanos:")
        self.label1.pack(side = RIGHT)

        #label decimal
        self.label1 = Label(self.frameTopo, text="Decimal:")
        self.label1.pack(side = LEFT)

        #frame topo
        self.frameTopo2 = Frame(self)
        self.frameTopo2.pack(side=TOP, fill="x")

        #entry romanos
        self.entryRomanos = Entry(self.frameTopo2)
        self.entryRomanos.pack(side=RIGHT)

        #entry decimal
        self.entryDecimal = Entry(self.frameTopo2)
        self.entryDecimal.pack(side=LEFT)

        #frame inferior esquerdo
        self.frameInferiorEsquerdo = Frame(self)
        self.frameInferiorEsquerdo.pack(side=LEFT)

        #button 2roman
        self.button2roman = Button(self.frameInferiorEsquerdo, text="Romano--->")
        self.button2roman.bind("<ButtonRelease-1>", self.toRoman)
        self.button2roman.pack(side=LEFT, padx=15)

        #frame inferior direito
        self.frameInferiorDireito = Frame(self)
        self.frameInferiorDireito.pack(side=RIGHT)

        #button 2int
        self.button2int = Button(self.frameInferiorDireito, text="<---Decimal")
        self.button2int.bind("<ButtonRelease-1>", self.toInt)
        self.button2int.pack(side=RIGHT, padx=15)

        #label imagem
        self.soldier = PhotoImage(file="roma.jpg")
        self.soldier = self.soldier.subsample(4,4)
        self.image = Label(self,image=self.soldier)
        self.image.pack()
        
    def toRoman(self, event):
        numInt = self.entryDecimal.get()
        try:
            numInt = int(numInt)
            numRoman = int2roman(numInt)
        except:
            numRoman = "Entrada inválida"
        self.entryRomanos.delete(0, END)
        self.entryRomanos.insert(0,numRoman)
        
    def toInt(self, event):
        numRoman = self.entryRomanos.get()
        try:
            numInt = roman2int(numRoman)
        except:
            numInt = "Entrada inválida"
        self.entryDecimal.delete(0, END)
        self.entryDecimal.insert(0,numInt)

    
if __name__ == "__main__":
    a = janelaRomanos()
    a.mainloop()
