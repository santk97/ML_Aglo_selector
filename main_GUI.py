from tkinter import *
from tkinter import filedialog
from tkinter import  messagebox
from tkinter import ttk

root=Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(0,0)
root.title("Algorithm Accuracy Preditor")
head=Label(root,text="Algorithm Accuracy Predictor ",relief='groove',)

head.config(font=('Times New Roman',32))
head.place(relx=0.3,rely=0.01)

def browsefunc():

    filename = filedialog.askopenfilename()
    path_entry.config(text="PAth to the File :"+filename)
    path_entry.insert(0,filename)

browsebutton = Button(root, text="Browse to Path", command=browsefunc,width=20,height=1)
browsebutton.place(relx=0.045,rely=0.23)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(0,0)
root.title("Algorithm Accuracy Preditor")
head=Label(root,text="Algorithm Accuracy Predictor ",relief='groove',)

head.config(font=('Times New Roman',32))
head.place(relx=0.3,rely=0.01)
path_entry = Entry(root,width=40,borderwidth=2,relief="groove")
path_entry.place(relx=0.03,rely=0.19)
path_entry.config(font=('Times New Roman',12),)



def upload_filepath():
    if len(path_entry.get())==0:
        messagebox.showerror("WRONG FILE TYPE","THE FILE IS NOT VALID or EMPTY. UPLOAD AGAIN.")

upload_button=Button(root,text="Upload File",foreground="red",command=upload_filepath)
upload_button.place(relx=0.18,rely=0.23)
Label(root,text="Strategy :",font=('Times New Roman',15)).place(relx=0.45,rely=0.18)
strategy=StringVar()
rad1=Radiobutton (root,text="Mean",value="mean",variable=strategy,font=("Times New Roman",12))
rad1.place(relx=0.33,rely=0.23)
rad1=Radiobutton(root,text="Median",value="median",variable=strategy,font=("Times New Roman",12))
rad1.place(relx=0.43,rely=0.23)
rad1=Radiobutton(root,text="Mode",value="mode",variable=strategy,font=("Times New Roman",12))
rad1.place(relx=0.53,rely=0.23)



# code for graphs
graph=StringVar()
Label(root,text="Viusalise the Data",font=("Times New Roman",16)).place(relx=0.70,rely=0.17)
graph_op=ttk.Combobox(root,textvariable=graph,state='readonly',font=("Times New Roman",14))
graph_op.set("Bar Graph")
graph_op['values']=['Bar Graph',"Violin Plot"]
graph_op.place(rely=0.23,relx=0.70)
plot_graph=Button(root,text="Plot Grpah",font=("Times New Roman",14))
plot_graph.place(relx=0.87,rely=0.22)


# Encoding the data
Label(root,text="Select the Column to be encoded :",font=("Times New Roman",15)).place(relx=0.1,rely=0.34)
col_no=IntVar()
enc_col=ttk.Combobox(root,textvariable=col_no,state='readonly',font=("Times New Roman",14))
enc_col.set("Choose Col. for encoding")
enc_col['values']=list(range(10))
enc_col.place(relx=0.1,rely=0.42)
onehot_but=Button(root,text="Encode ",font=("Times New Roman",14))
onehot_but.place(relx=0.28,rely=0.42)

Label (root,text="Train to Test Split ratio",font=("Times NEw Roman",15)).place(relx=0.45,rely=0.34)
w = Scale(root, from_=0, to=100,orient=HORIZONTAL,width=30,length=160,cursor ="arrow",bd=4,tickinterval=20)
w.set(70)
w.place(relx=0.46,rely=0.38)
def get_ratio():
    ratio=w.get()/100
    print ("the trian test split ratio is :",ratio)
split_but=Button(root,text="Split the data",command=get_ratio,height=1,width=13,font=("Times New Roman",12))
split_but.place(relx=0.60,rely=0.41)



#the alogorithm combobox
Label(root,text="Select the algorithm ",font=("Times NEw Roman",24)).place(relx=0.40,rely=0.6)
algo=StringVar()
algo_list=ttk.Combobox(root,textvariable=algo,state='readonly',font=("Times New Roman",18))
algo_list.set("Choose Your Algorithm")
algo_list['values']=["Linear Regression ", "SVM", "Logistic Regression", " Decision Tree", "Random Forest"]
algo_list.place(relx=0.3, rely=0.71)
final_but=Button(root,text="Apply the Algorithm ",font=("Times New Roman",17))
final_but.place(relx=0.55,rely=0.70)




show_result=Button(root,text="Show Accuracy",font=("Times New Roman",15))
show_result.place(relx=0.35,rely=0.85)
result=Label(root,text="Accuracy :   ",relief='groove')
result.config(font=('Times New Roman',24))
result.place(relx=0.5,rely=0.85)

root.mainloop()