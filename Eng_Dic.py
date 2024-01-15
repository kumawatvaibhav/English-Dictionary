#...............................Oxford Dictionary................................. :
#import section  
import requests
import json
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from subprocess import Popen
import MyApi 

#api response
Popen("python MyApi.py")  #running the api file to get data


response = requests.get("http://127.0.0.1:5000/readfile")   
print(response.status_code)
def getdata():
    Word = Word_entry.get()
    data = response.json()[Word]
    output_window = Tk()
    output_window.geometry("700x700")
    disp = Text(output_window,height=200,width=70)
    disp.pack()
    disp.insert(END,data)
    print(data)

#tkinter window setup
root = CTk()
root.geometry("500x400")
root.title("")

#Labels and Input : 
Heading = CTkLabel(root,text="ENGLISH DICTIONARY",height=5,width=20)
Heading.place(relx=0.5,rely=0.05,anchor="n")

#word entry
Word_entry = CTkEntry(root,placeholder_text="Search Word",placeholder_text_color="black",fg_color="white",width=300,
                      corner_radius=10,text_color="black")
Word_entry.place(relx=0.2,rely=0.25)
btn = CTkButton(root,text="Enter",command=getdata,corner_radius=10)
btn.place(relx=0.5,rely=0.35)



#appearance_mode : 
def switch_event():
    if(switch_var.get()=="Light"):
        set_appearance_mode("Light")
    elif(switch_var.get()=="Dark"):
        set_appearance_mode("Dark")
    else:
        print("Error")



switch_var = StringVar(value="Dark")
switch = CTkSwitch(root,text="M", command=switch_event,
            variable=switch_var, onvalue="Light", offvalue="Dark")
switch.place(relx=0.85,rely=0.05)


root.mainloop()