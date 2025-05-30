import pandas as pd
import tkinter as tk
from tkinter import ttk


print("hello world")

root = tk.Tk()
root.geometry('750x750')


# title = tk.Label(text="Task Tracker by Project")
# title.grid(column=0, row=0)

filename = r'C:\Users\brads\OneDrive\Programs\Task_Tracker_by_Project\example.json'


status_values = ['Open', 'In-process', 'Waiting on Responce', 'Closed']
project_values = ['kitchen', 'bedroom']
group_values = ['contractor', 'sub']

# df = pd.read_json(filename)
projects = pd.Series(['',])
df = pd.DataFrame({'id': pd.Series(dtype='int'), 'name': pd.Series(dtype='str'), 'status': pd.Series(status_values, dtype='category'), 'project': pd.Series(project_values, dtype='category'), 'group': pd.Series(group_values, dtype='category'),      'notes': pd.Series(dtype='str'), 'due': pd.Series(dtype='datetime64[ns]'), 'last_activity': pd.Series(dtype='datetime64[ns]'), 'created': pd.Series(dtype='datetime64[ns]')})
df['project'] = df['project'].astype('category')
# 'people': pd.Series(dtype='array'),


df['id'].fillna(0)
df['name'].fillna('')

# print(df.to_string())

for index, row in df.iterrows():
    # if row['status'] != Closed
    id_box = tk.Label(root, text=str(index))
    id_box.grid(row=index, column=0)

    # name_box = tk.Text(root, row['name'], height=2, width=15)
    name_box = tk.Entry(root)
    name_box.insert(0, row['name'])
    name_box.grid(row=index, column=1)

    # status_box = tk.OptionMenu(root, row['status'], *status_values)

    status_box = ttk.Combobox(root, width = 27, textvariable = n)

    status_box['values'] = status_values
    # status_box['values'] = ('Open', 'Closed')
    status_box.grid(row=index, column=2)

    #  project_box = tk.OptionsMenu(root, row['project'], *project_values)

    project_box = ttk.Combobox(root, width = 27, textvariable = n)

    project_box['values'] = project_values

    project_box.grid(row=index, column=3)



    # group_box = tk.OptionMenu(root, row['group'], *group_values)

    group_box = ttk.Combobox(root, width = 27, textvariable = n)

    group_box['values'] = group_values

    group_box.grid(row=index, column=4)

    # people_box = 

    due_box = tk.Label(text=str(row['due']))
    due_box.grid(row=index, column=6)

    last_activity_box = tk.Label(text=str(row['last_activity']))
    created_box.grid(row=index, column=7)

    created_box = tk.Label(text=str(row['created']))
    created_box.grid(row=index, column=8)

    # May need to use a TopLevel with Scrollbar to show display of rows geather than 1 screen

    # Want to add ability for blocker links

    


print(df.to_string())





root.mainloop()
