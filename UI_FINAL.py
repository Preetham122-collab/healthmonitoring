import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  ##

from sklearn import metrics
from sklearn.metrics import confusion_matrix,classification_report


from sklearn import tree
from sklearn.metrics import f1_score,accuracy_score,roc_curve,roc_auc_score,recall_score #,plot_roc_curve
##from mlxtend.plotting import plot_confusion_matrix



from sklearn.ensemble import ExtraTreesClassifier

import requests
import telepot
deeksha=telepot.Bot("6162094642:AAHu9YvljJQZLp86BRtdTSuNFZy_6AJyAds")
anjali=telepot.Bot("6124297801:AAH5xRhCQyV1gffbmSYkrfRzbX3OSZRv960")


# from warnings import filterwarnings
# filterwarnings("ignore")
df = pd.read_csv('data.csv',sep=',',encoding="utf-8")
X = df.drop('target',axis=1).values
Y = df['target'].values

# Split the dataset into training and testing.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Train and predict.
LL = LogisticRegression(solver='liblinear',max_iter = 1000, random_state = 31)
LL.fit(X_train,Y_train)
Y_pred_lr = LL.predict(X_test) 
y_pred_lr = np.around(Y_pred_lr)


score_lr = round(accuracy_score(Y_pred_lr,Y_test)*100,4)


data=requests.get("https://api.thingspeak.com/channels/2064702/feeds.json?api_key=XX8GDWC6J3S44965&results=2")
hb_t=float(data.json()['feeds'][-1]['field1'])
temp_t=float(data.json()['feeds'][-1]['field2'])
oxy_t=float(data.json()['feeds'][-1]['field3'])
bp_t=float(data.json()['feeds'][-1]['field4'])
ecg_t=float(data.json()['feeds'][-1]['field5'])



from tkinter import *
import tkinter as tk



root = tk.Tk()
root.title('Virtual Doctor')
root.geometry('1500x750')
root.configure(background="#ffffff")
from PIL import Image,ImageTk

img=Image.open("aa.jpg")
img=img.resize((1500,750))
bg=ImageTk.PhotoImage(img)
lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

label = Label( root, text="patient survilence" ,font=('arial',18,'bold'),background="#4cd2e0")

label.place(x=400,y=20)


label_1 = tk.Label(root, text ='NAME',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=100)


    
Entry_0= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_0.place(x=500,y=100)


label_1 = tk.Label(root, text ='Blood pressure',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=170)


    
Entry_1= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_1.place(x=500,y=170)
Entry_1.insert(0,bp_t)

label_2 = tk.Label(root, text ='SpO2',font=("Helvetica", 20),background="#4cd2e0")
label_2.place(x=100,y=240)


    
Entry_2 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_2.place(x=500,y=240)
Entry_2.insert(0,oxy_t)
    
    
label_3 = tk.Label(root, text ='Heart beat',font=("Helvetica", 20),background="#4cd2e0")
label_3.place(x=100,y=310)


    
Entry_3 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_3.place(x=500,y=310)
Entry_3.insert(0,hb_t)

label_4 = tk.Label(root, text ='ECG rate',font=("Helvetica", 20),background="#4cd2e0")
label_4.place(x=100,y=380)


    
Entry_4= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_4.place(x=500,y=380)
Entry_4.insert(0,ecg_t)



label_5 = tk.Label(root, text ='Temperature',font=("Helvetica", 20),background="#4cd2e0")
label_5.place(x=100,y=450)


    
Entry_5 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_5.place(x=500,y=450)
Entry_5.insert(0,temp_t)


    
    
    
    

    


def fever():
    med="Diagnosis Drugs for Fever  \n  Paracetamol \n acetaminophen \n Tylenol  \n aspirin \n  Acephen  \n Ecpirin"
    label_rem.configure(text=med)
    label_rem.configure(font=("Arial",16),height=10,width=35)
    deeksha.sendMessage("1871797402",str( " \n  Medicine Provided  :  "+str(med)))
    anjali.sendMessage("1685693022",str( " \n  Medicine Provided  :  "+str(med)))
def chest_pain():
    med="Diagnosis Drugs for chest_pain \n Amlodipine \n Nadroparin \n Isosorbide \n Nifedipine \n Atenolol \n Diltiazem"
    label_rem.configure(text=med)
    label_rem.configure(font=("Arial",16),height=10,width=35)
    deeksha.sendMessage("1871797402",str( " \n  Medicine Provided  :  "+str(med)))
    anjali.sendMessage("1685693022",str( " \n  Medicine Provided  :  "+str(med)))
def Critical():
    med="You were critical \n concern the doctor nearby"
    label_rem.configure(text=med)
    label_rem.configure(font=("Arial",16),height=10,width=35)
    deeksha.sendMessage("1871797402",str( " \n  Medicine Provided  :  "+str(med)))
    anjali.sendMessage("1685693022",str( " \n  Medicine Provided  :  "+str(med)))
   
    
    

