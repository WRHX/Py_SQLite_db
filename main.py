import sqlite3
#===============================FUNCTION DEFINITIONS============================
def db_AddPerson():
    "Add person to the database table People"
    name = input('Please input the (front) name:\n')
    surname = input('Please input the surname:\n')
    age = input('Please input the Age:\n')
    city = input('Please input the City:\n')
    #make connection to database, add to table and close connection
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO People VALUES (?,?,?,?)",(name,surname,age,city))
    conn.commit()
    conn.close()
    return('Succesfully added '+ name + surname + ' to the table')

def db_DisplayPerson():
    "Display person from table"
    name = input('Please enter first name of person:\n')
    #connect to db and look for people with this name
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    for person in c.execute("SELECT * FROM People WHERE name =?", (name,)):
        print(person)
    surname = input('Please enter surname of person:\n')
    conn.close()
    return()

#============================================PROGRAM===============================
existence = 1;
while existence == 1:
    base = input('Welcome, do you wish to mutate? [y/n]\n') 

    if base == 'y':
        ans = int(input('Select mutation:\n\
        1. Add to database.\n\
        2. Display information.\n'))
        if ans == 1:
            db_AddPerson()
        elif ans == 2:
            db_DisplayPerson()
        existence = 1;
    else:
        input('Press any key to leave')
        existence = 0;


    
    


    


    
