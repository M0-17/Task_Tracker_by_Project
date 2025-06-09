# Version 1.0

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry
import datetime
import os

def select_file():
    global filename
    global filename_Entry
    global filename_val
    filename = filedialog.askopenfilename(initialdir = os.path.dirname(filename), title='Select Filename')
    filename_val.set(filename)



def update_last_activity(index, uid):
    df.at[index, 'last_activity'] = pd.Timestamp.now()
    last_activity_box[uid].config(text = df.at[index, 'last_activity'].strftime('%d-%m-%Y'))

def clean_df():
    # df['id'] = df['id'].fillna( )
    df['name'] = df['name'].fillna('')
    df['status'] = df['status'].fillna('Unknown')
    df['priority'] = df['priority'].fillna('Unknown')
    df['project'] = df['project'].fillna('Unknown')
    df['group'] = df['group'].fillna('Unknown')
    # df['people'] = df['people'].fillna('')
    df['notes'] = df['notes'].fillna('')


def Entity_Combo_callback(uid, col_label, value):
    index = df.index[df['uid'] == uid].to_list()[0]
    df.at[index, col_label] = value
    update_last_activity(index, uid)
    print(df.to_string())

def name_callback(name, index, mode):
    Entity_Combo_callback(name_val[name][1], 'name', name_val[name][0].get())

def status_callback(name, index, mode):
    Entity_Combo_callback(status_val[name][1], 'status', status_val[name][0].get())

def priority_callback(name, index, mode):
    Entity_Combo_callback(priority_val[name][1], 'priority', priority_val[name][0].get())

def project_callback(name, index, mode):
    Entity_Combo_callback(project_val[name][1], 'project', project_val[name][0].get())

def group_callback(name, index, mode):
    Entity_Combo_callback(group_val[name][1], 'group', group_val[name][0].get())

def notes_callback(name, index, mode):
    Entity_Combo_callback(notes_val[name][1], 'notes', notes_val[name][0].get())

#######################################################################################

def Timestamp_callback(uid, col_label, value):              # TODO Fix this!!!
    index = df.index[df['uid'] == uid].to_list()[0]
    print(index)
    print(df.to_string())

    update_last_activity(index, uid)

def due_callback(name, index, mode):

    Entity_Combo_callback(due_val[name][1], 'due', due_val[name][0].get())       # TODO Fix this!!!

def last_activity_callback(name, index, mode):
    Timestamp_callback(name_val[name][1], 'last_activity', name_val[name][0].get()) # TODO Fix this!!!

#######################################################################################

def new_StringVar(uid, val_dict, col_name, callback):
    temp = tk.StringVar()
    val_dict[temp._name] = (temp, uid)
    val_dict[temp._name][0].set('')
    val_dict[temp._name][0].trace('w', callback)
    return temp

def insert_new_row():
    global df
    global max_uid
    
    col_offset = 0
    print("new row")
    max_uid = max_uid + 1
    uid = max_uid
    index = len(df)
    # ['Select', 'UId', 'Name', 'Status', 'Priority', 'Project', 'Group', 'People', 'Notes', 'Due', 'Last Activity', 'Created']
    df.loc[index] = {'select': '', 'uid' : uid, 'priority': '', 'project': '', 'group': '', 'people': '', 'notes': '', 'due': '', 'last_activity': pd.Timestamp.now(), 'created': pd.Timestamp.now()}

    # load_row(index=index - 1, row=df.iloc[-1], col_offset=col_offset)

    print(df.to_string())

    
    checkbox_box[uid] = tk.Checkbutton(root, onvalue=1, offvalue=0)
    checkbox_box[uid].grid(row=index + 2, column=0 + col_offset)

    uid_box[uid] = tk.Label(root, text=str(uid))
    uid_box[uid].grid(row=index + 2, column=1 + col_offset)

    temp = new_StringVar(uid, name_val, 'name', name_callback)
    name_box[uid] = tk.Entry(root, textvariable=name_val[temp._name][0])    
    name_box[uid].grid(row=index + 2, column=2 + col_offset)

    temp = new_StringVar(uid, status_val, 'status', status_callback)
    status_box[uid] = ttk.Combobox(root, textvariable=status_val[temp._name][0], width=20, values=status_values, state="readonly")
    status_box[uid].grid(row=index + 2, column=3 + col_offset)

    temp = new_StringVar(uid, priority_val, 'priority', priority_callback)
    priority_box[uid] = ttk.Combobox(root, textvariable=priority_val[temp._name][0], width=20, values=priority_values, state="readonly")
    priority_box[uid].grid(row=index + 2, column=4 + col_offset)
    
    temp = new_StringVar(uid, project_val, 'project', project_callback)
    project_box[uid] = ttk.Combobox(root, textvariable=project_val[temp._name][0], width=20, values=project_values, state="readonly")
    project_box[uid].grid(row=index + 2, column=5 + col_offset)

    temp = new_StringVar(uid, group_val, 'group', group_callback)
    group_box[uid] = ttk.Combobox(root, textvariable=group_val[temp._name][0], width=20, values=group_values, state="readonly")
    group_box[uid].grid(row=index + 2, column=6 + col_offset)

    # people_box =   #TODO


    temp = new_StringVar(uid, notes_val, 'notes', notes_callback)
    notes_box[uid] = tk.Entry(root, textvariable=notes_val[temp._name][0])
    notes_box[uid].grid(row=index + 2, column=8 + col_offset)

    temp = tk.StringVar()
    due_val[temp._name] = (temp, uid)
    due_box[uid] = DateEntry(root, textvariable=due_val[temp._name][0], allow_empty=True, width=12, background='darkblue', foreground='white', borderwidth=2)
    due_val[temp._name][0].set('')
    due_box[uid].delete(0, "end")
    due_val[temp._name][0].trace('w', due_callback)
    due_box[uid].grid(row=index + 2, column=9 + col_offset)

    
    last_activity_box[uid] = tk.Label(text=str(pd.Timestamp.now().strftime('%d-%m-%Y')))
    last_activity_box[uid].grid(row=index + 2, column=10 + col_offset)

    created_box[uid] = tk.Label(text=str(pd.Timestamp.now().strftime('%d-%m-%Y')))
    created_box[uid].grid(row=index + 2, column=11 + col_offset)

    

