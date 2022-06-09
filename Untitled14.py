import praw

from gtts import gTTS
import textwrap
import playsound
import os


import glob
from tkinter import *
#from tkinter import ttk
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
        #os.remove('C:/Users/jabio/Documents/LTspiceXVII/reddit0.mp3')
        global postNumber
        files = glob.glob(f'C:/Users/jabio/Documents/LTspiceXVII/')
        for f in totalarr:
            os.remove(f'C:/Users/jabio/Documents/LTspiceXVII/reddit{postNumber}.mp3')
    
    
    def speak(message,m):
          g = gTTS(message, lang = 'en')#, tld = 'com.au')


          file=f'C:/Users/jabio/Documents/LTspiceXVII/reddit{m}.mp3'
          totalarr.append(file)
          print(file)
          g.save(file)
          #playsound.playsound(file)
          pygame.mixer.music.load(file)
          pygame.mixer.music.play(loops=0)

   
        

    
    def showImage(file_name,val):
            def deleteImage():
                label1.destroy()
            
            global g
            
            g=g+1
            
            
           
            
            
            #file_name='C:/Users/jabio/Documents/LTspiceXVII/'+ file_name

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
            
            # Position image
            
                
            

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
        tempFile= 'C:/Users/jabio/Documents/LTspiceXVII/' + file_name
            
        with open(tempFile ,"wb") as f:
            f.write(r.content)
        f.close()    
        if file_name != '.jpg':
            
            
            Display1 = Button(root, height = 5,
                     width = 10,
                     text ="view Image",
                     command = lambda:showImage(tempFile,0),font=("times new roman",10,"bold"))
            Display1.place(x=0,y=0)
            
            
            
            
            
        
            #load.show()
    
    def start(desiredLevel):
        
        reddit = praw.Reddit(client_id='inqKlcP85Mqdy5ack2UVZQ',
                             client_secret='kj8BuCWeVvoI0sYhWZlA4GG0ymVNlQ',
                             username='Friendly-Orange-5033',
                             password='Poopface%1',
                             user_agent='Anything you want')
        subreddit = reddit.subreddit('HamRadio')
        hot_confessions = subreddit.hot(limit=100)
        m=0
        for submission in hot_confessions:
            
            x=submission.title+(submission.selftext.lower())
            c= (textwrap.fill(submission.title,50) + "\n" + "\n" + textwrap.fill(x,50))
            
            #Output.insert(END, c)
           # return c
             # displayText(c)

            
           # getImage(submission)
           # speak(c,m)




          #    u=input("Next Story?")
            
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
        c=start(postNumber)
        speak(c,postNumber)
        postNumber+=1
        
        #Output.insert(END, 'Correct')
        

    def delete():
        print("here")
        Output.delete('1.0',END)
    
    
    
    
    
    
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
