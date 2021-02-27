import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox  #messagebox
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Courier"

#-----------------------------------EDIT FUNCTIONALITY------------------------------#
def edit():
    website=str(website_entry.get().title())
    email=str(email_entry.get())
    password=password_entry.get()

    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
        
        if website in data:
            data[website]["email"]=email
            data[website]["password"]=password

            new_data={
                website:{
                    "email": email,
                    "password": password,
                }
            }
            
            messagebox.showinfo("Password Manager",f"Your credentials of {website} has been edited.")

            data.update(new_data) 

            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0,END)


        elif website not in data:

            messagebox.showinfo("Password Manager","There is no such website to be edited.")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    
    except FileNotFoundError:

        messagebox.showinfo("Password Manager","There is no data saved to be edited.")



   
#---------------------------------DELETE FUNCTION-----------------------------#
def delete():
    website_name=str(website_entry.get().title())
    # website_info="Website: "+website_name

    # with open("data.txt") as file:
    #     l=file.readlines()
    # list1=[char.strip("\n") for char in l]
    # list2=[char.split(";") for char in list1]
   
    # with open("data.txt", "w") as f:
    #     for sub_list in (list2):
    #         for j in  sub_list:
    #             if j==website_info :
    #                 required_index=list2.index(sub_list)
    #                 required_index1=sub_list.index(website_info)
    #                 required_list=list2[required_index]
    
    #     for i in range(len(list2)):
    #     # for line in list2:
    #         if list2[i]!=required_list:
    #             string=";".join(str(ele) for ele in list2[i])
    #             f.write(f"{string}")
    #             f.write("\n")

    # messagebox.showinfo("Password Manager",f"Your credentials of {website_info} has been deleted.")
    
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)

        if website_name in data:
            data.pop(website_name)

            data.update() 

            messagebox.showinfo("Password Manager",f"Your credentials of {website_name} has been deleted.")

            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
            
           
            
            website_entry.delete(0,END)
        
        elif website_name not in data:
            messagebox.showinfo("Password Manager","There is no such website.\n If you want you can add it.")

    except FileNotFoundError:
        messagebox.showinfo("Password Manager","There is no data saved.\n Please save it first.")

#-------------------------------SEARCHING INFORMATION---------------------------#

def search_info():
    """Searches the credentials from the file."""                  
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)<=0:
        messagebox.showinfo("Oops","Please enter something to be searched.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file) 
            
            if website not in data:
                messagebox.showinfo("Error","No Data File Found.")
                website_entry.delete(0,END)
                return
        
        except FileNotFoundError:
            messagebox.showinfo("Error","No Data File Found.")
        

        else:
            messagebox.showinfo(f"{website}","Email: "+data[website]["email"] + "\n" + "Password: "+data[website]["password"])

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator(): 
    """Generates a random password."""

    if len(password_entry.get()) >0:
        messagebox.showinfo("Password Manager","Password Already generated!")

    else:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4) 

        # password_list = []

        # for char in range(nr_letters):
        #     password_list.append(random.choice(letters))
        
        password_letters=[random.choice(letters) for char in range(nr_letters)]

        # for char in range(nr_symbols):
        #     password_list += random.choice(symbols)

        password_symbols=[random.choice(symbols) for char in range(nr_symbols)]

        # for char in range(nr_numbers):
        #     password_list += random.choice(numbers)
        
        password_numbers=[random.choice(numbers) for char in range(nr_numbers)]
        password_list = password_letters+password_numbers+password_symbols
        random.shuffle(password_list)

        # password = ""
        # for char in password_list:
        #     password += char

        password="".join(password_list)

        # print(f"Your password is: {password}")
        password_entry.insert(0,password)
        pyperclip.copy(password)  #already copies our password to the clipboard.


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Saves the login credentials."""

    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data={
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else: 
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered :\n Email:{email}\n Password: {password} \n Is it ok to save?")
        if is_ok:
            try:       
                with open("data.json", "r") as data_file:
                    # json.dump(new_data,data_file,indent=4)

                    #Reading old data
                    data=json.load(data_file) 
                    # print(data)              
            
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)
                
            else:

                #UPDATING OLD DATA WITH NEW DATA
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #Saving update data
                    json.dump(data,data_file,indent=4) #saving the updated data back into the json file and clearing off the previous data.
            
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

#-----------------------------EXIT FUNCTIONALITY---------------------------#

def exit_program():
    """Exits the Application."""

    website_info=str(website_entry.get().title()) 
    email_info=email_entry.get()
    password_info=password_entry.get()

    if len(website_info)>0 or len(password_info)>0:
        messagebox.showinfo("Password Manager","Please save your credentials if you haven't!\n It wouldn't be saved.")
    
    val=messagebox.askokcancel("Exit","Do you really want to exit? ")
    if val:
        exit()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.iconbitmap("password manager.ico")
window.config(padx=20,pady=20,bg="gold")
window.resizable(width=False,height=False)

#Canvas
canvas=Canvas(width=200,height=200,highlightthickness=0,bg="gold")
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label=tk.Label(text="Website:", font=(FONT_NAME, 10),bg="orange red")
website_label.grid(row=1,column=0)

email_label=tk.Label(text="Email/Username:", font=(FONT_NAME, 10),bg="orange red")
email_label.grid(row=2,column=0)

password_label=tk.Label(text="Password:", font=(FONT_NAME, 10),bg="orange red")
password_label.grid(row=3,column=0)

#Entry Boxes
website_entry = Entry(width=32)
website_entry.focus()#Puts cursor in textbox.
website_entry.grid(row=1,column=1)

email_entry = Entry(width=32)
email_entry.focus()#Puts cursor in textbox.
email_entry.insert(0,"harsh@gmail.com")
email_entry.grid(row=2,column=1)

password_entry = Entry(width=32,show="*")
password_entry.focus()#Puts cursor in textbox.
password_entry.grid(row=3,column=1)

#Buttons
generate_pass_button=Button(text="Generate Password",width=14,command=password_generator,bg="magenta",fg="blue4")
generate_pass_button.grid(row=3,column=2,padx=5,pady=5)

edit_button=Button(text="Edit",width=14,command=edit,bg="magenta",fg="blue4")
edit_button.grid(row=2,column=2)

add_button=Button(text="Add",width=24,command=save,bg="magenta",fg="blue4")
add_button.grid(row=4,column=1)

delete_button=Button(text="Delete",width=13,command=delete,bg="magenta",fg="blue4")
delete_button.grid(row=4,column=2)

search_button=Button(text="Search",width=14,bg="magenta",fg="blue4",command=search_info)
search_button.grid(row=1,column=2,padx=5,pady=5)

exit_button=Button(text="Exit",width=10,bg="magenta",fg="blue4",command=exit_program)
exit_button.grid(row=4,column=0,padx=5,pady=5)


window.mainloop()

