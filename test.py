import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import panel as pn

# Connect to the MariaDB server on laptop A
connection = mysql.connector.connect(
    host='192.168.178.53',  # Replace with the IP address or hostname of laptop A
    user='panel1',
    password='panel1',
    database='panel'
)

# Execute the SQL query to fetch the data from the 'plot' table
query = 'SELECT year, percentage FROM paneltable'
df = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Create the plot using Matplotlib
plt.plot(df['year'], df['percentage'])
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.title('Graph of percentage over years')

# Create a Panel figure for interactive plotting
panel_figure = pn.pane.Matplotlib(plt.gcf())

# Display the Panel figure
panel_figure.show()