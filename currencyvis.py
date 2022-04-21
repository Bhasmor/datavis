import tkinter as tk
import datetime
import json
import os.path

  
path = "currency.json"
def set_data(money):
     curDate = datetime.datetime.now()
     date = curDate.strftime(F"Date : %d.%m.%Y")
     my_currency ={
        "days":[
            {
            "date" : F"{date}",
            "money" : money
            }
        ]
        
    }

     if os.path.isfile(path):
         with open(path, "r") as outfile:
            json_object = json.load(outfile)
         with open(path, "w") as outfile:  
            json_object["days"] += (my_currency["days"])
            json.dump(json_object, outfile , indent=4) 
     else:
         with open(path, "w") as outfile:
             json.dump(my_currency, outfile , indent=4)             
    

def get_data():
     with open(path, 'r') as openfile:
        json_object = json.load(openfile)
     return json_object



master=tk.Tk() 

master.geometry("600x400")
money_var=tk.IntVar()
 

def submit(): 
    money=money_var.get()
    set_data(money)
    money_var.set("")
     

money_label = tk.Label(master, text = 'Money', font=('calibre',15, 'bold'))
money_entry = tk.Entry(master,textvariable = money_var, font=('calibre',15,'normal'))
sub_btn=tk.Button(master,text = 'Submit', command = submit)
  

money_label.grid(row=0,column=0)
money_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
master.mainloop()
