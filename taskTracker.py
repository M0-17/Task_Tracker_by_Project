# Version 1.0

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry
import datetime
import os
import json

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


def Entry_Combo_callback(uid, col_label, value):
    index = df.index[df['uid'] == uid].to_list()[0]
    df.at[index, col_label] = value
    update_last_activity(index, uid)
    # print(df.to_string())

def name_callback(name, index, mode):
    Entry_Combo_callback(name_val[name][1], 'name', name_val[name][0].get())

def status_callback(name, index, mode):
    Entry_Combo_callback(status_val[name][1], 'status', status_val[name][0].get())

def priority_callback(name, index, mode):
    Entry_Combo_callback(priority_val[name][1], 'priority', priority_val[name][0].get())

def project_callback(name, index, mode):
    Entry_Combo_callback(project_val[name][1], 'project', project_val[name][0].get())

def group_callback(name, index, mode):
    # print('here--------------------------')
    # print(tabs)
    old_group = df.at[df.index[df['uid'] == group_val[name][1]].to_list()[0], 'group']
    Entry_Combo_callback(group_val[name][1], 'group', group_val[name][0].get())
    # update_group_tabs(old_group, 'group', tabs['group'])
    # if group_val[name][0].get() == 'Closed':


def people_callback(name, index, mode):
    Entry_Combo_callback(people_val[name][1], 'people', people_val[name][0].get())

def notes_callback(name, index, mode):
    Entry_Combo_callback(notes_val[name][1], 'notes', notes_val[name][0].get())

#######################################################################################

def Timestamp_callback(uid, col_label, value):              # TODO Fix this!!!
    index = df.index[df['uid'] == uid].to_list()[0]
    # print(index)
    # print(df.to_string())

    update_last_activity(index, uid)

def due_callback(name, index, mode):

    Entry_Combo_callback(due_val[name][1], 'due', due_val[name][0].get())       # TODO Fix this!!!

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
    new_row = {}
    
    headers = df.columns.tolist()
    for head in headers:
        if head == 'uid':
            max_uid = int(max_uid + 1)
            uid = int(max_uid)
            new_row['uid'] = uid
        elif head == 'last_activity':
            new_row['last_activity'] = pd.Timestamp.now()
        elif head == 'created':
            new_row['created'] = pd.Timestamp.now()
        else:
            new_row[head] = defaults[head]

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    load_row(df.index[-1], df.iloc[-1], scroll_frame, col_offset)

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

def load_row(index, row, frame, col_offset):
    global max_uid
    uid = int(row['uid'])
    if max_uid < uid:
        max_uid = uid

    last_activity_box[uid] = tk.Label(frame, text=str(row['last_activity'].strftime('%d-%m-%Y')), width=header['Last Activity'])
    last_activity_box[uid].grid(row=index + 2, column=10 + col_offset)

    uid_box[uid] = tk.Label(frame, text=str(uid), width=header['UId'])
    uid_box[uid].grid(row=index + 2, column=1 + col_offset)
    
    checkbox_box[uid] = tk.Checkbutton(frame, onvalue=1, offvalue=0, width=header['Select'])
    checkbox_box[uid].grid(row=index + 2, column=0 + col_offset)

    temp = setup_StringVar(uid, name_val, row, 'name', name_callback)
    name_box[uid] = tk.Entry(frame, textvariable=name_val[temp._name][0], width=header['Name'])    
    name_box[uid].grid(row=index + 2, column=2 + col_offset)

    temp = setup_StringVar(uid, status_val, row, 'status', status_callback)
    status_box[uid] = ttk.Combobox(frame, textvariable=status_val[temp._name][0], width=header['Status'], values=status_values, state="readonly")
    status_box[uid].grid(row=index + 2, column=3 + col_offset)

    temp = setup_StringVar(uid, priority_val, row, 'priority', priority_callback)
    priority_box[uid] = ttk.Combobox(frame, textvariable=priority_val[temp._name][0], width=header['Priority'], values=priority_values, state="readonly")
    priority_box[uid].grid(row=index + 2, column=4 + col_offset)
    
    temp = setup_StringVar(uid, project_val, row, 'project', project_callback)
    project_box[uid] = ttk.Combobox(frame, textvariable=project_val[temp._name][0], width=header['Project'], values=project_values, state="readonly")
    project_box[uid].grid(row=index + 2, column=5 + col_offset)

    temp = setup_StringVar(uid, group_val, row, 'group', group_callback)
    group_box[uid] = ttk.Combobox(frame, textvariable=group_val[temp._name][0], width=header['Group'], values=group_values, state="readonly")
    group_box[uid].grid(row=index + 2, column=6 + col_offset)

    # people_box =   #TODO
    temp = setup_StringVar(uid, people_val, row, 'people', people_callback)
    people_box[uid] = tk.Entry(frame, textvariable=people_val[temp._name][0], width=header['People'])
    people_box[uid].grid(row=index+2, column=7 + col_offset)


    temp = setup_StringVar(uid, notes_val, row, 'notes', notes_callback)
    notes_box[uid] = tk.Entry(frame, textvariable=notes_val[temp._name][0], width=header['Notes'])
    notes_box[uid].grid(row=index + 2, column=8 + col_offset)

    temp = tk.StringVar()
    due_val[temp._name] = (temp, uid)
    due_box[uid] = DateEntry(frame, textvariable=due_val[temp._name][0], allow_empty=True, width=header['Due'], background='darkblue', foreground='white', borderwidth=2)
    if pd.isnull(row['due']):
        due_val[temp._name][0].set('')
        due_box[uid].delete(0, "end")
    else:
        due_val[temp._name][0].set(str(row['due'].strftime('%d-%m-%Y')))
        due_box[uid].set_date(row['due'])
    due_val[temp._name][0].trace('w', due_callback)
    due_box[uid].grid(row=index + 2, column=9 + col_offset)


    created_box[uid] = tk.Label(frame, text=str(row['created'].strftime('%d-%m-%Y')), width=header['Created'])
    created_box[uid].grid(row=index + 2, column=11 + col_offset)


