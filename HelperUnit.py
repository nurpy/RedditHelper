import praw

from gtts import gTTS
import textwrap
import playsound
import os


import glob
from tkinter import *

import tkinter as tk
import requests
import pygame
import re


import PIL.ImageTk
import PIL.Image

postNumber=0
g=0
totalarr=[]       


def main():
    def deleteMusic():
       
        global postNumber
        totalarr=os.getcwd()
       
        for f in totalarr:
            if f.find("reddit") != -1:
                os.remove(f)
    
    
    def speak(message,m):
          g = gTTS(message, lang = 'en')


          file=f'reddit{m}.mp3'
          totalarr.append(file)
          print(file)
          g.save(file)
         
          pygame.mixer.music.load(file)
          pygame.mixer.music.play(loops=0)

   
        

    
    def showImage(file_name,val):
            def deleteImage():
                label1.destroy()
            
            global g
            
            g=g+1
            
            
           
            
            

            load= PIL.Image.open(file_name)

            load.thumbnail((1920, 1080))

            test = PIL.ImageTk.PhotoImage(load)

            label1 = Label(image=test)
            label1.image = test
            label1.place(x=0, y=0)
            
            Display2 = Button(root, height = 5,
                     width = 10,
                     text ="Delete Image",
                     command = lambda:deleteImage(),font=("times new roman",10,"bold"))
            Display2.place(x=75,y=0)
            
          
                
            

    def getImage(submission):
        url = (submission.url)
        file_name = url.split("/")
        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        file_name = file_name[-1]
        if "." not in file_name:
            file_name += ".jpg"
        print(file_name)
        r = requests.get(url)
        tempFile= file_name
            
        with open(tempFile ,"wb") as f:
            f.write(r.content)
        f.close()    
        if file_name != '.jpg':
            
            
            Display1 = Button(root, height = 5,
                     width = 10,
                     text ="view Image",
                     command = lambda:showImage(tempFile,0),font=("times new roman",10,"bold"))
            Display1.place(x=0,y=0)
            
            
            
            
            
        
           
    
    def start(desiredLevel,INPUT):
        
        reddit = praw.Reddit(client_id='CLIENT_ID',
                             client_secret='client_secret',
                             username='username',
                             password='password',
                             user_agent='user_agent')
        subreddit = reddit.subreddit(INPUT)
        hot_confessions = subreddit.hot(limit=100)
        m=0
        for submission in hot_confessions:
            
            x=submission.title+(submission.selftext.lower())
            c= (textwrap.fill(submission.title,50) + "\n" + "\n" + textwrap.fill(x,50))
            
 
            
            if m==desiredLevel:
                getImage(submission)
                Output.insert(END,c)
                return c
            m=m+1
        
    
    
    
    
    
    
    
    def Take_input():
        pygame.mixer.music.stop()

        #deleteMusic()
        delete()
        INPUT = inputtxt.get("1.0", "end-1c")
        print("INPUT")
        global postNumber
        print(postNumber)
        c=start(postNumber,INPUT)
        speak(c,postNumber)
        postNumber+=1
        
        
        

    def delete():
        print("here")
        Output.delete('1.0',END)
    
    
    
    
    
    deleteMusic()
    root = Tk()
    root.state('zoomed')
    root.title(" KI5KDF ")
    pygame.mixer.init()
    
    l = Label(text = "What subreddit would you like to hear from? ",font=("times new roman",45,"bold"))
    inputtxt = Text(root, height = 2,width = 1280,bg = "light yellow")

    Output = Text(root, height = 600,
                  width = 1280,
                  bg = "light cyan",
                  font=("times new roman",50,"bold"))

    Display = Button(root, height = 1,
                     width = 500,
                     text ="Next Post",
                     command = lambda:Take_input(),font=("times new roman",45,"bold"))

    l.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()

    mainloop()

if __name__ == "__main__":
    main()    
    

