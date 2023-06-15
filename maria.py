import mariadb

# Connect to the MariaDB server
maria = mariadb.connect(
     host='localhost',
     user='root',  # Replace with your MariaDB username
     password='Shiva@01',  # Replace with your MariaDB password
 )

# # Create a cursor
cursor = maria.cursor()

# # Create a new user
createuser = "CREATE USER 'shiva2'@'localhost' IDENTIFIED BY 'shiva'"
cursor.execute(createuser)

# # Create a new database
createdb = "CREATE DATABASE shiva2"
cursor.execute(createdb)

# # Grant privileges to the user on the database
grant_privileges_query = "GRANT ALL PRIVILEGES ON *.* TO 'shiva2'@'localhost'"
cursor.execute(grant_privileges_query)

# # Switch to the newly created database
use_db_query = "USE shiva2"
cursor.execute(use_db_query)

# # Create a new table
create_table_query = """
CREATE TABLE mytable (
column1 FLOAT,
column2 FLOAT
)
"""
cursor.execute(create_table_query)

# Load data from CSV file into the table
load_data_query = r"""
    LOAD DATA INFILE 'C:\Users\sbiru\Desktop\rmssimfile.csv'
    INTO TABLE mytable
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\\n'
    IGNORE 1 ROWS
    (@var1,@var2)
    SET column1=CAST(@var1 AS FLOAT),
        column2=CAST(@var2 AS FLOAT)
"""
cursor.execute(load_data_query)

# Commit the changes
maria.commit()

# Close the cursor and connection
cursor.close()
maria.close()