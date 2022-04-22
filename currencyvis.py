import tkinter as tk
import datetime
import json
import os.path


money_hold = 0
path = "currency.json"

#TODO add a label shows the "todays" added money 


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
            for i in json_object["days"]:
                global money_hold
                money_hold += i["money"]
            
     else:
         with open(path, "w") as outfile:
             json.dump(my_currency, outfile , indent=4)
         with open(path, "r") as outfile:
            json_object = json.load(outfile)         
            for i in json_object["days"]:
                money_hold += i["money"]

def get_data():
     with open(path, 'r') as openfile:
        json_object = json.load(openfile)
        for i in json_object["days"]:
            global money_hold
            money_hold += i["money"]
            money_holder.set(F"Current Money = {money_hold}")


def submit(): 
    global money_hold
    money=money_var.get()
    set_data(money)
    money_var.set("")  
    money_holder.set(F"Current Money = {money_hold}")
    money_hold = 0


master=tk.Tk() 

master.geometry("600x400")
money_var=tk.IntVar()
money_holder = tk.IntVar()


if os.path.isfile(path):     
    get_data()
    money_hold = 0

else:
    money_holder.set(F"Current Money = {money_hold}")

money_label = tk.Label(master, text = 'Money', font=('calibre',15, 'bold'))
money_entry = tk.Entry(master,textvariable = money_var, font=('calibre',15,'normal'))
cur_money_label = tk.Label(master, textvariable= money_holder , font=('calibre',15, 'bold'))
sub_btn=tk.Button(master,text = 'Submit', command = submit)

money_label.grid(row=0,column=0)
money_entry.grid(row=0,column=1)
cur_money_label.grid(row=1,column=0)
sub_btn.grid(row=2,column=1)
master.mainloop()