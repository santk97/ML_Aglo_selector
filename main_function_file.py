#the import section
from tkinter import *
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import  messagebox
from tkinter import ttk
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.svm import  SVR
import re
from pandastable import Table, TableModel
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np


#the heading code and basic gui setting

root=Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(0,0)
root.configure(background='black')
root.title("Algorithm Accuracy Preditor")
head=Label(root,text="Algorithm Accuracy Predictor ",relief='groove',)
head.config(font=('Times New Roman',32))
head.grid(row=0,column=0,padx=10,pady=30)


def get_column_names(data):
    col_list = []
    for col in data.columns:
        col_list.append(col)
    return col_list


# the function to allow browsing for files
def browsefunc():
    filename = filedialog.askopenfilename()
    path_entry.config(text="Path to the File :" + filename)
    path_entry.insert(0, filename)


# the function to clear the entry widget
def clear_field(widget):
    widget.delete(0, END)


# the function to check if the file path is valid or not
def check_filepath():
    if (len(path_entry.get()) == 0):
        messagebox.showerror("EMPTY FILE ", "THE FILE IS EMPTY. UPLOAD AGAIN.")
        clear_field(path_entry)
        # path_entry.delete(0,END)
        return False

    else:
        pattern = r'\.csv$'
        if (re.search(pattern, path_entry.get())):
            return True
        else:
            messagebox.showerror("WRONG FILE TYPE ", "THE FILE IS NOT OF THE SPECIFIED FORMAT, PLEASE TRY AGAIN")
            clear_field(path_entry)
            return False


# the function to upload the csv file data
def upload_file():
    if check_filepath():
        global dataframe
        data = pd.read_csv(path_entry.get())
        messagebox.showinfo("SUCCESULL", "THE FILE HAS BEEN UPLOADED SUCCESFULLY")

        dataframe = data
        # print(dataframe)


# The function to show the data table
def show_table(data):
    toplevel = Toplevel(root)
    if check_filepath():
        messagebox.showinfo("Succesfull", "Now showing your data in table Format.")
    else:
        toplevel.destroy()
        return 0

    toplevel.geometry('600x400+200+100')
    toplevel.title('Table app')
    f = Frame(toplevel)
    f.pack(fill=BOTH, expand=1)
    table = pt = Table(f, dataframe=data, showtoolbar=False, showstatusbar=False, showindex=True, )
    pt.show()


# the function to show the description of data
def show_desc_data(data):
    toplevel2 = Toplevel(root)
    if check_filepath():
        messagebox.showinfo("Succesfull", "Now showing your data in table Format.")
        data = data.describe()

    else:
        toplevel2.destroy()
        return 0

    toplevel2.geometry('600x400+200+100')
    toplevel2.title('Data Description')
    f = Frame(toplevel2)
    f.pack(fill=BOTH, expand=1)
    table = pt = Table(f, dataframe=data, showtoolbar=False, showstatusbar=False, showindex=True, )
    pt.show()


# the widgets related to the uploadu=ing of the file

upload_frame = LabelFrame(root, text="Upload File", fg='blue', font=(None, 20))
upload_frame.configure(background='black')
upload_frame.grid(row=5, column=0, padx=40, pady=20)

browsebutton = Button(upload_frame, text="Browse to Path", width=20, height=1, command=lambda: browsefunc())
browsebutton.grid(row=3, column=1, padx=10, pady=10)

path_entry = Entry(upload_frame, width=40, borderwidth=2, relief="groove")
path_entry.grid(row=2, column=1, padx=10, pady=10)
path_entry.config(font=('Times New Roman', 12), )
upload_button = Button(upload_frame, text="Upload File", foreground="red", command=lambda: upload_file())
upload_button.grid(row=3, column=2, padx=10, pady=10)
reset_but = Button(upload_frame, text="Reset", foreground="blue", command=lambda: clear_field(path_entry))
reset_but.grid(row=3, column=3, padx=10, pady=10)

view_data = Button(upload_frame, text="show data", command=lambda: show_table(dataframe))

# messagebox.showerror("Error","No file Selected")
desc_data = Button(upload_frame, text="Describe Data", command=lambda: show_desc_data(dataframe))
view_data.grid(row=4, column=1, padx=5, pady=10)
desc_data.grid(row=4, column=2, padx=5, pady=10)


