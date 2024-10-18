import pickle
model=pickle.load(open("LL.pkl","rb"))
from tkinter import *
import tkinter as tk
root = tk.Tk()
root.title('Virtual Doctor')
root.geometry('1920x1080')
root.configure(background="#ffffff")
from PIL import Image,ImageTk

img=Image.open("aa.jpg")
img=img.resize((1920,1080))
bg=ImageTk.PhotoImage(img)
lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

label = Label( root, text="patient survilence" ,font=('arial',22,'bold'),background="#4cd2e0")

label.place(x=500,y=20)


label_1 = tk.Label(root, text ='NAME',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=100)


    
Entry_0= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_0.place(x=500,y=100)

label_1 = tk.Label(root, text ='AGE',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=170)


    
Entry_01= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_01.place(x=500,y=170)

label8=tk.Label(root,text="Gender",bg="#4cd2e0",fg="black",font=("times",20))
label8.place(x=100,y=240)

#############################################################################333
def sel():
    global opt
    opt=""
    if var.get()==1:
        opt='MALE'
    elif var.get()==2:
        opt='FEMALE'
    else:
        opt='Others'
    gen_val=int(var.get())
    selection = "Selected : \n " + str(opt)
    label.config(text = selection)
##root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="M", variable=var, value=1,command=sel,bg="#4cd2e0",fg="black",font=("times",20))
R1.place(x=500,y=240)
R2 = Radiobutton(root, text="F", variable=var, value=2,command=sel,bg="#4cd2e0",fg="black",font=("times",20))
R2.place(x=600,y=240)
R3 = Radiobutton(root, text="O", variable=var, value=3,command=sel,bg="#4cd2e0",fg="black",font=("times",20))
R3.place(x=700,y=240)
label = Label(root,bg="#4cd2e0",fg="black",font=("times",20))
label.place(x=800,y=240)


label_1 = tk.Label(root, text ='Blood pressure',font=("Helvetica", 20),background="#4cd2e0")
label_1.place(x=100,y=310)


    
Entry_1= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_1.place(x=500,y=310)

label_2 = tk.Label(root, text ='SpO2',font=("Helvetica", 20),background="#4cd2e0")
label_2.place(x=100,y=380)


    
Entry_2 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_2.place(x=500,y=380)
##Entry_2.insert(0,oxy_t)
    
    
label_3 = tk.Label(root, text ='Heart beat',font=("Helvetica", 20),background="#4cd2e0")
label_3.place(x=100,y=450)


    
Entry_3 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_3.place(x=500,y=450)
##Entry_3.insert(0,hb_t)

label_4 = tk.Label(root, text ='ECG rate',font=("Helvetica", 20),background="#4cd2e0")
label_4.place(x=100,y=520)


    
Entry_4= Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_4.place(x=500,y=520)



label_5 = tk.Label(root, text ='Temperature',font=("Helvetica", 20),background="#4cd2e0")
label_5.place(x=100,y=590)


    
Entry_5 = Entry(root,font=("Helvetica", 20),background="#4cd2e0",justify=CENTER)
Entry_5.place(x=500,y=590)
##Entry_5.insert(0,temp_t)


label8=tk.Label(root,text="Cough",bg="#4cd2e0",fg="black",font=("times",20))
label8.place(x=100,y=650)

#############################################################################333
def selc():
    global optc
    optc=[]
    if varc.get()==1:
        optc='YES'
    else:
        optc='NO'
    gen_val=int(varc.get())
    selection = "Selected :  " + str(optc)
    labelc.config(text = selection)
##root = Tk()
varc = IntVar()
R1 = Radiobutton(root, text="YES", variable=varc, value=1,command=selc,bg="#4cd2e0",fg="black",font=("times",20))
R1.place(x=500,y=650)
R2 = Radiobutton(root, text="NO", variable=varc, value=2,command=selc,bg="#4cd2e0",fg="black",font=("times",20))
R2.place(x=600,y=650)

labelc = Label(root,bg="#4cd2e0",fg="black",font=("times",20))
labelc.place(x=700,y=650)


def predict():
    global name,agee        # Entry_0,Entry_1,Entry_2,Entry_3,Entry_3,Entry_5
    agee=int(Entry_01.get())
    name=str(Entry_0.get())
    bp =  float(Entry_1.get())
    oxy = float(Entry_2.get())
    hb = float(Entry_3.get())
    ecg = float(Entry_4.get())
    temp =  float(Entry_5.get())
    global res,b3,out
    out = model.predict([[float(bp),
    float(oxy),
    float(hb),
    float(ecg),
    float(temp)]])     ##float(area)

    


    print(out[0])
    
    res=""
    if out[0] == 1 :
        res="NORMAL"       
    elif out[0] == 2: 
        res="FEVER"        
    elif out[0] == 3:
        res="CHEST PAIN"
    elif out[0] == 4:
        res="Critical"
        
    
    print(res)
    output.configure(text=res)
        
  



b1 = Button(root, text = 'predict',font=("Helvetica", 20),background="#4cd2e0",command = predict)
b1.place(x=950,y=650)
    
global label_rem,output
output = Label(root,text=" ",font=("Helvetica", 20),background="#4cd2e0")
output.place(x=1100,y=650)


label_rem= Label(root,fg="black",font=("Arial",16),height=0,width=0)
               


root.mainloop()



