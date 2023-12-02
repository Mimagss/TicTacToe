from tkinter import *
from Spielbrett import Spielbrett

class TicTacToe:
    def __init__(self):
        self.brett = Spielbrett()
        self.aktSpieler = "X"
        self.fertig = False
        self.gewinner = ""
        self.gültigerZug = 1
        self.Info = ""

    def bestimmeReiheSpalte(self, event):
        buttonCoords = {b1 : (0,0), b2 : (0,1), b3: (0,2),
                     b4 : (1,0), b5 : (1,1), b6: (1,2),
                     b7 : (2,0), b8: (2,1), b9: (2,2)}
        return buttonCoords[event.widget]

    def gewonnen(self):
        zeile0 = self.brett.gib(0,0) == self.brett.gib(0,1) and self.brett.gib(0,1) == self.brett.gib(0,2) and self.brett.gib(0,0) != " "
        zeile1 = self.brett.gib(1,0) == self.brett.gib(1,1) and self.brett.gib(1,1) == self.brett.gib(1,2) and self.brett.gib(1,0) != " "
        zeile2 = self.brett.gib(2,0) == self.brett.gib(2,1) and self.brett.gib(2,1) == self.brett.gib(2,2) and self.brett.gib(2,0) != " "
        spalte0 = self.brett.gib(0,0) == self.brett.gib(1,0) and self.brett.gib(1,0) == self.brett.gib(2,0) and self.brett.gib(0,0) != " "
        spalte1 = self.brett.gib(0,1) == self.brett.gib(1,1) and self.brett.gib(1,1) == self.brett.gib(2,1) and self.brett.gib(0,1) != " "
        spalte2 = self.brett.gib(0,2) == self.brett.gib(1,2) and self.brett.gib(1,2) == self.brett.gib(2,2) and self.brett.gib(0,2) != " "
        diag1 = self.brett.gib(0,0) == self.brett.gib(1,1) and self.brett.gib(1,1) == self.brett.gib(2,2) and self.brett.gib(0,0) != " "
        diag2 = self.brett.gib(0,2) == self.brett.gib(1,1) and self.brett.gib(1,1) == self.brett.gib(2,0) and self.brett.gib(0,2) != " "
        return zeile0 or zeile1 or zeile2 or spalte0 or spalte1 or spalte2 or diag1 or diag2

    def onClick(self,event):
        if self.fertig == False:
            reihe, spalte = self.bestimmeReiheSpalte(event)

            if self.brett.gib(reihe, spalte) == ' ':
                self.brett.setze(reihe, spalte, self.aktSpieler)
                guiKachel = event.widget
                print(guiKachel)
                guiKachel.config(text = self.aktSpieler) 
                print(self.brett)
                print(self.gültigerZug)
                self.fertig = self.gewonnen()

                if self.fertig:
                    self.gewinner = self.aktSpieler
                    self.Info= ("gewinner ist", self.gewinner)
                    labelText = self.Info
                    label.configure(text=labelText)

                elif self.gültigerZug == 9:
                    self.fertig = True
                    self.Info = ("Remis")
                    labelText = self.Info
                    label.configure(text=labelText)
                                   
                elif self.aktSpieler == "X":
                    self.aktSpieler = "O"
                    self.Info = "O"
                    labelText = self.Info
                    label.configure(text=labelText)
                    self.gültigerZug += 1
                else:
                    self.aktSpieler = "X"
                    self.Info = "X"
                    labelText = self.Info
                    label.configure(text=labelText)
                    self.gültigerZug += 1

ttt = TicTacToe()  
dieGUI = Tk()
dieGUI.title("TicTacToe")
dieGUI.geometry("900x950")
labelText = ""
label = Label(dieGUI,text=labelText)

b1 = Button(master=dieGUI)
b2 = Button(master=dieGUI)
b3 = Button(master=dieGUI)
b4 = Button(master=dieGUI)
b5 = Button(master=dieGUI)
b6 = Button(master=dieGUI)
b7 = Button(master=dieGUI)
b8 = Button(master=dieGUI)
b9 = Button(master=dieGUI)

b1.place(x=0, y=0, width=300, height=300)
b2.place(x=300, y=0, width=300, height=300)
b3.place(x=600, y=0, width=300, height=300)
b4.place(x=0, y=300, width=300, height=300)
b5.place(x=300, y=300, width=300, height=300)
b6.place(x=600, y=300, width=300, height=300)
b7.place(x=0, y=600, width=300, height=300)
b8.place(x=300, y=600, width=300, height=300)
b9.place(x=600, y=600, width=300, height=300)

label.place(x=0, y=900, width=900, height=50)

b1.bind('<Button>', ttt.onClick)
b2.bind('<Button>', ttt.onClick)
b3.bind('<Button>', ttt.onClick)
b4.bind('<Button>', ttt.onClick)
b5.bind('<Button>', ttt.onClick)
b6.bind('<Button>', ttt.onClick)
b7.bind('<Button>', ttt.onClick)
b8.bind('<Button>', ttt.onClick)
b9.bind('<Button>', ttt.onClick)


dieGUI.mainloop()
