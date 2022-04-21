# Program to make a simple
# login screen 
 
 
import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
money_var=tk.StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    money=money_var.get()
     
    print("The name is : " + money)
     
    money_var.set("")
     
     
# creating a label for
# name using widget Label
money_label = tk.Label(root, text = 'Money', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
money_entry = tk.Entry(root,textvariable = money_var, font=('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
money_label.grid(row=0,column=0)
money_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()