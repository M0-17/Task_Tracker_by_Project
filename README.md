# Task_Tracker_by_Project
A Task Tracker that can be labeled and sorted by project. Data stored into a JSON file.





# Coding Nodes
## Tracking UIDs and indexs
On any value that can be changed by the user, there is a StringVar that will emit an interupt whenever it is changed. Each Column has it's own callback function that can call a standard function if it is used a lot. This allows for the pandas dataframe to be updated in read time without having to have a separt save button. This value is stored in a dictionary with the name of the StringVar as the key, with a tuple of (StringVar, uid) as the value.
There is no StringVar or array for values that are constantent or automatically updated, (uid, created, last_updated, etc)





Created and last_activity will allows be filled, and must be populated at creation of record


# Install
`pip install pandas tkcalendar datatime`
versions
pandas: 2.3.0
tkcalendar: 1.6.0



# Software Release Notes

## v2.1
- Added Tabs to allow for multiple windows
- Update insert_new_row() to create a blank/default row & then call load_row() 
- Adding Tabs for basic screens, described in config.json
- Add button that will updates values across tabs

### v2.1 Limitations
- must set defaults in config file, no current error handling
- people cannot be indexed only a string text
- Select box
- No Error Dectetion/Correction
- Due is having some bugs
- Due cannot be cleared
- Must to set in code(no GUI):
    - filename
    - status_values
    - project_values
    - group_values
    - priority_values
- col_offset currently is not set


## v2.0
- Made Grid scrollable
- Added status value 'Need to Follow UP'
- Fixed bug where uid would display and save as float. Now is an int
- When creating a new row it sets focus to the name to allow for immediate data entry
- Allows for user to set config file 
- Config file can set defaults for combo box
    - status
    - priority
    - project
    - group
- Added Text box for people (Not reversabliable)

### v2.0 Limitations
- must set defaults in config file, no current error handling
- people cannot be indexed only a string text
- Select box
- No Error Dectetion/Correction
- Due is having some bugs
- Due cannot be cleared
- Must to set in code(no GUI):
    - filename
    - status_values
    - project_values
    - group_values
    - priority_values
- col_offset currently is not set

## v1.0
- Allows for adding new rows during runtime
- Allow for changing values of all colums ['UId', 'Name', 'Status', 'Priority', 'Project', 'Group', 'People', 'Notes', 'Due', 'Last Activity', 'Created']
- Choose which file that will be loading from and saved to 
- allow for loading and saving of dataframe to file
- will automatically loading from filename specified in program 


### v1.0 Limitiations
- Select box and People does nothing
- No Error Dectetion/Correction
- Due is having some bugs
- Due cannot be cleared
- Must to set in code(no GUI):
    - filename
    - status_values
    - project_values
    - group_values
    - priority_values
- col_offset currently is not set
