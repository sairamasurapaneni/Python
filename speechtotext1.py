import speech_recognition as sr
from googletrans import Translator

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Speech Recognition")
root.rowconfigure(3, weight = 1)
root.columnconfigure(3, weight = 1)
root.geometry('300x150')

r = sr.Recognizer()
lang_trans = {'chinese':'zh-cn', 'russian':'ru', 'arabic':'ar', 'greek':'el', 'french':'fr', 'german':'de', 'spanish':'es', 'korean':'ko'}


def recordCallback():
    audio = record()
    text = audio_to_text(audio)
    displayText(text)
    displayTranslateButton(text)
    return

def translateCallback(text, translate_to):
    
    translator = Translator()
    translation=translator.translate(text,dest=lang_trans[translate_to])
    displayTranslatedText(translation.origin + ' -> ' + translation.text)
    return

def record():
    m = sr.Microphone()
    with m as source:
       r.adjust_for_ambient_noise(source)
       audio = r.listen(source)
    return audio


def displayTranslateButton(text):
    
    default_lang = StringVar(root)
    default_lang.set('chinese')
    
    dropdown = OptionMenu(root, default_lang, *lang_trans)
    dropdown.grid(row = 1)
    
    button_translate = Button(root, text = "Translate the recognized text...", command = lambda: translateCallback(text, default_lang.get()))
    button_translate.grid(row = 2)

def displayText(text):
    messagebox.showinfo("Recognized audio", text)
    return

def displayTranslatedText(text):
    messagebox.showinfo("Translated text", text)
    return

def audio_to_text(audio):
    return r.recognize_google(audio)

button_record = Button(root, text ="Start Recording...", command = recordCallback)
button_record.grid(row = 0, sticky = N)

root.mainloop()