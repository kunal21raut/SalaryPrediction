from tkinter import *
import tkinter as tk

import pickle
import pandas as pd
from sklearn import linear_model


win = Tk()
win.geometry('300x300')
win.title("Salary Prediction")

with open('salary_model_pickle.pkl','rb') as f:
    model = pickle.load(f)


def calc():
    x = noOfYears.get()
    if x == "":
        user = "Please enter no of years."
        Label(win,text=user,fg='red',bg='yellow',font=("Verdana 10 bold")).place(x=12,y=200)
    else:
        predicted = model.predict([[x]])
        Label(win,text="Your Expected Salary is :"+str(int(predicted[0][0])),fg = "blue",bg="yellow",height="2",font=("Calibri 10")).place(x=12,y=200)
    
    



title = title = Label(win,text='Salary Prediction',width="300",height="2",fg='blue',font=("Verdana 20")).pack()
noOfYears =StringVar()
yearLabel = Label(win,text="Years of Experience :",fg = "blue",bg="yellow",font=("Calibri 10")).place(x=12,y=60)
years = Entry(win,width=20,textvariable=noOfYears).place(x=140,y=60)
calculate_btn = Button(win,text="Submit",command=calc,activebackground="lightgreen",bg='green',font=("Calibri 15")).place(x=150,y=100)



win.mainloop()