def data_Cleaning(data):
    toplevel123=Toplevel(root)
    def get_column_names(data):
        col_list=[]
        for col in data.columns:
            col_list.append(col)
        return col_list

    def get_null_col(data):
        col_list=[]
        for col in data.columns:
            if data[col].isna().any()==True:
                col_list.append(col)
        return col_list

    def remove_col(col_name,data):
        try:
            data.drop(columns=col_name,inplace=True)
            col_nam['values']=get_column_names(data)
            messagebox.showinfo("Succesfull","Succesfully Removed "+col_name+" Column and Updated the data!!!")
        except :
            messagebox.showerror("Error","The column has already been deleted")


    #root.geometry('600x500')
    tabcontrol=ttk.Notebook(toplevel123)
    tab1=ttk.Frame(tabcontrol)
    tab2=ttk.Frame(tabcontrol)
    tabcontrol.add(tab1,text="Remove Columns")
    tabcontrol.add(tab2,text="Fill Null Values")

    col_nam=ttk.Combobox(tab1,width=20,font=("Times New Roman ",17))
    col_nam.set("Select col. to be removed")
    col_nam['values']=get_column_names(data)

    del_but=Button(tab1,text="Delete",command= lambda: remove_col(col_nam.get(),data))

    col_nam.pack()
    del_but.pack()

    # TAB2 interface
    def show_null_val(data):
        toplevel=Toplevel(tab2)
        Label(toplevel,text=data.isnull().sum()).pack()
    def fill_null(data,column,f_strat):
        if f_strat=='Mean':
            #print(np.mean(data[column]))
            try:
                data[column]=data.fillna(np.mean(data[column]))
                messagebox.showinfo("Succesfull","Succesfullu filled"+column+"with Mode"+str(np.mean(data[column])))
            except KeyError:
                messagebox.showerror("Error","The column you are trying to fill is not available")
            except TypeError:
                 messagebox.showerror("Error","This Column can not be filled with this Type of Value. \n \t\t\tTry Again!!!")

        elif f_strat=='Mode':
            try:
                data[column]=data.fillna((data[column]).mode())
                messagebox.showinfo("Succesfull","Succesfullu filled"+column+"with Mode"+str((data[column]).mode()))
            except KeyError:
                messagebox.showerror("Error","The column you are trying to fill is not available")
            except TypeError:
                 messagebox.showerror("Error","This Column can not be filled with this Type of Value. \n \t\t\tTry Again!!!")

        col_name['value']=get_null_col(data)

        return data
    show_null=Button(tab2,text="Show Null Values",command= lambda:show_null_val(data))
    show_null.pack()
    Label(tab2,text="Select the Column you want to fill",font=("Times New Roman ",17)).pack()
    col_name=ttk.Combobox(tab2,width=18,font=("Times New Roman ",17))
    col_name.set("Select Col. to fill")
    col_name['values']=get_null_col(data)
    strategy=ttk.Combobox(tab2,width=18,font=("Times New Roman ",15))
    strategy.set("Select Filling Strategies")
    strategy['values']=['Mean',"Mode"]
    fill_vall=Button(tab2,text="Fill Values",command= lambda: fill_null(data,col_name.get(),strategy.get()))
    col_name.pack()
    strategy.pack()
    fill_vall.pack()
    tabcontrol.pack()
#the widgets related to the filling strategy
clean_frame=LabelFrame(root,text="Data Cleaning",fg='blue',font=(None,20))
clean_frame.configure(background='black')
clean_frame.grid(row=5,column=1)
try:
    fill_button=Button(clean_frame,text="Data Cleaning ",font=('Times New Roman',15),command=lambda : data_Cleaning(dataframe))
except :
    messagebox.showerror("ERROR","YOU NEED TO UPLOAD A FILE FIRST!!!")
fill_button.grid(row=3,column=2,padx=20,pady=10)

