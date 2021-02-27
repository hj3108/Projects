from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from translate import Translator

FONT_NAME = "Courier"

#--------------------------------------------------TRANSLATE FUNCTIONALITY-----------------------------------#

def translate():
    """Translates the text."""
    source_language=source_language_entry.get()
    destination_language=destination_language_entry.get()
    text=text_entry.get()
    if len(text)==0:
        messagebox.showinfo("Multi Language Translator","Please provide some text to be translated.")
        return
    else:
        translator= Translator(from_lang=source_language,to_lang=destination_language)
        translation = translator.translate(text)
        if len(translated_text_entry.get())==0:
            translated_text_entry.insert(0,translation)
        else:
            messagebox.showinfo("Multi Language Translator","Text has already been translated.")

#------------------------------------------CLEAR FUNCTIONALITY----------------------------------#

def clear():
    """Clears the text."""
    text_entry.delete(0,END)
    translated_text_entry.delete(0,END)

#-----------------------------------------------EXIT FUNCTIONALITY-----------------------------------------#

def exit_program1():
    """Exits the Application."""
    val=messagebox.askokcancel("Exit","Do you really want to exit? ")
    if val:
        exit()

#-------------------------------------------UI SETUP-----------------------------------------------#

window=Tk()
window.title("Multi Language Translator")
window.config(bg="gold")
window.resizable(width=False,height=False)

#Canvas
canvas=Canvas(width=300,height=300,highlightthickness=0,bg="gold")
logo_img=PhotoImage(file="translation.png")
canvas.create_image(150,150,image=logo_img)
canvas.grid(row=0,column=0,columnspan=2,padx=120)

#Labels
source_language_label=Label(text="Source Language: ", font=(FONT_NAME, 10),bg="orange red")
source_language_label.grid(row=1,column=0,padx=20,pady=5)

to_language_label=Label(text="Destination Language: ", font=(FONT_NAME, 10),bg="orange red")
to_language_label.grid(row=2,column=0,padx=20,pady=5)

text_label=Label(text="Text: ", font=(FONT_NAME, 10),bg="orange red")
text_label.grid(row=3,column=0,padx=20,pady=5)

translated_text_label=Label(text="Translated Text: ", font=(FONT_NAME, 10),bg="orange red")
translated_text_label.grid(row=4,column=0,padx=20,pady=5)

#Combobox
source_language_entry = ttk.Combobox(width=40,state='readonly')
source_language_entry["values"]=("english","german","spanish","hindi","french","arabic","gujarati","tamil","telugu","turkish","ukrainian","swedish")
source_language_entry.current(0)
source_language_entry.grid(row=1,column=1,columnspan=2,pady=2)

destination_language_entry = ttk.Combobox(width=40,state='readonly')
destination_language_entry["values"]=("english","german","spanish","hindi","french","arabic","gujarati","tamil","telugu","turkish","ukrainian","swedish")
destination_language_entry.current(1)
destination_language_entry.grid(row=2,column=1,columnspan=2,pady=2)

text_entry = Entry(width=43)
text_entry.focus()#Puts cursor in textbox.
text_entry.grid(row=3,column=1,columnspan=2,pady=2)

translated_text_entry = Entry(width=43)
translated_text_entry.focus()#Puts cursor in textbox.
translated_text_entry.grid(row=4,column=1,columnspan=2,pady=2)

#Buttons
exit_button=Button(text="Exit",width=18,bg="magenta",fg="blue4",command=exit_program1)
exit_button.grid(row=5,column=0,padx=5,pady=5)

translate_button=Button(text="Translate",width=36,bg="magenta",fg="blue4",command=translate)
translate_button.grid(row=5,column=1,padx=5,pady=5)

clear_button=Button(text="Clear",width=36,bg="magenta",fg="blue4",command=clear)
clear_button.grid(row=6,column=1,padx=5,pady=5)



window.mainloop()