#######################################################################################

def setup_StringVar(uid, val_dict, row, col_name, callback):
    temp = tk.StringVar()
    val_dict[temp._name] = (temp, uid)
    if pd.isnull(row[col_name]):
        val_dict[temp._name][0].set('')
    else:
        val_dict[temp._name][0].set(row[col_name])
    val_dict[temp._name][0].trace('w', callback)
    return temp

def load_row(index, row, col_offset):
    global max_uid
    uid = row['uid']
    if max_uid < uid:
        max_uid = uid

    uid_box[uid] = tk.Label(root, text=str(uid))
    uid_box[uid].grid(row=index + 2, column=1 + col_offset)
    
    checkbox_box[uid] = tk.Checkbutton(root, onvalue=1, offvalue=0)
    checkbox_box[uid].grid(row=index + 2, column=0 + col_offset)

    temp = setup_StringVar(uid, name_val, row, 'name', name_callback)
    name_box[uid] = tk.Entry(root, textvariable=name_val[temp._name][0])    
    name_box[uid].grid(row=index + 2, column=2 + col_offset)

    temp = setup_StringVar(uid, status_val, row, 'status', status_callback)
    status_box[uid] = ttk.Combobox(root, textvariable=status_val[temp._name][0], width=20, values=status_values, state="readonly")
    status_box[uid].grid(row=index + 2, column=3 + col_offset)

    temp = setup_StringVar(uid, priority_val, row, 'priority', priority_callback)
    priority_box[uid] = ttk.Combobox(root, textvariable=priority_val[temp._name][0], width=20, values=priority_values, state="readonly")
    priority_box[uid].grid(row=index + 2, column=4 + col_offset)
    
    temp = setup_StringVar(uid, project_val, row, 'project', project_callback)
    project_box[uid] = ttk.Combobox(root, textvariable=project_val[temp._name][0], width=20, values=project_values, state="readonly")
    project_box[uid].grid(row=index + 2, column=5 + col_offset)

    temp = setup_StringVar(uid, group_val, row, 'group', group_callback)
    group_box[uid] = ttk.Combobox(root, textvariable=group_val[temp._name][0], width=20, values=group_values, state="readonly")
    group_box[uid].grid(row=index + 2, column=6 + col_offset)

    # people_box =   #TODO


    temp = setup_StringVar(uid, notes_val, row, 'notes', notes_callback)
    notes_box[uid] = tk.Entry(root, textvariable=notes_val[temp._name][0])
    notes_box[uid].grid(row=index + 2, column=8 + col_offset)

    temp = tk.StringVar()
    due_val[temp._name] = (temp, uid)
    due_box[uid] = DateEntry(root, textvariable=due_val[temp._name][0], allow_empty=True, width=12, background='darkblue', foreground='white', borderwidth=2)
    if pd.isnull(row['due']):
        due_val[temp._name][0].set('')
        due_box[uid].delete(0, "end")
    else:
        due_val[temp._name][0].set(str(row['due'].strftime('%d-%m-%Y')))
        due_box[uid].set_date(row['due'])
    due_val[temp._name][0].trace('w', due_callback)
    due_box[uid].grid(row=index + 2, column=9 + col_offset)

    last_activity_box[uid] = tk.Label(text=str(row['last_activity'].strftime('%d-%m-%Y')))
    last_activity_box[uid].grid(row=index + 2, column=10 + col_offset)

    created_box[uid] = tk.Label(text=str(row['created'].strftime('%d-%m-%Y')))
    created_box[uid].grid(row=index + 2, column=11 + col_offset)


