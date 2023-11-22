#Importing the modules
import panel as pn  
from power_factory_file import loadcal,rmscal                
import pandas as pd                   
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, WheelZoomTool, PanTool, ResetTool, SaveTool, BoxZoomTool

pn.extension()  # extensions for the panel libraries

# Defining the options and select widget
options = ["LoadFlow Calculations", "RMS simulations", "ActiveLoad"]
select = pn.widgets.Select(value=options[0], options=options)

# Defining the widgets
# Defining the buttons for each option 

button_loadcal = pn.widgets.Button(name="Load Calculations", visible=False)
button_rms = pn.widgets.Button(name="RMS Simulations", visible=False)
button_activeload = pn.widgets.Button(name="Active Load", visible=False)
button_column = pn.Column(button_loadcal, button_rms, button_activeload, align="center", visible=False)

# Defining a function to update the layout based on the selected option
def update_layout(event):
    if select.value == "LoadFlow Calculations":
        button_loadcal.visible = True
        button_rms.visible = False
        button_activeload.visible = False
        button_column.visible = True
        
    elif select.value == "RMS simulations":
        button_loadcal.visible = False
        button_rms.visible = True
        button_activeload.visible = False
        button_column.visible = True

    elif select.value == "ActiveLoad":
        button_loadcal.visible = False
        button_rms.visible = False
        button_activeload.visible = True
        button_column.visible = True

# Attach the update function to the select widget
select.param.watch(update_layout, "value")

#Load Flow Calculation

output = pn.pane.Markdown(" ")

# Function to calculate the LoadFlow Calculations

def LoadCalculations(event):
    result=loadcal()[0:]
    output.object=result
button_loadcal.on_click(LoadCalculations)

#RMS PLOT 

# Function to run the RMS simulation

def RMSSimulations(event):
    # filepath.object = rmscal()
    createplot(rmscal())
button_rms.on_click(RMSSimulations)

# Define a function to create the plot

def createplot(file_path):
    # Load the data from CSV file
    df = pd.read_csv(str(file_path))
    df = df.rename(columns={r"Network Model\Network Data\Grid\B1\m:u1":"B1voltage"})
    source = ColumnDataSource(df)
    # Create a Bokeh plot
    p = figure(title="Curve Plot",
               tools=[WheelZoomTool(), PanTool(), BoxZoomTool(), ResetTool(), SaveTool(), HoverTool(tooltips=[('Time','@Time'),('B1voltage','@B1voltage')])])
    p.line(x='Time', y='B1voltage', source=source, line_width=2)
    plot_widget=pn.pane.Bokeh(p)
    main_column.append((pn.Row(pn.Card(plot_widget))))

# Define the template and layout
name = pn.pane.Markdown("PowerFactory Options :", style={
    'font-weight': 'bold',
    'font-style': 'italic',
    'color': 'blueviolet',
    'font-size': '15px'
})

main_column=pn.Column()

# Template of panel "FastListTemplate"
layout = pn.template.FastListTemplate(
    site="Digsilient",
    title="PowerFactory Web interface",
    sidebar=[name, select], # Sidebar components for user interface
    main=[button_column,output,main_column],  # Add the button column to the main parameter
    header_background='#2a3952',
    accent_base_color="green"
)
layout.main.visible=False
layout.servable() # this is used to serve the panel as a webpplication