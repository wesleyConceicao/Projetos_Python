from tkinter import *
from threading import Thread
import time as tm



class digitalClock:

      # 
      # Constructor.
      #
      # @param master a TK to display the time.
      # @param secs number of seconds for time regressive counting.
      # @param time string for initializing the time. Just leave the default.
      #
      # 
      def __init__ ( self, master, secs = 0, time='' ):
            self.varStart = False
            self.master = master
            self.secs = secs
            if time!= '':
                  self.time = time
            else:
                  self.time = tm.strftime('%H:%M:%S')
            # relogio digital
            self.clock = Label(self.master, font=('times 20', 20, 'bold'))
            self.clock.pack(fill=BOTH, expand=1)
            self.clock['text'] = self.time

            # cronometro
            #self.cronometro = Entry(self.master, font= ('times 20', 20, 'bold'), bg='red')
            #self.cronometro.pack(fill=BOTH, expand=1, anchor=W)
            #self.cronometro.delete(0, END)
            #self.cronometro.insert(0, str(self.secs))

            # frame inferior
           # self.frame = Frame(self.master)
            #self.frame.pack(fill=BOTH, expand=1)

            # botão start (inicia contagem regressiva)
            #self.start = Button(self.frame, text = 'Start')
            #self.start.pack(side = LEFT, padx = 5)
            #self.start.bind('<ButtonRelease-1>', self.inicio_contagem)

            # botão plus30 (soma 30 segundos)
            #self.plus30 = Button(self.frame, text = '+30')
            #self.plus30.pack(side = LEFT, padx = 5)
            #self.plus30.bind('<ButtonRelease-1>', self.soma30)

            # botão pause (pausa contagem regressiva)
            #self.pause = Button(self.frame, text = 'Pause')
            #self.pause.pack(side = LEFT, padx = 5)
            #self.pause.bind('<ButtonRelease-1>', self.pausa_contagem)

      # 
      # Updates the clock display.
      #
      def tick(self):
          self.time = tm.strftime('%H:%M:%S')
          self.clock['text'] = self.time
          #calls itself every 1000 milliseconds
          #to update the time display as needed
          self.clock.after(1000, self.tick)

      # 
      # Starts a count down from the number of seconds set to zero.
      #
     # def tickDown(self):
           # if self.varStart and self.secs > 0:
            #      self.secs -= 1
            #      self.cronometro.delete(0, END)
            #      self.cronometro.insert(0, str(self.secs))
            #      if self.secs > 0:
            ##            self.cronometro.after(1000, self.tickDown)
           #       else:
            #            self.varStart = False
         #   else:
               #   self.varStart = False


      #def inicio_contagem(self, event):
       #     self.secs = int(self.cronometro.get())
        #    self.varStart = True
         #   self.cronometro.after(1000, self.tickDown)

      #def pausa_contagem(self, event):
       #     self.varStart = False

      #def soma30(self, event):
       #     self.secs += 30
        #    self.cronometro.delete(0, END)
         #   self.cronometro.insert(0, str(self.secs))


## Creates a new thread.
class makeThread (Thread):
      ## Constructor.
      #
      #  @param func function to be executed in this thread.
      #
      def __init__ (self,func):
          Thread.__init__(self)
          self.__action = func
          self.debug = False

      ## Obejct destructor.
      #  In Python, destructors are needed much less, because Python has
      #  a garbage collector that handles memory management.
      #  However, there are other resources to be dealt with, such as:        
      #  sockets and database connections to be closed, 
      #  files, buffers and caches to be flushed.
      #
      def __del__ (self):
          if ( self.debug ): print ("Thread end")

      ## Method representing the thread's activity.
      #  This method may be overriden in a subclass.
      #
      def run (self):
          if ( self.debug ): print ("Thread begin")
          self.__action()

def main ():
    root = Tk()
    d = digitalClock(root)
    t = makeThread(d.tick)
    t.start()
    mainloop()

if __name__ == '__main__':
    main()
