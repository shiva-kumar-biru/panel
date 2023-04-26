
import IPython
import panel as pn
import ipywidgets as widgets
from IPython.display import display
from load import loadcal
from rms import rmscal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, WheelZoomTool, PanTool, ResetTool, SaveTool, BoxZoomTool

import sys
sys.path.append(r'C:\Program Files\DIgSILENT\PowerFactory 2022 SP4\Python\3.10')

import powerfactory
app = powerfactory.GetApplication()
app.Show()

pn.extension()

# Define the options and select widget
options = ["LoadCal", "RMS", "ActiveLoad"]
select = pn.widgets.Select(value=options[0], options=options)
# select.servable(target='sidebar')

# Define the buttons for each option and group them in a Column layout object
button_loadcal = pn.widgets.Button(name="Load Calculations", visible=False)
button_rms = pn.widgets.Button(name="RMS", visible=False)
button_activeload = pn.widgets.Button(name="Active Load", visible=False)
button_column = pn.Column(button_loadcal, button_rms, button_activeload, align="center", visible=False)




# Define a function to update the layout based on the selected option
def update_layout(event):
    main_column.clear()
    if select.value == "LoadCal":
        button_loadcal.visible = True
        button_rms.visible = False
        button_activeload.visible = False
        button_column.visible = True
        main_column.clear()
        # layout.main=pn.Column(button_column)

        
    elif select.value == "RMS":
        button_loadcal.visible = False
        button_rms.visible = True
        button_activeload.visible = False
        button_column.visible = True
        main_column.clear()

    elif select.value == "ActiveLoad":
        button_loadcal.visible = False
        button_rms.visible = False
        button_activeload.visible = True
        button_column.visible = True
        main_column.clear()

# Attach the update function to the select widget
select.param.watch(update_layout, "value")

#Load Flow Calculation

output = pn.pane.Markdown(" ")
def Load(event):
    main_column.clear()
    result=loadcal()[0:]
    output.object=result
    # dispaly=pn.Row(pn.pane.markdown(result))
button_loadcal.on_click(Load)

#RMS PLOT 

def on_button_clicked(event):
    # filepath.object = rmscal()
    create_plot(rmscal())


button_rms.on_click(on_button_clicked)


# Define a function to create the plot
def create_plot(file_path):
    # Load data from CSV file
    df = pd.read_csv(str(file_path))
    df = df.rename(columns={r"Network Model\Network Data\Grid\B1\m:u1":"B1voltage"})
    # Define a ColumnDataSource object to hold the data for the plot
    source = ColumnDataSource(df)
    # Create a Bokeh plot
    p = figure(title="Curve Plot", plot_width=800, plot_height=400,
               tools=[WheelZoomTool(), PanTool(), BoxZoomTool(), ResetTool(), SaveTool(), HoverTool(tooltips=[('Time','@Time'),('B1voltage','@B1voltage')])])
    p.line(x='Time', y='B1voltage', source=source, line_width=2)
    # return pn.pane.Bokeh(p)
    plot_widget=pn.pane.Bokeh(p)
    main_column.append((pn.Row(pn.Card(plot_widget))))

# Define the template and layout
name = pn.pane.Markdown("PowerFactory Options :", style={
    'font-weight': 'bold',
    'font-style': 'italic',
    'color': 'blueviolet',
    'font-size': '15px'
})
# .servable(target='sidebar')
main_column=pn.Column()

layout = pn.template.FastListTemplate(
    site="Digsilient",
    title="PowerFactory Web interface",
    sidebar=[name, select],
    main=[button_column,output,main_column],  # Add the button column to the main parameter
    header_background='#2a3952',
    accent_base_color="green"
)
layout.main.visible=False


layout.servable()