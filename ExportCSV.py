# coding=utf8
# export DDCC to CSV files
import pandas as pd
import DDCC as theDDCC
def export(QualityFactor='ICRP60',Geom='Ap',Organ='Thymus',Gender='Female',particleName='proton'):
    #proton
    if particleName=='proton':
        Energy, dose,factor =theDDCC.DDCC_Proton(DoseType,QualityFactor,Geom,Organ,Gender)
        columns =['#MeV/nuc', '#Absorbed dose','#Quality Factor']
        dataframe = pd.DataFrame({'#MeV/nuc': Energy, '#Absorbed dose': dose,'#Quality Factor':factor})
        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv("DDCC-Proton.csv", index=False, header=True,sep=',',columns=columns)
    elif particleName=='neutron':
        Energy, dose = theDDCC.DDCC_Neutron(DoseType, QualityFactor, Geom, Organ, Gender)
    elif particleName=='Positive pion' or particleName=='Negative pion':
        Energy, dose = theDDCC.DDCC_Pion(DoseType, QualityFactor, Geom, Organ, Gender, particleName)
    else:
        Energy, dose = theDDCC.DDCC_Ion(DoseType, QualityFactor, Geom, Organ, Gender, particleName)
def exportAll(QualityFactor='ICRP60',Organ='Thymus',Gender='Female'):
    #proton
    Energy, dose, factor = theDDCC.DDCC_Proton(DoseType, QualityFactor, Geom, Organ, Gender)
    columns = ['#MeV/nuc', '#Absorbed dose', '#Quality Factor']
    dataframe = pd.DataFrame({'#MeV/nuc': Energy, '#Absorbed dose': dose, '#Quality Factor': factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("DDCC-Proton.csv", index=False, header=True, sep=',', columns=columns)
    #neutron
    Energy, dose, factor = theDDCC.DDCC_Neutron(DoseType, QualityFactor, Geom, Organ, Gender)
    columns = ['#MeV/nuc', '#Absorbed dose', '#Quality Factor']
    dataframe = pd.DataFrame({'#MeV/nuc': Energy, '#Absorbed dose': dose, '#Quality Factor': factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("DDCC-Neutron.csv", index=False, header=True, sep=',', columns=columns)
    # ion z=2~28
    for Z in range(2,29,1):
        columns.

export()