def predict():
    global name,bp,oxy,hb,ecg,temp
    name=Entry_0.get()
    bp =  float(Entry_1.get())
    oxy = float(Entry_2.get())
    hb = float(Entry_3.get())
    ecg = float(Entry_4.get())
    temp =  float(Entry_5.get())
    if bp> 140 or bp <90 or hb > 130 or hb < 60 or oxy > 100 or oxy < 95 or ecg > 860 or ecg < 160 or temp<80 or temp > 108 :
        label_5 = tk.Label(root, text ='CHECK THE INPUT RANGE',font=("Helvetica", 20),background="#4cd2e0")
        label_5.place(x=500,y=550)
    else:
        out = LL.predict([[float(bp),
        float(oxy),
        float(hb),
        float(ecg),
        float(temp)]])     ##float(area)

        


        print(out[0])
        global res
        res=""
        if out[0] == 1 :
            res="NORMAL"
            deeksha.sendMessage("1871797402",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n  "))
            anjali.sendMessage("1685693022",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n " ))
            
        elif out[0] == 3: 
            res="FEVER"
            deeksha.sendMessage("1871797402",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n  "))
            anjali.sendMessage("1685693022",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n " ))
            if bp > 150:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n HIGN Blood Pressure"))  
                anjali.sendMessage("1685693022",str( " \n  HIGN Blood Pressure"))
            elif bp<40:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n LOW Blood Pressure"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Blood Pressure"))
            if ecg < 100:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  Low ECG Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  Low ECG Rate Heart Issues"))
            elif ecg>450:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  HIGH ECG Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH ECG Rate Heart Issues"))
            if hb> 150:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Heart Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Heart Rate Heart Issues"))
            elif hb<50:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  LOW Heart Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Heart Rate Heart Issues"))
            if oxy> 150:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Oxygen Rate Heart Issues"))
            elif oxy<50:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  LOW Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Oxygen Rate Heart Issues"))
            elif oxy>150:
                res="FEVER"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Oxygen Rate Heart Issues"))
            b3=tk.Button(root,text="fever",bg="pink",fg="black",font=("Arial",16),width=10,command=fever)
            b3.place(x=500,y=650)
            
            
        elif out[0] == 2:
            res="CHEST PAIN"
            deeksha.sendMessage("1871797402",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n  "))
            anjali.sendMessage("1685693022",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n " ))
            if bp > 150:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n HIGN Blood Pressure"))  
                anjali.sendMessage("1685693022",str( " \n  HIGN Blood Pressure"))
            elif bp<40:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n LOW Blood Pressure"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Blood Pressure"))
            if ecg < 100:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  Low ECG Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  Low ECG Rate Heart Issues"))
            elif ecg>450:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  HIGH ECG Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH ECG Rate Heart Issues"))
            if hb> 150:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Heart Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Heart Rate Heart Issues"))
            elif hb<50:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  LOW Heart Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Heart Rate Heart Issues"))
            if oxy> 150:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Oxygen Rate Heart Issues"))
            elif oxy<50:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  LOW Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Oxygen Rate Heart Issues"))
            elif oxy>150:
                res="CHEST PAIN"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Oxygen Rate Heart Issues"))
            b3=tk.Button(root,text="chest_pain",bg="pink",fg="black",font=("Arial",16),width=10,command=chest_pain)
            b3.place(x=500,y=650)
            
            
        elif out[0] == 4:
            res="Critical"
            deeksha.sendMessage("1871797402",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n  "))
            anjali.sendMessage("1685693022",str("Patient  :  "+str(name)+ "\n Status  :  "+str(res)+" \n " ))
            if bp > 150:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n HIGN Blood Pressure"))  
                anjali.sendMessage("1685693022",str( " \n  HIGN Blood Pressure"))
            elif bp<40:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n LOW Blood Pressure"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Blood Pressure"))
            if ecg < 100:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  Low ECG Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  Low ECG Rate Heart Issues"))
            elif ecg>450:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  HIGH ECG Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH ECG Rate Heart Issues"))
            if hb> 150:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Heart Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Heart Rate Heart Issues"))
            elif hb<50:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  LOW Heart Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Heart Rate Heart Issues"))
            if oxy> 150:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Oxygen Rate Heart Issues"))
            elif oxy<50:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  LOW Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  LOW Oxygen Rate Heart Issues"))
            elif oxy>150:
                res="Critical"
                deeksha.sendMessage("1871797402",str( " \n  HIGH Oxygen Rate Heart Issues"))  
                anjali.sendMessage("1685693022",str( " \n  HIGH Oxygen Rate Heart Issues"))
            b3=tk.Button(root,text="Critical",bg="pink",fg="black",font=("Arial",16),width=10,command=Critical)
            b3.place(x=500,y=650)
        
    
        print(res)
        output.configure(text=res)
        
  



b1 = Button(root, text = 'predict',font=("Helvetica", 20),background="#4cd2e0",command = predict)
b1.place(x=100,y=550)
    

output = Label(root,text=" ",font=("Helvetica", 20),background="#4cd2e0")
output.place(x=500,y=550)
global label_rem
label_rem= Label(root,fg="black",font=("Arial",16),height=0,width=0)
label_rem.place(x=900,y=30)                 


root.mainloop()