def gui_to_df():
    print('gui_to_df')



def save_json():
    print('save json')
    print(df)
    print(filename)
    df.to_json(path_or_buf=filename)

def load_json():
    print('load json')
    global df
    df = pd.read_json(filename, convert_dates=['due', 'last_activity', 'created'])     # TODO error handling
    for index, row in df.iterrows():
        load_row(index, row, 0)


if __name__ == "__main__":
    print("hello world")

    root = tk.Tk()
    # root.configure(bg='white')
    root.geometry('1250x750')
    max_uid = 0
    date_entry = DateEntry(root)
    # uid_to_row = {}

    checkbox_box = {}
    uid_box = {}
    name_box = {}
    name_val = {}
    status_box = {}
    status_val = {}
    priority_box = {}
    priority_val = {}
    project_box = {}
    project_val = {}
    group_box = {}
    group_val = {}
    notes_box = {}
    notes_val = {}
    due_box = {}
    due_val = {}
    last_activity_box = {}
    created_box = {}

    # title = tk.Label(text="Task Tracker by Project")
    # title.grid(column=0, row=0)

    # filename = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example.json'
    filename = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example2.json'


    status_values = ['Unknown', 'Open', 'In-process', 'Waiting on Responce', 'Closed']
    project_values = ['Unknown', 'kitchen', 'bedroom']
    group_values = ['Unknown', 'contractor', 'sub']
    priority_values = ['Unknown', 'NOW', 'High', 'Med', 'Low', 'Not Now']


    # df = pd.read_json(filename)
    projects = pd.Series(['',])
    df = pd.DataFrame({'uid': pd.Series(dtype='int'), 'name': pd.Series(dtype='str'), 'status': pd.Series(status_values, dtype='category'), 'priority': pd.Series(priority_values, dtype='category'), 'project': pd.Series(project_values, dtype='category'), 'group': pd.Series(group_values, dtype='category'),      'notes': pd.Series(dtype='str'), 'due': pd.Series(dtype='datetime64[ns]'), 'last_activity': pd.Series(dtype='datetime64[ns]'), 'created': pd.Series(dtype='datetime64[ns]')})
    df['project'] = df['project'].astype('category')
    # 'people': pd.Series(dtype='array'),


    # Testing
    # df['uid'] = range(4, 10)
    # df['created'] = pd.Timestamp.now()
    # df['last_activity'] = df['created']
    # df['name'] = ['Task 0', 'Task 1', 'Call HR', '', 'Task 4', '']
    # df['project'] = ['kitchen', 'dinning', '', ' ', 'bedroom', 'kitten']
    # df['due'] = [None, datetime.date(2001, 1, 1), datetime.date(2025, 6, 15), None, None, None]

    # print(df.to_string())

    header = ['Select', 'UId', 'Name', 'Status', 'Priority', 'Project', 'Group', 'People', 'Notes', 'Due', 'Last Activity', 'Created']
    for index, head in enumerate(header):
        header_box = tk.Label(text=head)
        header_box.grid(row=1, column=index)

    try:
        load_json()
    except:
        print(filename + " Not Acceptable")

    # clean_df()    
   
    insert_button = tk.Button(root, text="Insert New Task", command=insert_new_row)
    insert_button.grid(row=0, column=2)

    filename_val = tk.StringVar()
    filename_val.set(filename)
    filename_Entry = tk.Entry(root, textvariable=filename_val)
    filename_Entry.grid(row=0, column=8)
    filename_button = tk.Button(root, text='Select File', command=select_file)
    filename_button.grid(row=0, column=9)

    
    load_button = tk.Button(root, text='Load From File', command=load_json)
    load_button.grid(row=0, column=6)
    save_button = tk.Button(root, text='Save To File', command=save_json)
    save_button.grid(row=0, column=7)


    print(df.to_string())

    root.mainloop()