def data_Cleaning(data):
    toplevel123=Toplevel(root)
    def get_column_names(data):
        col_list=[]
        for col in data.columns:
            col_list.append(col)
        return col_list

    def get_null_col(data):
        col_list=[]
        for col in data.columns:
            if data[col].isna().any()==True:
                col_list.append(col)
        return col_list

    def remove_col(col_name,data):
        try:
            data.drop(columns=col_name,inplace=True)
            col_nam['values']=get_column_names(data)
            messagebox.showinfo("Succesfull","Succesfully Removed "+col_name+" Column and Updated the data!!!")
        except :
            messagebox.showerror("Error","The column has already been deleted")


    #root.geometry('600x500')
    tabcontrol=ttk.Notebook(toplevel123)
    tab1=ttk.Frame(tabcontrol)
    tab2=ttk.Frame(tabcontrol)
    tabcontrol.add(tab1,text="Remove Columns")
    tabcontrol.add(tab2,text="Fill Null Values")

    col_nam=ttk.Combobox(tab1,width=20,font=("Times New Roman ",17))
    col_nam.set("Select col. to be removed")
    col_nam['values']=get_column_names(data)

    del_but=Button(tab1,text="Delete",command= lambda: remove_col(col_nam.get(),data))

    col_nam.pack()
    del_but.pack()

    # TAB2 interface
    def show_null_val(data):
        toplevel=Toplevel(tab2)
        Label(toplevel,text=data.isnull().sum()).pack()
    def fill_null(data,column,f_strat):
        if f_strat=='Mean':
            #print(np.mean(data[column]))
            try:
                data[column]=data.fillna(np.mean(data[column]))
                messagebox.showinfo("Succesfull","Succesfullu filled"+column+"with Mode"+str(np.mean(data[column])))
            except KeyError:
                messagebox.showerror("Error","The column you are trying to fill is not available")
            except TypeError:
                 messagebox.showerror("Error","This Column can not be filled with this Type of Value. \n \t\t\tTry Again!!!")

        elif f_strat=='Mode':
            try:
                data[column]=data.fillna((data[column]).mode())
                messagebox.showinfo("Succesfull","Succesfullu filled"+column+"with Mode"+str((data[column]).mode()))
            except KeyError:
                messagebox.showerror("Error","The column you are trying to fill is not available")
            except TypeError:
                 messagebox.showerror("Error","This Column can not be filled with this Type of Value. \n \t\t\tTry Again!!!")

        col_name['value']=get_null_col(data)

        return data
    show_null=Button(tab2,text="Show Null Values",command= lambda:show_null_val(data))
    show_null.pack()
    Label(tab2,text="Select the Column you want to fill",font=("Times New Roman ",17)).pack()
    col_name=ttk.Combobox(tab2,width=18,font=("Times New Roman ",17))
    col_name.set("Select Col. to fill")
    col_name['values']=get_null_col(data)
    strategy=ttk.Combobox(tab2,width=18,font=("Times New Roman ",15))
    strategy.set("Select Filling Strategies")
    strategy['values']=['Mean',"Mode"]
    fill_vall=Button(tab2,text="Fill Values",command= lambda: fill_null(data,col_name.get(),strategy.get()))
    col_name.pack()
    strategy.pack()
    fill_vall.pack()
    tabcontrol.pack()
#the widgets related to the filling strategy
clean_frame=LabelFrame(root,text="Data Cleaning",fg='blue',font=(None,20))
clean_frame.configure(background='black')
clean_frame.grid(row=5,column=1)
try:
    fill_button=Button(clean_frame,text="Data Cleaning ",font=('Times New Roman',15),command=lambda : data_Cleaning(dataframe))
except :
    messagebox.showerror("ERROR","YOU NEED TO UPLOAD A FILE FIRST!!!")
fill_button.grid(row=3,column=2,padx=20,pady=10)


# Encoding the data
def encode_data(data):
    toplevel1231 = Toplevel(root)

    def get_Categ_data(data):
        col_list = []
        for col in data.columns:
            if data.dtypes[col] == object:
                col_list.append(col)
        return col_list

    def encode_data(data, col_name):
        global features
        data = pd.get_dummies(data, columns=[col_name], )
        messagebox.showinfo("Error", " The Following Column " + col_name + " has been succesfully ONEHOT ENCODED")
        # col_name['values']=get_Categ_data(data)
        # toplevel1231.destroy()
        features = data

    def show_features(data):
        # print(features)
        toplevel = Toplevel(root)
        toplevel.geometry('600x400+200+100')
        toplevel.title('Table app')
        f = Frame(toplevel)
        f.pack(fill=BOTH, expand=1)
        table = pt = Table(f, dataframe=data,
                           showtoolbar=False, showstatusbar=False, showindex=True, )
        pt.show()

    col_name = ttk.Combobox(toplevel1231, )
    col_name.set('Select the categorical data')
    col_name['values'] = get_Categ_data(data)
    enco_but = Button(toplevel1231, text="Encode the Column ", command=lambda: encode_data(features, col_name.get()))
    show_features_but = Button(toplevel1231, text="Show the Features", command=lambda: show_features(features))
    col_name.pack()
    enco_but.pack()
    show_features_but.pack()


encode_frame = LabelFrame(root, text="One Hot Encoding", fg='blue', font=(None, 20))
encode_frame.configure(background='black')
encode_frame.grid(row=10, column=1)

onehot_but = Button(encode_frame, text="Encode ", font=("Times New Roman", 20), command=lambda: encode_data(features))
onehot_but.grid(row=7, column=1, padx=20, pady=10)

scale_frame = LabelFrame(root, text="Test To Train", fg='blue', font=(None, 20))
scale_frame.configure(background='black')
scale_frame.grid(row=10, column=2, padx=40)
# Label (scale_frame,text="Test to Train Split ratio",font=("Times New Roman",15)).grid(row=6,column=0)
scale = Scale(scale_frame, from_=0, to=100, orient=HORIZONTAL, width=30, length=160, cursor="arrow", bd=4,
              tickinterval=20)
scale.set(30)
scale.grid(row=7, column=0, padx=20, pady=10)


