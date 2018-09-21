from tkinter import *
from tkinter import filedialog
from tkinter import  messagebox

root=Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(0,0)
root.title("Algorithm Accuracy Preditor")
head=Label(root,text="Algorithm Accuracy Predictor ",relief='groove',)

head.config(font=('Times New Roman',32))
head.place(relx=0.3,y=0)

def browsefunc():

    filename = filedialog.askopenfilename()
    path_entry.config(text="PAth to the File :"+filename)
    path_entry.insert(0,filename)

browsebutton = Button(root, text="Browse to Path", command=browsefunc,width=20,height=1)
browsebutton.place(relx=0.07,rely=0.14)

path_entry = Entry(root,width=40,borderwidth=2,relief="groove")
path_entry.place(relx=0.03,rely=0.10)
path_entry.config(font=('Times New Roman',12),)

def upload_filepath():
    if len(path_entry.get())==0:
        messagebox.showerror("WRONG FILE TYPE","THE FILE IS NOT VALID or EMPTY. UPLOAD AGAIN.")



upload_button=Button(root,text="Upload File",foreground="red",command=upload_filepath)


upload_button.place(relx=0.2,rely=0.14)
root.mainloop()