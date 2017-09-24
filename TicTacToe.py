This is My Tic Tac Toe Game, Implemented in Python 3.
#To create the GUI, I have used the TkInter module for Python.

import tkinter as tk
from tkinter import ttk

StartFont =('verdana', 24)
NumFont = ('Verdana', 18)

#This is the main class, it contains a method that allows us to switch pages
class TicTacToe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        tk.Tk.wm_title(self, "Konstantin's Tic Tac Toe")
        
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage,GamePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky='nsew')
        
        self.show_frame(StartPage)
    
    #allows us to switch between pages    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
#This is our starting page, by clicking the button, the game is initialized
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Konstantin's Tic Tac Toe", font=StartFont)
        label.pack(padx=10,pady=10)
        basic = ttk.Button(self, text="Click To Begin",command=lambda:controller.show_frame(GamePage))
        basic.pack()


class GamePage(tk.Frame):
    #Keeps Track of Who's Turn it is
    Player = ""
    
    #If a Box is Empty, Inserts X or O and evaluates for winner.
    def boxclick(self,box,arg):
        if box["text"]== "":
            if arg=="X":
                self.TurnText["text"]="It is O's turn."
                box["text"]="X"
                GamePage.Player="O"
                self.checkwinner()
            else:
                self.TurnText["text"]="It is X's turn."
                box["text"]="O"
                GamePage.Player="X"
                self.checkwinner()
    
    #checks to see if there is a winner after the turn
    def checkwinner(self):
        if (self.box00["text"] == 'O' and self.box01["text"] == 'O' and self.box02["text"] == 'O' or
            self.box10["text"] == 'O' and self.box11["text"] == 'O' and self.box12["text"] == 'O' or
            self.box20["text"] == 'O' and self.box21["text"] == 'O' and self.box22["text"] == 'O' or
            self.box00["text"] == 'O' and self.box10["text"] == 'O' and self.box20["text"] == 'O' or
            self.box01["text"] == 'O' and self.box11["text"] == 'O' and self.box21["text"] == 'O' or
            self.box02["text"] == 'O' and self.box12["text"] == 'O' and self.box22["text"] == 'O' or
            self.box00["text"] == 'O' and self.box11["text"] == 'O' and self.box22["text"] == 'O' or
            self.box02["text"] == 'O' and self.box11["text"] == 'O' and self.box20["text"] == 'O'):
            self.TurnText["text"]="O Wins!!!"
        
        elif (self.box00["text"] == 'X' and self.box01["text"] == 'X' and self.box02["text"] == 'X' or
            self.box10["text"] == 'X' and self.box11["text"] == 'X' and self.box12["text"] == 'X' or
            self.box20["text"] == 'X' and self.box21["text"] == 'X' and self.box22["text"] == 'X' or
            self.box00["text"] == 'X' and self.box10["text"] == 'X' and self.box20["text"] == 'X' or
            self.box01["text"] == 'X' and self.box11["text"] == 'X' and self.box21["text"] == 'X' or
            self.box02["text"] == 'X' and self.box12["text"] == 'X' and self.box22["text"] == 'X' or
            self.box00["text"] == 'X' and self.box11["text"] == 'X' and self.box22["text"] == 'X' or
            self.box02["text"] == 'X' and self.box11["text"] == 'X' and self.box20["text"] == 'X'):
            self.TurnText["text"]="X Wins!!!"
        
        elif (self.box00["text"] != '' and
              self.box01["text"] != '' and
              self.box02["text"] != '' and
              self.box10["text"] != '' and
              self.box11["text"] != '' and
              self.box12["text"] != '' and
              self.box20["text"] != '' and
              self.box21["text"] != '' and
              self.box22["text"] != ''):
            self.TurnText["text"]="It's a Draw"
    
    #resets the game
    def resetgame(self):
        GamePage.Player = 'X'
        self.TurnText["text"]="It is X's turn."
        self.box00["text"]=""
        self.box01["text"]=""
        self.box02["text"]=""
        self.box10["text"]=""
        self.box11["text"]=""
        self.box12["text"]=""
        self.box20["text"]=""
        self.box21["text"]=""
        self.box22["text"]=""
            
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #This is just a greeting
        self.textbox = ttk.Label(self, text="Welcome To TicTacToe")
        self.textbox.grid(row=0,column=0,columnspan=3)
        
        GamePage.Player="X"
        
        #this text indicates whos turn it is or the result of the game.
        self.TurnText = ttk.Label(self, text="It is X's turn")                   
        self.TurnText.grid(row=1, column=0, columnspan=3)             
        
        #Defining The Squares for Tic Tac Toe
        self.box00 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box00,GamePage.Player))
        self.box00.grid(row=2, column=0)        

        self.box01 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box01,GamePage.Player))
        self.box01.grid(row=2, column=1)
        
        self.box02 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box02,GamePage.Player))
        self.box02.grid(row=2, column=2)
        
        self.box10 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box10,GamePage.Player))
        self.box10.grid(row=3, column=0)
        
        self.box11 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box11,GamePage.Player))
        self.box11.grid(row=3, column=1)        
        
        self.box12 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box12,GamePage.Player))
        self.box12.grid(row=3, column=2)
        
        self.box20 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box20,GamePage.Player))
        self.box20.grid(row=4, column=0)        
        
        self.box21 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box21,GamePage.Player))
        self.box21.grid(row=4, column=1)
    
        self.box22 = ttk.Button(self, text="", command=lambda:self.boxclick(self.box22,GamePage.Player))
        self.box22.grid(row=4, column=2)
        
        reset = tk.Button(self, text="Click to Reset Game", command=lambda:self.resetgame())
        reset.grid(row=6,column=0,columnspan=3)

app = TicTacToe()
app.mainloop()
