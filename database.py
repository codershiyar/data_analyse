import pyodbc
 
conn =  pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=data/DataAnalyse.accdb;')
cursor = conn.cursor()

def drop_table(table_name):
    # execute the SQL query 
    cursor.execute(f"DROP TABLE {table_name}")
    # # commit the changes to the database
    conn.commit()

def insert_word(table_name,word, count ):
    # define the SQL query to insert a new user
    query = f"INSERT INTO {table_name} (word, count) VALUES (?, ?)"
    # execute the SQL query with the values
    cursor.execute(query, word, count)
#         print(f"Word '{word}' is saved in database")
    # commit the changes to the database
    conn.commit()
    
def create_table(table_name, column1,column2):
    # define the SQL query to create a table if it doesn't exist already
    try:
         cursor.execute(f"CREATE TABLE {table_name} (id COUNTER PRIMARY KEY, {column1} TEXT, {column2} INTEGER)")  # execute the SQL query
         conn.commit() 
         print(f"Table '{table_name}' created")   
    except:
          print(f"INFO: Table {table_name} already exists.") # if table already exists python will give an error. in access db there is no 
    