def update_group_tabs(key, col, frame):
    # for widget in frame.winfo_children():
    #     widget.destroy()

    # print('updating ' + key)
    group_df = df.loc[df[col] == key]
    for index, row in group_df.iterrows():
        if not pd.isnull(row['last_activity']):
            load_row(index, row, frame, 0)

def update_all_tabs():
    # print("----------------------------------")
    for index, row in df.iterrows():
        if not pd.isnull(row['last_activity']):
            load_row(index, row, scroll_frame, 0)

    for tab_tuple in all_tabs:
        update_group_tabs(tab_tuple[0], tab_tuple[1], tab_tuple[2])

#######################################################################################

def save_json():
    print('save json')
    print(df)
    print(filename)
    df.to_json(path_or_buf=filename)

def load_json():
    print('load json')
    global df
    df = pd.read_json(filename, convert_dates=['due', 'last_activity', 'created'])     # TODO error handling
    
    update_all_tabs()

#######################################################################################

if __name__ == "__main__":
    # print("hello world")

    root = tk.Tk()
    root.geometry('1250x750')
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Main Tab')
    
    
    head_canvas = ttk.Frame(tab1)
    container = ttk.Frame(tab1)
    canvas = tk.Canvas(container)

    scrollbar_vertical = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar_horizontal = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)


    scroll_frame = ttk.Frame(canvas)
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    head_canvas.pack(side="top", fill="x")
    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_vertical.pack(side="right", fill="y")
    scrollbar_horizontal.pack(side="bottom", fill="x")

    # root.configure(bg='white')
    
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
    people_box = {}
    people_val = {}
    notes_box = {}
    notes_val = {}
    due_box = {}
    due_val = {}
    last_activity_box = {}
    created_box = {}

    # title = tk.Label(scroll_frame, text="Task Tracker by Project")
    # title.grid(column=0, row=0)

    # filename = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example.json'
    filename = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example3.json'
    config_file = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\config.json'

    status_values = ['Unknown', 'Open', 'In-process', 'Waiting on Responce', 'Need to Follow Up', 'Closed']
    project_values = ['Unknown', 'kitchen', 'bedroom']
    group_values = ['Unknown', 'contractor', 'sub']
    priority_values = ['Unknown', 'NOW', 'High', 'Med', 'Low', 'Not Now']


    cf = open(config_file)
    data = json.load(cf)
    defaults = {}

    label_config = data['labels']

    if 'name' in label_config and 'default' in label_config['name']:
        defaults['name'] = label_config['name']['defualts']
    else:
        defaults['name'] = ''

    if 'status' in label_config and 'default' in label_config['status'] and label_config['status']['default'] in status_values:
        defaults['status'] = label_config['status']['default']
    else:
        defaults['status'] = ''

    if 'priority' in label_config and 'default' in label_config['priority'] and label_config['priority']['default'] in priority_values:
        defaults['priority'] = label_config['priority']['default']
    else:
        defaults['priority'] = ''

    if 'project' in label_config and 'default' in label_config['project'] and label_config['project']['default'] in project_values:
        defaults['project'] = label_config['project']['default']
    else:
        defaults['project'] = ''

    if 'people' in label_config and 'default' in label_config['people']:
        defaults['people'] = label_config['people']['defualts']
    else:
        defaults['people'] = ''

    if 'group' in label_config and 'default' in label_config['group'] and label_config['group']['default'] in group_values:
        defaults['group'] = label_config['group']['default']
    else:
        defaults['group'] = ''

    if 'notes' in label_config and 'default' in label_config['notes']:
        defaults['notes'] = label_config['notes']['defualts']
    else:
        defaults['notes'] = ''

    if 'due' in label_config and 'default' in label_config['due']:
        defaults['due'] = label_config['due']['defualts']
    else:
        defaults['due'] = pd.NA


    # df = pd.read_json(filename)
    projects = pd.Series(['',])
    df = pd.DataFrame({'uid': pd.Series(dtype='int'), 'name': pd.Series(dtype='str'), 'status': pd.Series(status_values, dtype='category'), 'priority': pd.Series(priority_values, dtype='category'), 'project': pd.Series(project_values, dtype='category'), 'group': pd.Series(group_values, dtype='category'), 'people': pd.Series(dtype='str'), 'notes': pd.Series(dtype='str'), 'due': pd.Series(dtype='datetime64[ns]'), 'last_activity': pd.Series(dtype='datetime64[ns]'), 'created': pd.Series(dtype='datetime64[ns]')})
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

    header = {'Select':5, 'UId':2, 'Name':10, 'Status':10, 'Priority':10, 'Project':10, 'Group':10, 'People':10, 'Notes':50, 'Due':12, 'Last Activity':10, 'Created':10}
    index = 0
    for key, value in header.items():
        header_box = tk.Label(head_canvas, text=key, width=value)
        header_box.grid(row=1, column=index)
        index = index + 1

    try:
        load_json()
    except:
        print(filename + " Not Acceptable")

    # clean_df()    
   
    insert_button = tk.Button(head_canvas, text="Insert New Task", command=insert_new_row)
    insert_button.grid(row=0, column=2)

    filename_val = tk.StringVar()
    filename_val.set(filename)
    filename_Entry = tk.Entry(head_canvas, textvariable=filename_val)
    filename_Entry.grid(row=0, column=7)
    filename_button = tk.Button(head_canvas, text='Select File', command=select_file)
    filename_button.grid(row=0, column=8)

    
    load_button = tk.Button(head_canvas, text='Load From File', command=load_json)
    load_button.grid(row=0, column=10)
    save_button = tk.Button(head_canvas, text='Save To File', command=save_json)
    save_button.grid(row=0, column=6)

    update_grid_button = tk.Button(head_canvas, text='Update grid', command=update_all_tabs)
    update_grid_button.grid(row=0, column=3)

    # print(df.to_string())

    tabs = {}
    all_tabs = []
    # tabs['test'] = ttk.Frame(tabControl)
    # tabControl.add(tabs['test'], text='text')

    if data['tabs']['all_groups'] == "True":
        for label in group_values:
            if label == 'Closed':
                pass
            elif label == '' or label == 'unknown':
                pass
            else:
                tabs[label] = ttk.Frame(tabControl)
                tabControl.add(tabs[label], text=label)

                all_tabs.append([label, 'group', tabs[label]])

        for key, tab in tabs.items():
            update_group_tabs(key, 'group', tab)

        tabs['Closed'] = ttk.Frame(tabControl)
        tabControl.add(tabs['Closed'], text='Closed')
        all_tabs.append(['Closed', 'status', tabs['Closed']])
    # update_group_tabs('Closed', 'status', tabs['Closed'])


    # tab2 = ttk.Frame(tabControl)
    # tabControl.add(tab2, text='Tab 2')
    tabControl.pack(expand=1, fill='both')

    update_all_tabs()

    # treev = ttk.Treeview(tabs['test'], selectmode ='browse')
    ## print(header.keys())
    ## print(type(header.keys()))
    # treev["columns"] = list(header.keys())
    
    # for head in header.keys():
    #     treev.heading(head, text=head)

    # for index, row in df.iterrows():
    #     treev.insert("", "end", values=list(row))

    # treev.pack(expand=True, fill="both")



    root.mainloop()

