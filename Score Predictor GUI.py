#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
dataset = pd.read_csv('T20.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#encoding the categorial data
from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
x[:,0] = le1.fit_transform(x[:,0])
le2 = LabelEncoder()
x[:,1] = le2.fit_transform(x[:,1])
le3 = LabelEncoder()
x[:,2] = le3.fit_transform(x[:,2])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=1)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Training the dataset
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=20)
reg.fit(x_train,y_train)

def predict_score() :
    global enter_venue,enter_bat,enter_field,enter_curr,enter_wick,enter_ovr,enter_r5,enter_w5,enter_b1,enter_b2
    venue = enter_venue.get()
    team1 = enter_bat.get()
    team2 = enter_field.get()
    curr_score = enter_curr.get()
    wickets = enter_wick.get()
    overs = enter_ovr.get()
    runs_last_5 = enter_r5.get()
    wick_last_5 = enter_w5.get()
    bat1 = enter_b1.get()
    bat2 = enter_b2.get()
    
    if len(overs)<3 :
        overs=overs+'.0'

    overs=overs.split('.')
    overs=int(overs[0])*6+int(overs[1])
    overs=120-overs
    
    data1 = le1.transform([venue])
    data2 = le2.transform([team1])
    data3 = le3.transform([team2])
    final = reg.predict(sc.transform([[data1, data2, data3, curr_score, wickets, overs, runs_last_5, wick_last_5, bat1, bat2]]))
    string = 'The Projected Final Score is = ' + str(int(final[0]))
    
    label_final=Label(text=string,bg="white",font=('Century Schoolbook',14,'bold'))
    label_final.place(x=75,y=717,height=50,width=450)



from tkinter import *
screen = Tk()
screen.title("Cricket Score Predictor")
screen.geometry("770x590")
screen.wm_minsize(width=590,height=770)
screen.wm_maxsize(width=590,height=770)
screen.config(bg="white")

label_app_name=Label(screen,text="IPL Score Predictor",font=('Arial',20),bg="white")
label_app_name.pack()

label_venue=Label(text="Enter Venue :",bg="white",font=('Century Schoolbook',12,'bold'))
label_venue.place(x=15,y=60,height=30,width=250)
enter_venue=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_venue.place(x=300,y=60,height=30,width=250)

label_bat=Label(text="Enter Batting Team :",bg="white",font=('Century Schoolbook',12,'bold'))
label_bat.place(x=15,y=120,height=30,width=250)
enter_bat=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_bat.place(x=300,y=120,height=30,width=250)

label_field=Label(text="Enter Fielding Team :",bg="white",font=('Century Schoolbook',12,'bold'))
label_field.place(x=15,y=180,height=30,width=250)
enter_field=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_field.place(x=300,y=180,height=30,width=250)

label_curr=Label(text="Enter current score :",bg="white",font=('Century Schoolbook',12,'bold'))
label_curr.place(x=15,y=240,height=30,width=250)
enter_curr=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_curr.place(x=300,y=240,height=30,width=250)

label_wick=Label(text="Enter wickets fallen :",bg="white",font=('Century Schoolbook',12,'bold'))
label_wick.place(x=15,y=300,height=30,width=250)
enter_wick=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_wick.place(x=300,y=300,height=30,width=250)

label_ovr=Label(text="Enter Overs completed :",bg="white",font=('Century Schoolbook',12,'bold'))
label_ovr.place(x=15,y=360,height=30,width=250)
enter_ovr=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_ovr.place(x=300,y=360,height=30,width=250)

label_r5=Label(text="Enter runs scored \nin last 5 overs :",bg="white",font=('Century Schoolbook',12,'bold'))
label_r5.place(x=15,y=420,height=35,width=250)
enter_r5=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_r5.place(x=300,y=420,height=35,width=250)

label_w5=Label(text="Enter wickets fallen \nin last 5 overs :",bg="white",font=('Century Schoolbook',12,'bold'))
label_w5.place(x=15,y=480,height=35,width=250)
enter_w5=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_w5.place(x=300,y=480,height=35,width=250)

label_b1=Label(text="Enter score of Striker :",bg="white",font=('Century Schoolbook',12,'bold'))
label_b1.place(x=15,y=540,height=30,width=250)
enter_b1=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_b1.place(x=300,y=540,height=30,width=250)

label_b2=Label(text="Enter score of Non-striker :",bg="white",font=('Century Schoolbook',12,'bold'))
label_b2.place(x=15,y=600,height=30,width=250)
enter_b2=Entry(bg="white",font=('Century Schoolbook',12,'bold'),fg="black")
enter_b2.place(x=300,y=600,height=30,width=250)

btn_signup=Button(text="Predict Final Score",bg="blue",fg="white",font=('Arial Black',14,'bold'),relief="solid",borderwidth=1,command=predict_score)
btn_signup.place(x=180,y=660,height=30,width=230)

screen.mainloop()