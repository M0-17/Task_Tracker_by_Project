# Task_Tracker_by_Project
A Task Tracker that can be labeled and sorted by project. Data stored into a JSON file.





# Coding Nodes
## Tracking UIDs and indexs
On any value that can be changed by the user, there is a StringVar that will emit an interupt whenever it is changed. Each Column has it's own callback function that can call a standard function if it is used a lot. This allows for the pandas dataframe to be updated in read time without having to have a separt save button. This value is stored in a dictionary with the name of the StringVar as the key, with a tuple of (StringVar, uid) as the value.
There is no StringVar or array for values that are constantent or automatically updated, (uid, created, last_updated, etc)





Created and last_activity will allows be filled, and must be populated at creation of record


# Software Release Notes
## v1.0
- Allows for adding new rows during runtime
- Allow for changing values of all colums ['UId', 'Name', 'Status', 'Priority', 'Project', 'Group', 'People', 'Notes', 'Due', 'Last Activity', 'Created']
- Choose which file that will be loading from and saved to 
- allow for loading and saving of dataframe to file
- will automatically loading from filename specified in program 


### Libitiations
- Select box and People does nothing
- No Error Dectetion/Correction
- Due is having some bugs
- Due cannot be cleared
- Need to set in code:
    - filename
    - status_values
    - project_values
    - group_values
    - priority_values
