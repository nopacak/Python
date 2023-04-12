import tkinter  as tk 
from tkinter import ttk
from web import scrap_the_link


root = tk.Tk()
root.title("Smart Mirror")
root["bg"] = "black"
root.geometry("700x600")  
from time import strftime
def my_time():
    #time_string = strftime('%H:%M:%S %p') # time format 
    time_string = strftime('%H:%M:%S \n %A \n %x')
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('Helvetica',25,'bold') # display size and style
my_font_insult=('Times New Roman',18,'italic') # display size and style

l1=tk.Label(root,font=my_font, background="black", foreground="thistle")
l1.grid(row=0,column=0,padx=5,pady=25, sticky="n")

l_aux=tk.Label(root, font=my_font, background="black", foreground="black")
l_aux.grid(row=2,column=0,padx=5,pady=25)
l_aux.config(text="\n\n\n\n")

l2=tk.Label(root, font=my_font_insult, background="black", foreground="lavender")
l2.grid(row=15,column=0,padx=5,pady=25, sticky="w")




def my_insult():
    insult_for_gui = scrap_the_link()
    #print(f"main print: {insult_for_gui}")
    l2.config(text=insult_for_gui)
    l2.after(3500,my_insult)


my_insult()

my_time()
root.mainloop()
