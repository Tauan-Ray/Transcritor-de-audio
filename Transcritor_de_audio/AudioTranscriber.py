from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
from tkinter.filedialog import *
from tkinter import messagebox
from os import rename

# Cores
Colorfont = '#282828'
Colorbackground = '#FFFFFF'
ColorButton = '#696969'

# Criando janela
app = Tk()
app.title('Audio Transcriber')
app.geometry('450x400')
app.config(bg=Colorbackground)

global micOn
micOn = False

# Preparando as imagens
imageOff = Image.open('Transcritor_de_audio/images/microphoneOff.png')
imageOff = imageOff.resize((130,130))
imageOff = ImageTk.PhotoImage(imageOff)

imageOn = Image.open('Transcritor_de_audio/images/microphoneOn.png')
imageOn = imageOn.resize((130,130))
imageOn = ImageTk.PhotoImage(imageOn)

imageRecorded = Image.open('Transcritor_de_audio/images/recorded.png')
imageRecorded = imageRecorded.resize((50,50))
imageRecorded = ImageTk.PhotoImage(imageRecorded)


# Função para começar a captar voz e criação de butões de opções
def recorder():
        global source, texto

        # Criando funções dos botões lado direito
        def reset():
             showText.destroy()
             reset_button.destroy()
             copy_button.destroy()
             download_button.destroy()
        def copy():
            global texto
            texto = showText['text']
            app.clipboard_append(texto)
        def download():
            textSave = asksaveasfilename(defaultextension='.txt')
            if textSave:
                with open(textSave, 'w') as file:
                    file.write(showText)


        # Capturando fala, passando por bloco de try except finally e mostrando na janela
        if micOn:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='pt-BR')
                showText = Label(app, text=text, font=('Arial 9') ,bg=Colorbackground, fg=Colorfont, wraplength=320)
                showText.place(x=20, y=200)
                
                # Criando botões de opções
                reset_button = Button(app, command=reset ,text='Reset' ,width=7, height=1, anchor='center', font=('Arial 9 bold'), bg=ColorButton, fg=Colorfont, relief='raised', overrelief='sunken')
                reset_button.place(x=370, y=200)

                copy_button = Button(app, command=copy ,text='Copy', width=7, height=1, anchor='center', font=('Arial 9 bold'),  bg=ColorButton, fg=Colorfont, relief='raised', overrelief='sunken')
                copy_button.place(x=370, y=229)

                download_button = Button(app, command=download ,text='Download', width=7, height=1, anchor='center', font=('Arial 9 bold'),  bg=ColorButton, fg=Colorfont, relief='raised', overrelief='sunken')
                download_button.place(x=370, y=258)
            except:
                messagebox.showerror('Error',
                                     'O microfone não está ok')

# Função para ligar o microfone
def changeMic():
    global micOn, source, recorded_button
    if micOn == False:
        mic['image'] = imageOn
        micOn = True
        source = sr.Recognizer
        recorded_button = Button(app, command=recorder ,image=imageRecorded, width=35, height=35, compound='center', anchor='center', bg=Colorbackground, relief='flat', overrelief='sunken')
        recorded_button.place(x=190, y=140)    
    elif micOn:
        mic['image'] = imageOff
        micOn = False
        recorded_button.destroy()


# Criando header
header = Frame(app, width=451, height=40, relief='raised', bg=Colorbackground, borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Audio Transcriber', width=15, height=1, font=('Serif-Font 15 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
titleHeader.place(x=130, y=2)

# Criando botões do ativação do microfone
mic = Button(app, command=changeMic ,image=imageOff, width=80, height=80, compound='center', anchor='center', bg=Colorbackground, relief='flat', overrelief='sunken')
mic.place(x=170, y=50)


app.mainloop()
