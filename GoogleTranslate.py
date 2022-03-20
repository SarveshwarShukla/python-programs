# Language Translator using googletrans (GUI)
# Sarveshwar Shukla (20 March 2022)
# Not working now (needs modifications)

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def TranslateApp(text="Type Here", src="english", dest="hindi"):
    receivedText = text
    receivedSource = src
    receivedDestination = dest
    translate_object = Translator()
    translated_text = translate_object.translate(text, src=receivedSource, dest=receivedDestination)
    return translated_text.text

def getData():
    sourceLanguage = source_comboBox.get()
    destinationLanguage = destination_comboBox.get()
    receivedSourceText = sourceText.get(1.0, END)
    finalTranslatedText = TranslateApp(receivedSourceText,sourceLanguage, destinationLanguage)
    destinationText.delete(1.0, END)
    destinationText.insert(END, finalTranslatedText)
    




translateAppWindow = Tk()
translateAppWindow.title("Translator")
translateAppWindow.geometry("500x800")
translateAppWindowBackgroundColor = "#F8F9FA"
translateAppWindowTextColor = "#000E35"
textAreaBackgroundColor = "#FFFFFF"
translateAppWindow.config(bg=translateAppWindowBackgroundColor)

label_title = Label(translateAppWindow, text="Translator", font=("Time New Roman", 30, "bold"),bg=translateAppWindowBackgroundColor,fg=translateAppWindowTextColor)
label_title.place(x=100,y=50)

frame = Frame(translateAppWindow).pack(side=BOTTOM)

label_sourceText = Label(translateAppWindow, text="Source Text", font=("Time New Roman", 20, "bold"), bg=translateAppWindowBackgroundColor)
label_sourceText.place(x=40,y=120, height=100)
sourceText = Text(frame, font=("Time New Roman", 20, "bold"), bg=textAreaBackgroundColor, wrap=WORD)
sourceText.place(x=40,y=200, height=100, width=400)

list_language = list(LANGUAGES.values())

source_comboBox = ttk.Combobox(frame,value=list_language)
source_comboBox.place(x=40,y=320,height=40, width=100)
source_comboBox.set("english")

translateButton = Button(frame, text="Translate", relief=RAISED, command=getData)
translateButton.place(x = 170, y = 320)

destination_comboBox = ttk.Combobox(frame, value=list_language)
destination_comboBox.place(x = 290, y = 320, height=40, width=100)
destination_comboBox.set("hindi")

label_destinationText = Label(translateAppWindow, text="Destination Text", font=("Time New Roman", 20, "bold"), bg=translateAppWindowBackgroundColor)
label_destinationText.place(x=40,y=380, height=100)
destinationText = Text(frame, font=("Time New Roman", 20, "bold"), bg=textAreaBackgroundColor, wrap=WORD)
destinationText.place(x=40, y = 460, height=100, width=400)





translateAppWindow.mainloop()