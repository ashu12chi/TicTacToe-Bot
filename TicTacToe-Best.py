# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:06:30 2019

@author: ASHUTOSH CHITRANSHI
"""

from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from copy import deepcopy
from gtts import gTTS
import os
import playsound

class Board:
 
  def __init__(self,other=None):
    self.player = 'X'
    self.opponent = 'O'
    self.empty = '.'
    self.size = 3
    self.fields = {}
    for y in range(self.size):
      for x in range(self.size):
        self.fields[x,y] = self.empty
    if other:
      self.__dict__ = deepcopy(other.__dict__)
 
  def move(self,x,y):
    board = Board(self)
    board.fields[x,y] = board.player
    (board.player,board.opponent) = (board.opponent,board.player)
    return board
 
  def __minimax(self, player):
    if self.won():
      if player:
        return (-1,None)
      else:
        return (+1,None)
    elif self.tied():
      return (0,None)
    elif player:
      best = (-2,None)
      for x,y in self.fields:
        if self.fields[x,y]==self.empty:
          value = self.move(x,y).__minimax(not player)[0]
          if value>best[0]:
            best = (value,(x,y))
      return best
    else:
      best = (+2,None)
      for x,y in self.fields:
        if self.fields[x,y]==self.empty:
          value = self.move(x,y).__minimax(not player)[0]
          if value<best[0]:
            best = (value,(x,y))
      return best
 
  def best(self):
    return self.__minimax(True)[1]

  def best1(self,player):
      if self.won():
          if player:
            return (-1,None)
          else:
            return (+1,None)
      elif self.tied():
          return (0,None)
      elif player:
          for x,y in self.fields:
              if self.fields[x,y]==self.empty:
                  return (2,(x,y))
        
        
        
 
  def tied(self):
    for (x,y) in self.fields:
      if self.fields[x,y]==self.empty:
        return False
    return True
 
  def won(self):
    for y in range(self.size):
      winning = []
      for x in range(self.size):
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
      if len(winning) == self.size:
        return winning
    for x in range(self.size):
      winning = []
      for y in range(self.size):
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
      if len(winning) == self.size:
        return winning
    winning = []
    for y in range(self.size):
      x = y
      if self.fields[x,y] == self.opponent:
        winning.append((x,y))
    if len(winning) == self.size:
      return winning
    winning = []
    for y in range(self.size):
      x = self.size-1-y
      if self.fields[x,y] == self.opponent:
        winning.append((x,y))
    if len(winning) == self.size:
      return winning
    return None
 
  def __str__(self):
    string = ''
    for y in range(self.size):
      for x in range(self.size):
        string+=self.fields[x,y]
      string+="\n"
    return string

class Start:
    
    def __init__(self):
        self.frame = Tk()
        self.frame.title('TicTacToe')
        self.frame.geometry("400x400")
        self.frame.resizable(width=False,height=False)
        self.b1 = Button(self.frame,text='Beginner',command=self.beginner)
        self.b2 = Button(self.frame,text='Advanced',command=self.advance)
        self.font = Font(family="Arial", size=32)
        self.l1=Label(self.frame,text="Welcome!!!",font=self.font)
        self.l1.place(x=50,y=20,height=50,width=300)
        self.b1.place(x=150,y=120,height=50,width=100)
        self.b2.place(x=150,y=190,height=50,width=100)
        language = 'en'
        mytext = "Game Starts Are you beginner or Advance level player"
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("test.mp3")
        playsound.playsound('test.mp3')
        os.remove('test.mp3')
        
    def mainloop(self):
        self.frame.mainloop()  
    def advance(self):
        language = 'en'
        mytext = "You think to be pro let's test"
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("test.mp3")
        playsound.playsound('test.mp3')
        os.remove('test.mp3')
        GUI().mainloop()
    def beginner(self):
        language = 'en'
        mytext = "OK Noob"
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("test.mp3")
        playsound.playsound('test.mp3')
        os.remove('test.mp3')
        Beginner().mainloop()

class Beginner:
    
    def __init__(self):
        self.frame = Tk()
        self.frame.title('TicTacToe')
        self.frame.resizable(width=False, height=False)
        self.font = Font(family="Arial", size=32)
        self.buttons = {}
        self.board = Board()
        for x,y in self.board.fields:
            handler = lambda x=x,y=y: self.move(x,y)
            button = Button(self.frame, command=handler, font=self.font, width=12, height=6)
            button.grid(row=y, column=x)
            self.buttons[x,y] = button
        handler = lambda: self.reset()
        button = Button(self.frame, text='reset', command=handler)
        button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky="WE")
        self.update()
    
    def move(self,x,y):
        self.frame.config(cursor="watch")
        self.frame.update()
        self.board = self.board.move(x,y)
        self.update()
        move = self.board.best1(True)[1]
        if move:
          self.board = self.board.move(*move)
          self.update()
        self.frame.config(cursor="")


    def update(self):
        for (x,y) in self.board.fields:
          text = self.board.fields[x,y]
          self.buttons[x,y]['text'] = text
          self.buttons[x,y]['disabledforeground'] = 'black'
          if text==self.board.empty:
            self.buttons[x,y]['state'] = 'normal'
          else:
            self.buttons[x,y]['state'] = 'disabled'
        winning = self.board.won()
        if winning:
          for x,y in winning:
            self.buttons[x,y]['disabledforeground'] = 'red'
          if self.buttons[winning[0]]['text'] == 'O':
              language = 'en'
              mytext = "Noob cannot even win at beginner, Try again"
              myobj = gTTS(text=mytext, lang=language, slow=False) 
              myobj.save("test.mp3")
              playsound.playsound('test.mp3')
              os.remove('test.mp3')
          else:
              language = 'en'
              mytext = "Still thinking to be Noob, Be pro!!!"
              myobj = gTTS(text=mytext, lang=language, slow=False) 
              myobj.save("test.mp3")
              playsound.playsound('test.mp3')
              os.remove('test.mp3')
          for x,y in self.buttons:
            self.buttons[x,y]['state'] = 'disabled'
        for (x,y) in self.board.fields:
          self.buttons[x,y].update()
          
    def mainloop(self):
        self.frame.mainloop()

    def reset(self):
        self.board = Board()
        self.update()
    

class GUI:
 
  def __init__(self):
    self.frame = Tk()
    self.frame.title('TicTacToe')
    self.frame.resizable(width=False, height=False)
    self.board = Board()
    self.font = Font(family="Arial", size=32)
    self.buttons = {}
    for x,y in self.board.fields:
      handler = lambda x=x,y=y: self.move(x,y)
      button = Button(self.frame, command=handler, font=self.font, width=12, height=6)
      button.grid(row=y, column=x)
      self.buttons[x,y] = button
    handler = lambda: self.reset()
    button = Button(self.frame, text='reset', command=handler)
    button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky="WE")
    self.update()
 
  def reset(self):
    self.board = Board()
    self.update()
 
  def move(self,x,y):
    self.frame.config(cursor="watch")
    self.frame.update()
    self.board = self.board.move(x,y)
    self.update()
    move = self.board.best()
    if move:
      self.board = self.board.move(*move)
      self.update()
    self.frame.config(cursor="")
 
  def update(self):
    for (x,y) in self.board.fields:
      text = self.board.fields[x,y]
      self.buttons[x,y]['text'] = text
      self.buttons[x,y]['disabledforeground'] = 'black'
      if text==self.board.empty:
        self.buttons[x,y]['state'] = 'normal'
      else:
        self.buttons[x,y]['state'] = 'disabled'
    winning = self.board.won()
    if winning:
      for x,y in winning:
        self.buttons[x,y]['disabledforeground'] = 'red'
    if winning and self.buttons[winning[0]]['text'] == 'O':
        language = 'en'
        mytext = "Still thinking to be pro, you are Noob!!!"
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("test.mp3")
        playsound.playsound('test.mp3')
        os.remove('test.mp3')
    else:
        if winning:
            language = 'en'
            mytext = "I accept, you are a master"
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("test.mp3")
            playsound.playsound('test.mp3')
            os.remove('test.mp3')
    if winning:
        for x,y in self.buttons:
            self.buttons[x,y]['state'] = 'disabled'
    for (x,y) in self.board.fields:
      self.buttons[x,y].update()
 
  def mainloop(self):
    self.frame.mainloop()

if __name__ == '__main__':
  Start().mainloop()