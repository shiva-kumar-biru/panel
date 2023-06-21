import panel as pn
from Loadcalculation import loadcal
from Rmssimulation import rmscal
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, WheelZoomTool, PanTool, ResetTool, SaveTool, BoxZoomTool
import sys
import powerfactory

def powerfactory_web_interface():
    """
    Runs a web interface for PowerFactory options, which includes LoadFlow Calculations and RMS Simulations and more options.

    The web interface allows the user to select an option (LoadFlow Calculations, RMS Simulations, or ActiveLoad)
    and provides corresponding buttons to perform the selected option. The results are displayed in the interface.

    Returns:
        None
    """
    app = powerfactory.GetApplication()
    app.Show()

    pn.extension()

    options = ["LoadFlow Calculations", "RMS simulations", "ActiveLoad"]
    select = pn.widgets.Select(value=options[0], options=options)

    button_loadcal = pn.widgets.Button(name="Load Calculations", visible=False)
    button_rms = pn.widgets.Button(name="RMS Simulations", visible=False)
    button_activeload = pn.widgets.Button(name="Active Load", visible=False)
    button_column = pn.Column(button_loadcal, button_rms, button_activeload, align="center", visible=False)

    def update_layout(event):
        main_column.clear()
        if select.value == "LoadFlow Calculations":
            button_loadcal.visible = True
            button_rms.visible = False
            button_activeload.visible = False
            button_column.visible = True
            output.object = None
        elif select.value == "RMS simulations":
            button_loadcal.visible = False
            button_rms.visible = True
            button_activeload.visible = False
            button_column.visible = True
            output.object = None
        elif select.value == "ActiveLoad":
            button_loadcal.visible = False
            button_rms.visible = False
            button_activeload.visible = True
            button_column.visible = True
            output.object = None

    select.param.watch(update_layout, "value")

    output = pn.pane.Markdown(" ")

    def LoadCalculations(event):
        result = loadcal()[0:]
        output.object = result
        main_column.clear()

    button_loadcal.on_click(LoadCalculations)

    def RMSSimulations(event):
        createplot(rmscal())

    button_rms.on_click(RMSSimulations)

    def createplot(file_path):
        df = pd.read_csv(str(file_path))
        df = df.rename(columns={r"Network Model\Network Data\Grid\B1\m:u1": "B1voltage"})
        source = ColumnDataSource(df)
        p = figure(title="Curve Plot", plot_width=800, plot_height=400,
                   tools=[WheelZoomTool(), PanTool(), BoxZoomTool(), ResetTool(), SaveTool(),
                          HoverTool(tooltips=[('Time', '@Time'), ('B1voltage', '@B1voltage')])])
        p.line(x='Time', y='B1voltage', source=source, line_width=2)
        plot_widget = pn.pane.Bokeh(p)
        main_column.append((pn.Row(pn.Card(plot_widget))))

    name = pn.pane.Markdown("PowerFactory Options :", style={
        'font-weight': 'bold',
        'font-style': 'italic',
        'color': 'blueviolet',
        'font-size': '15px'
    })

    main_column = pn.Column()

    layout = pn.template.FastListTemplate(
        site="Digsilient",
        title="PowerFactory Web interface",
        sidebar=[name, select],
        main=[button_column, output, main_column],
        header_background='#2a3952',
        accent_base_color="green"
    )
    layout.main.visible = False

    layout.servable()


powerfactory_web_interface()