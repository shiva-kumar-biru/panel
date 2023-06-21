import sys
sys.path.append(r'C:\Program Files\DIgSILENT\PowerFactory 2022 SP4\Python\3.10')
import powerfactory
import powfacpy
import os
def rmscal():
    """
    This function performs the RMS simulation and exports the simulation results to a CSV file.
    Returns:
        str: The filepath of the exported CSV file containing the simulation results.
    """
    app = powerfactory.GetApplication()
    pfbi = powfacpy.PFBaseInterface(app)
    proj=app.ActivateProject('practice')
    app.PrintPlain(proj)
    #Get load flow object from study case
    ldf=app.GetFromStudyCase('Comldf')
    ldf.Execute()
    
    pfds = powfacpy.PFDynSimInterface(app)
    pfds.initialize_and_run_sim()
    filepath=r"C:\Users\sbiru\Desktop\rmssimfile"
    
    filedir = os.path.dirname(filepath)
    filename = os.path.basename(filepath) 
    csv_filename = os.path.splitext(filename)[0] + ".csv"  # Add the .csv extension
    csv_filepath = os.path.join(filedir, csv_filename)  # Combining the directory and filename into a full filepath
    
    pfds.export_to_csv(dir=filedir, file_name=filename)
    
    return csv_filepath
    
   