def rmscal():
    import sys
    sys.path.append(r'C:\Program Files\DIgSILENT\PowerFactory 2022 SP4\Python\3.10')
    import powerfactory
    import powfacpy
    import os
    
    app = powerfactory.GetApplication()
    pfbi = powfacpy.PFBaseInterface(app)
    proj=app.ActivateProject('practice')
    app.PrintPlain(proj)
    #Get load flow object from study case
    ldf=app.GetFromStudyCase('Comldf')
    ldf.Execute()
    
    pfds = powfacpy.PFDynSimInterface(app)
    pfds.initialize_and_run_sim()
    filepath=r"C:\Users\sbiru\Desktop\rmscsvfile"
    
    filedir = os.path.dirname(filepath)
    filename = os.path.basename(filepath) 
    csv_filename = os.path.splitext(filename)[0] + ".csv"  # Add the .csv extension
    csv_filepath = os.path.join(filedir, csv_filename)  # Combine the directory and filename into a full filepath
    
    pfds.export_to_csv(dir=filedir, file_name=filename)
    
    return csv_filepath
    
    # filedir=os.path.dirname(filepath)
    # filename=os.path.basename(filepath) 
    # pfds.export_to_csv(dir=filedir,file_name=filename)
    # return filename


    # path=pfbi.get_obj('Study Cases\Study Case\Result Export.ComRes')
    # path.f_name=r"C:\Users\sbiru\Desktop\rmsfile.csv"
    # file=app.obj.f_name
    # app.PrintPlain(file)
    
    