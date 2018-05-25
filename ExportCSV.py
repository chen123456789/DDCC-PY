# coding=utf8
# export DDCC to CSV files
import pandas as pd
import DDCC as theDDCC
def export(QualityFactor='ICRP60',Geom='ISO',Organ='Thymus',Gender='Female',particleName='proton'):
    #proton
    if particleName=='proton':
        Energy, dose,factor =theDDCC.DDCC_Proton(QualityFactor,Geom,Organ,Gender)
    elif particleName=='neutron':
        Energy, dose,factor = theDDCC.DDCC_Neutron(QualityFactor, Geom, Organ, Gender)
    elif particleName=='Positive pion' or particleName=='Negative pion':
        Energy, dose,factor = theDDCC.DDCC_Pion(QualityFactor, Geom, Organ, Gender, particleName)
    else:
        Energy, dose,factor,factor = theDDCC.DDCC_Ion(QualityFactor, Geom, Organ, Gender, particleName)
    columns =['#MeV/nuc', '#Absorbed dose','#Quality Factor']
    dataframe = pd.DataFrame({'#MeV/nuc': Energy, '#Absorbed dose': dose,'#Quality Factor':factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    filename = "DDCC-%s.csv" %(particleName)
    dataframe.to_csv(filename, index=False, header=True,sep=',',columns=columns)
def exportAll(QualityFactor='ICRP60',Geom='ISO',Organ='Thymus',Gender='Female'):
    #proton
    Energy, dose, factor = theDDCC.DDCC_Proton(QualityFactor, Geom, Organ, Gender)
    columns = ['#MeV/nuc', 'Absorbed dose', 'Quality Factor']
    dataframe = pd.DataFrame({'#MeV/nuc': Energy, '#Absorbed dose': dose, '#Quality Factor': factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("DDCC-Proton.csv", index=False, header=True, sep=',', columns=columns)
    #neutron
    Energy, dose, factor = theDDCC.DDCC_Neutron( QualityFactor, Geom, Organ, Gender)
    columns = ['#MeV/nuc', 'Absorbed dose', 'Quality Factor']
    dataframe = pd.DataFrame({'#MeV/nuc': Energy, 'Absorbed dose': dose, 'Quality Factor': factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("DDCC-Neutron.csv", index=False, header=True, sep=',', columns=columns)

    # ion z=2~28
    columns = ['#MeV/nuc']
    df= pd.DataFrame()
    particleNames = ['He4','Li7','Be9','B11','C12','N14','O16','F19','Ne20','Na23','Mg24',\
                     'Al27','Si28','P31','S32','Cl35','Ar40','K39','Ca40','Sc45','Ti48',\
                     'V51','Cr52','Mn55','Fe56','Co59','Ni59']
    for particleName in particleNames:
        columns.append('Absorbed dose')
        columns.append('Quality Factor')
        Energy, dose, factor  = theDDCC.DDCC_Ion(QualityFactor, Geom, Organ, Gender, particleName)
        df['MeV/nuc'] = Energy
        df['Absorbed dose']= dose
        df['Quality Factor'] = factor
    df.to_csv("DDCC-Ion.csv", index=False, header=True, sep=',', columns=columns)
def export_Dose_equivalent(QualityFactor='ICRP60',Geom='ISO',Organ='Effective',Gender='Male'):
    #proton
    energy, dose, factor = theDDCC.DDCC_Proton('ICRP60','ISO', Organ, Gender)
    columns = ['MeV/nuc', 'proton']
    dataframe = pd.DataFrame({'MeV/nuc': energy, 'proton': dose*factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("DDCC-Proton.csv", index=False, header=True, sep=',', columns=columns)
    #neutron
    energy, dose, factor = theDDCC.DDCC_Neutron( 'ICRP60','ISO', Organ, Gender)
    columns = ['MeV/nuc', 'neutron']
    dataframe = pd.DataFrame({'MeV/nuc': energy, 'neutron': dose*factor})
    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("DDCC-Neutron.csv", index=False, header=True, sep=',', columns=columns)

    # ion z=2~28
    columns = ['MeV/nuc']
    df= pd.DataFrame()
    particleNames = ['He4','Li7','Be9','B11','C12','N14','O16','F19','Ne20','Na23','Mg24',\
                     'Al27','Si28','P31','S32','Cl35','Ar40','K39','Ca40','Sc45','Ti48',\
                     'V51','Cr52','Mn55','Fe56','Co59','Ni59']
    for particleName in particleNames:
        columns.append(particleName)
        energy, dose, factor  = theDDCC.DDCC_Ion(QualityFactor, Geom, Organ, Gender, particleName)
        df['MeV/nuc'] = energy
        df[particleName]= dose*factor
    df.to_csv("DDCC-Ion.csv", index=False, header=True, sep=',', columns=columns)
export_Dose_equivalent()