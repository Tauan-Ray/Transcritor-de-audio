from tkinter import *
from PIL import Image, ImageTk

# Cores
Colorfont = '#282828'
Colorbackground = '#FFFFFF'

# Criando janela
app = Tk()
app.title('Audio Transcriber')
app.geometry('400x350')
app.config(bg=Colorbackground)

global micOn
micOn = False

# Preparando as imagens
imageOff = Image.open('Transcritor de audio/images/microphoneOff.png')
imageOff = imageOff.resize((130,130))
imageOff = ImageTk.PhotoImage(imageOff)

imageOn = Image.open('Transcritor de audio/images/microphoneOn.png')
imageOn = imageOn.resize((130,130))
imageOn = ImageTk.PhotoImage(imageOn)

def changeMic():
    global micOn
    if micOn == False:
        mic['image'] = imageOn
        micOn = True
    
    elif micOn == True:
        mic['image'] = imageOff
        micOn = False


# Criando header
header = Frame(app, width=401, height=40, relief='raised', bg=Colorbackground, borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Audio Transcriber', width=15, height=1, font=('Serif-Font 15 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
titleHeader.place(x=105, y=2)

# Criando botões do ativação do microfone
mic = Button(app, command=changeMic ,image=imageOff, width=80, height=80, compound='center', anchor='center', bg=Colorbackground, relief='flat', overrelief='sunken')
mic.place(x=150, y=50)


app.mainloop()
