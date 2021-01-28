import tkinter as tk
from tkinter import *
from tkinter import ttk 
import adafruit_dht as DHT
import gpiozero
import adafruit_dht
import board
import time


class GraugeApp(tk.Tk):
    
    
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "JOHNS MAN CAVE")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage, NextPage):
            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row=0,column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame= self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        self.tempSen = adafruit_dht.DHT11(board.D17)
        self.relay = gpiozero.LED(18)
        #self.actualTemp = IntVar()
        #self.actualTemp.set(self.tempSen.temperature)
        print(self.tempSen.temperature,"starting Temp")
        self.pack(fill=BOTH, expand=1)
        self.quitButton = Button(self, text="QUIT", command=self.client_exit)
        self.quitButton.grid(row=1,column=1)
        self.relayButton = Button(self, text="relay", command=self.toggleRelay)
        self.relayButton.grid(row=1, column=2)
        self.lable = Label(self,text="TEMP:")
        self.lable.grid(row=1, column=3)
        self.lableTemp = Label(self, text="start")
        self.lableTemp.grid(row=1, column=4)
        self.temp = 0 
        self.onUpdate()
        
    def onUpdate(self):
        try:
            self.temp = self.tempSen.temperature
        except RuntimeError as i:
            print("HANDELED", i)

        self.lableTemp.configure(text=self.temp)
        print(self.temp,"still trying")
        self.after(2000, self.onUpdate)

    def client_exit(self):
        exit()

    def toggleRelay(self):
        if self.relay.value == 0:
            self.relay.on()
        else: self.relay.off()
            
    def tempSend(self):
        return self.tempSen.temperature


class NextPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        pass


app = GraugeApp()

app.mainloop()
