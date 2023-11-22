import sys
import powfacpy
import os
import json

def load_settings():
    """
    This function loads user specific settings from the json file named settigs.json.
    Returns:
        dict : A python dictionary conatinng the loaded settings
    """

    settings_file = "settings.json"
    with open(settings_file,"r") as file:
        settings=json.load(file)
    return settings    

path=load_settings();
powerfactorypath=path["powerfactorypath"]
sys.path.append(powerfactorypath)  
import powerfactory
app = powerfactory.GetApplication()
app.Show()


def loadcal():
    """
    This function performs load flow calculations.
    Returns:
        str : A string containing the voltage values of the Buses.
    """
    # app = powerfactory.GetApplication()
    proj=app.ActivateProject('practice')
    app.PrintPlain(proj)
    s=app.GetProjectFolder('study')
    app.PrintPlain(s)
    b=app.GetFromStudyCase('study')
    app.PrintPlain(b)
    ldf = app.GetFromStudyCase('ComLdf')
    ldf.Execute()
    #Get load flow object from study case
    Buses = app.GetCalcRelevantObjects('*.ElmTerm')
    output=''
    for Bus in Buses:
        if Bus.HasAttribute('m:u'):
            name = Bus.loc_name
            voltage = Bus.GetAttribute('m:u')      
            output+='voltage of the %s =%.2f p.u.\n' %(name,voltage)
    return output
    
def rmscal():
    """
    This function performs the RMS simulation and exports the simulation results to a CSV file.
    Returns:
        str: The filepath of the exported CSV file containing the simulation results.
    """
    # app = powerfactory.GetApplication()
    pfbi = powfacpy.PFBaseInterface(app)
    proj=app.ActivateProject('practice')
    app.PrintPlain(proj)
    #Get load flow object from study case
    ldf=app.GetFromStudyCase('Comldf')
    ldf.Execute()
    
    pfds = powfacpy.PFDynSimInterface(app)
    pfds.initialize_and_run_sim()
    # filepath=r"C:\Users\sbiru\Desktop\rmssimfile"
    user_setting = load_settings()
    filepath = user_setting["rmsfilepath"]
    
    filedir = os.path.dirname(filepath)
    filename = os.path.basename(filepath) 
    csv_filename = os.path.splitext(filename)[0] + ".csv"  # Add the .csv extension
    csv_filepath = os.path.join(filedir, csv_filename)  # Combining the directory and filename into a full filepath
    
    pfds.export_to_csv(dir=filedir, file_name=filename)
    
    return csv_filepath
    
   
   
    
    

        
    
	 