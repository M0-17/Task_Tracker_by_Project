import pandas as pd
import tkinter as tk
from tkinter import ttk
import math


def insert_new_row():
    col_offset = 0
    print("new row")
    global max_uid
    max_uid = max_uid + 1
    id = max_uid
    uid_box[id] = tk.Label(root, text=str(id))
    uid_box[id].grid(row=root.grid_size()[1], column=col_offset)

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
    
    

def setup_ComboBox(values, row_value, row_index, width = 20):
    combo_box = ttk.Combobox(root, width=width, values=values, state="readonly")
    if not row_value[row_index] or row_value[row_index].isspace():
        combo_box.current(0)
    elif row_value[row_index] in values:
        try:
            combo_box.current(values.index(row_value[row_index]))
        except ValueError:
            combo_box.current(0)
    else:
        combo_box.current(0)

    return combo_box


def Entity_callback(uid, col_label, value):
    index = df.index[df['uid'] == uid].to_list()[0]
    df.at[index, col_label] = value
    update_last_activity(index, uid)

def name_callback(name, index, mode):
    Entity_callback(name_val[name][1], 'name', name_val[name][0].get())

def notes_callback(name, index, mode):
    Entity_callback(notes_val[name][1], 'notes', notes_val[name][0].get())


def Timestamp_callback(uid, col_label, value):
    index = df.index[df['uid'] == uid].to_list()[0]
    print(Timestamp_callback)
    update_last_activity(index, uid)

def due_callback(name, index, mode):
    Timestamp_callback(name_val[name][1], 'due', name_val[name][0].get())

def last_activity_callback(name, index, mode):
    Timestamp_callback(name_val[name][1], 'last_activity', name_val[name][0].get())

def load_row(index, row, col_offset):
    global max_uid
    uid = row['uid']
    if max_uid < uid:
        max_uid = uid
    # uid_to_row[uid] = index + 2     # Row must match between grid and setting row

    uid_box[uid] = tk.Label(root, text=str(uid))
    uid_box[uid].grid(row=index + 2, column=col_offset)
    

    temp = tk.StringVar()
    name_val[temp._name] = (temp, uid)
    name_val[temp._name][0].set(row['name'])
    name_val[temp._name][0].trace('w', name_callback)
    name_box[uid] = tk.Entry(root, textvariable=name_val[temp._name][0])    
    name_box[uid].grid(row=index + 2, column=1 + col_offset)

    
    status_box[uid] = setup_ComboBox(status_values, row, 'status', 15)
    status_box[uid].grid(row=index + 2, column=2 + col_offset)

    priority_box[uid] = setup_ComboBox(priority_values, row, 'priority', 15)
    priority_box[uid].grid(row=index + 2, column=3 + col_offset)
    
    project_box[uid] = setup_ComboBox(project_values, row, 'project')
    project_box[uid].grid(row=index + 2, column=4)

    group_box[uid] = setup_ComboBox(group_values, row, 'group')
    group_box[uid].grid(row=index + 2, column=5)

    # people_box =   #TODO


    temp = tk.StringVar()
    notes_val[temp._name] = (temp, uid)
    notes_val[temp._name][0].set(row['notes'])
    notes_val[temp._name][0].trace('w', notes_callback)
    notes_box[uid] = tk.Entry(root, textvariable=notes_val[temp._name][0])
    notes_box[uid].grid(row=index + 2, column=7)

    temp = tk.StringVar()
    due_val[temp._name] = (temp, uid)
    if pd.isnull(row['due']):
        due_val[temp._name][0].set('')
    else:
        due_val[temp._name][0].set(str(row['due'].strftime('%d-%m-%Y')))
    due_val[temp._name][0].trace('w', due_callback)
    due_box[uid] = tk.Label(textvariable=due_val[temp._name][0])
    due_box[uid].grid(row=index + 2, column=8)

    last_activity_box[uid] = tk.Label(text=str(row['last_activity'].strftime('%d-%m-%Y')))
    last_activity_box[uid].grid(row=index + 2, column=9)

    created_box[uid] = tk.Label(text=str(row['created'].strftime('%d-%m-%Y')))
    created_box[uid].grid(row=index + 2, column=10)

    # Have dictionaries based in ids rather than index


def gui_to_df():
    print('gui_to_df')



def save_json():
    print('save json')




if __name__ == "__main__":
    print("hello world")

    root = tk.Tk()
    root.geometry('1000x750')
    max_uid = 0

    # uid_to_row = {}

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

    output_path = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example.json'


    insert_button = tk.Button(root, text="Insert New Task", command=insert_new_row)

    # title = tk.Label(text="Task Tracker by Project")
    # title.grid(column=0, row=0)

    filename = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example.json'


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
    df['uid'] = range(4, 10)
    df['created'] = pd.Timestamp.now()
    df['last_activity'] = df['created']
    df['name'] = ['Task 0', 'Task 1', 'Call HR', '', 'Task 4', '']
    df['project'] = ['kitchen', 'dinning', '', ' ', 'bedroom', 'kitten']

    # print(df.to_string())

    header = ['UId', 'Name', 'Status', 'Priority', 'Project', 'Group', 'People', 'Notes', 'Due', 'Last Activity', 'Created']
    for index, head in enumerate(header):
        header_box = tk.Label(text=head)
        header_box.grid(row=1, column=index)



    clean_df()    

    for index, row in df.iterrows():
        load_row(index, row, 0)

        # # if row['status'] != Closed
        # id_box[id] = tk.Label(root, text=str(index))
        # id_box[id].grid(row=index + 2, column=0)

        # # name_box = tk.Text(root, row['name'], height=2, width=15)
        # name_box[id] = tk.Entry(root)
        # name_box[id].insert(0, row['name'])
        # name_box[id].grid(row=index + 2, column=1)

        # # status_box = tk.OptionMenu(root, row['status'], *status_values)
        # sb_var[id] = tk.StringVar()
        # status_box[id] = ttk.Combobox(root, width = 20, textvariable = sb_var[id])

        # status_box[id]['values'] = status_values
        # # status_box.current(1)                         # TODO For all combo boxes
        # # status_box['values'] = ('Open', 'Closed')
        # status_box[id].grid(row=index + 2, column=2)

        # #  project_box = tk.OptionsMenu(root, row['project'], *project_values)
        # pb_var = tk.StringVar()
        # project_box = ttk.Combobox(root, width = 20, textvariable = pb_var)

        # project_box['values'] = project_values

        # project_box.grid(row=index + 2, column=4)



        # # group_box = tk.OptionMenu(root, row['group'], *group_values)
        # gb_var = tk.StringVar()
        # group_box = ttk.Combobox(root, width = 20, textvariable = gb_var)

        # group_box['values'] = group_values

        # group_box.grid(row=index + 2, column=5)

        # # people_box =                    # TODO 

        # TODO notes do we want to make larger box

        # notes_box[id] = tk.Entry(root)
        # notes_box[id].insert(0, row['notes'])
        # notes_box[id].grid(row=index + 2, column=7)

        # due_box = tk.Label(text=str(row['due']))
        # due_box.grid(row=index + 2, column=8)

        # last_activity_box = tk.Label(text=str(row['last_activity']))
        # last_activity_box.grid(row=index + 2, column=9)

        # created_box = tk.Label(text=str(row['created']))
        # created_box.grid(row=index + 2, column=10)

#     trace(name_val )
# name_val[id].trace('w', update_callback)
    insert_button.grid(row=0, column=1)

    print(df.to_string())

    root.mainloop()

