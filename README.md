# DIgSILENT POWERFACTORY WEB INTERFACE

## *Introduction*

The goal of this project is to create a web interface for visualizing Digsilent Power-Factory simulation data and a basic control system to interact with it, by an open-source Python library "PANEL".

This will streamline the simulation process, which makes it simpler to use as it bypasses the requirement to use Power-Factory directly for repeated tasks.

## *Getting Started*
To get started please refer to the presentation: [link](https://github.com/shiva-kumar-biru/panel/blob/main/Documents/panel_introduction.pptx)

## *Setup Process for Panel*. 

### 1. Setup Virtual environment


1. creates a new folder:  mkdir folder_name
  
2. Navigate to the newly created folder: cd folder_name 

3. Create a virtual environment: python -m venv file_name 

4. Activate the virtual env: file_name\Scripts\activate 



### 2. Installation process.

To use the web interface, you need to install the following libraries:

Panel: pip install panel

Bokeh: pip install bokeh.

Pandas : pip install pandas.

MySQL: pip install mysql-connector-python.

mariadb : pip install mariadb.

--> Please refer to the documentation of each library for further information on usage and features:

Panel Documentation: https://panel.holoviz.org/

Bokeh Documentation: https://docs.bokeh.org/

Pandas Documentation: https://pandas.pydata.org/docs/

MySQL Connector/Python Documentation: https://dev.mysql.com/doc/connector-python/en/

MariaDB Connector/Python Documentation: https://mariadb.com/kb/en/mariadb-connector-python/


## *Files* 

### Panel Files:

1. panel.py: This file sets up a web interface for PowerFactory operations, providing a user-friendly way to perform load calculations, run RMS simulations, and visualize results.
2. loadcalculations.py : This file interacts with the PowerFactory application, and executes a load flow calculation.
3. Rmssimulation.py : This file interacts with the PowerFactory application, and executes a Rmssimulation.


### Database Files:

1. maria.py : This file connects to a MariaDB server, creates a new user and database, creates a table, and loads data from a CSV file into the table.
2. test.py : the file retrieves data from a MariaDB database, creates a line plot using Matplotlib, and displays the plot as an interactive Panel figure.

## *How to run the panel*

Run the following command to run the panel application : 

panel serve <pyfile> --show  --autoreload





## *Documentation and Resources*

Panel website :
https://panel.holoviz.org/

Overview of panel : <a href="https://www.youtube.com/watch?v=1UVghBXt6dY"> YouTube.</a>

Web development resource :  [W3Schools](https://www.w3schools.com/) 

Data Visualization : [link](https://realpython.com/python-data-visualization-bokeh/)


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/shiva-kumar-biru/panel/main)
