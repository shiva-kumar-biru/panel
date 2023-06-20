import sys
sys.path.append(r'C:\Program Files\DIgSILENT\PowerFactory 2022 SP4\Python\3.10')
import powerfactory
def loadcal():
    app = powerfactory.GetApplication()
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
    
      
   
    
    

        
    
	 