def split_data(features, label):
    global features_train
    global features_test
    global label_train
    global label_test
    features_train, features_test, label_train, label_test = train_test_split(features, label,
                                                                              test_size=(scale.get() / 100),
                                                                              random_state=0)
    messagebox.showinfo("Successfull", "The data has been successfully splitted into Test and Train.")


split_but = Button(scale_frame, text="Split the data", command=lambda: split_data(features, label), height=1, width=13,
                   font=("Times New Roman", 14))
split_but.grid(row=7, column=1, padx=20, pady=10)


def feat_label(data):
    toplevel1212 = Toplevel(root)

    def strip_data(data, label_name):
        global features
        global label
        label = data[label_name]
        features = data[data.columns.difference([label_name])]
        messagebox.showinfo("Succesfull!!!", "The features and labels have been successfully seperated!!!")
        toplevel1212.destroy()
        # print(features)
        # print (label)

    Label(toplevel1212, text="Select the Column for Label and rest are features: ").pack()
    Label_name = ttk.Combobox(toplevel1212, )
    Label_name.set("Select the Label ")
    Label_name['values'] = get_column_names(data)
    strip = Button(toplevel1212, text="Seprate Features and Labels", command=lambda: strip_data(data, Label_name.get()))

    Label_name.pack()
    strip.pack()


featlabel_frame = LabelFrame(root, text="Identify Features and Labels", fg='blue', font=(None, 20))
featlabel_frame.configure(background='black')
featlabel_frame.grid(row=10, column=0)

try:
    feat_and_label = Button(featlabel_frame, text="Features and Label ", font=("Times New Roman", 16),
                            command=lambda: feat_label(dataframe))
    feat_and_label.grid(row=7, column=1, padx=20, pady=10)

except:
    messagebox.showerror("ERROR", "YOU NEED TO UPLOAD A FILE FIRST!!!")

# the alogorithm combobox
algo_frame = LabelFrame(root, text="Algorithm", fg='blue', font=(None, 20))
algo_frame.configure(background='black')
algo_frame.grid(row=15, column=0)
# Label(algo_frame,text="Select the algorithm ",font=("Times New Roman",24)).grid(row=12,column=1)
algo = StringVar()
algo_list = ttk.Combobox(algo_frame, textvariable=algo, state='readonly', font=("Times New Roman", 18))
algo_list.set("Choose Your Algorithm")
algo_list['values'] = ["Linear Regression", "SVM", "Logistic Regression", "Decision Tree", "Random Forest"]
algo_list.grid(row=13, column=1, padx=20, pady=10)


def apply_algo(algo):
    global label_pred
    if algo == 'Linear Regression':
        regressor = LinearRegression()
        regressor.fit(features_train, label_train)
        label_pred = regressor.predict(features_test)
        messagebox.showinfo("SUCCESSFULL", "The Alogrithm has been applied")

    if algo == 'SVM':
        regressor = SVR(kernel='rbf')
        regressor.fit(features, label)
        label_pred = regressor.predict(features_test)
        messagebox.showinfo("SUCCESSFULL", "The Alogrithm has been applied")
    if algo == 'Logistic Regression':
        messagebox.showinfo("SUCCESSFULL", "The Alogrithm has been applied")

    if algo == 'Decision Tree':
        regressor = DecisionTreeRegressor(random_state=0)
        regressor.fit(features, label)
        label_pred = regressor.predict(features_test)
        messagebox.showinfo("SUCCESSFULL", "The Alogrithm has been applied")

    if algo == 'Random Forest':
        regressor = RandomForestRegressor(n_estimators=10, random_state=0)
        regressor.fit(features, label)
        # Predicting a new result
        label_pred = regressor.predict(features_test)
        messagebox.showinfo("SUCCESSFULL", "The Alogrithm has been applied")


final_but = Button(algo_frame, text="Apply the Algorithm ", font=("Times New Roman", 17),
                   command=lambda: apply_algo(algo_list.get()))
final_but.grid(row=13, column=2, padx=20, pady=10)



def show_acc():
    accuracy=(r2_score(label_test,label_pred)*100)
    result.configure(text="Accuracy: %.2f%%"%(accuracy))
res_frame=LabelFrame(root,text="Algorithm",fg='blue',font=(None,20))
res_frame.configure(background='black')
res_frame.grid(row=15,column=1,padx=20,pady=50)
show_result=Button(res_frame,text="Show Accuracy",font=("Times New Roman",15),command= lambda: show_acc())
show_result.grid(row=12,column=1,padx=20,pady=10)
result=Label(res_frame,text="Accuracy: 000.00%",relief='groove')
result.config(font=('Times New Roman',20))
result.grid(row=13,column=1,padx=20,pady=10)


root.mainloop()









