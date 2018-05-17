# coding=utf8
import pandas as pd
import numpy as np
def DDCC_Proton(QualityFactor='ICRP60',Geom='ISO',Organ='Thymus',Gender='Female'):

    xls = pd.ExcelFile("ICRP123/proton.xls")
    sheetX = xls.parse(0) #data

    QualityFactors  = sheetX.ix[0:1,3]
    Geoms           = sheetX.ix[0:5,4]
    Organs          = sheetX.ix[0:30,5]
    Genders         = sheetX.ix[0:1,6]
    EnergySize      = int(sheetX.ix[0:0,1])
    #
    Organs_Index = np.where(Organs == Organ)[0]+1
    Genders_Index = np.where(Genders == Gender)[0]+1
    QualityFactors_Index = np.where(QualityFactors == QualityFactor)[0]+1

    if Organs_Index[0]==1:
        gray_index = 3-2
        factor_index = QualityFactors_Index[0]+3-2
    else:
        gray_index   = (Organs_Index[0])*6+(Genders_Index[0])*3+1-10-2
        factor_index = (Organs_Index[0])*6+(Genders_Index[0])*3+1+QualityFactors_Index[0]-10-2
    #print gray_index,factor_index

    sheetX = xls.parse(1)  # proton

    Energy = sheetX.ix[:,0]

    absorbed_dose = sheetX.ix[:,gray_index]

    factor = sheetX.ix[0:EnergySize, factor_index]

        #品质因子
    return Energy, absorbed_dose,factor
def DDCC_Neutron(QualityFactor='ICRP60',Geom='Ap',Organ='Thymus',Gender='Female'):

    xls = pd.ExcelFile("ICRP123/neutron.xls")
    sheetX = xls.parse(0) #data

    QualityFactors  = sheetX.ix[0:1,3]
    Geoms           = sheetX.ix[0:5,4]
    Organs          = sheetX.ix[0:30,5]
    Genders         = sheetX.ix[0:1,6]
    EnergySize      = int(sheetX.ix[0:0,1])
    #
    Organs_Index = np.where(Organs == Organ)[0]+1
    Genders_Index = np.where(Genders == Gender)[0]+1
    QualityFactors_Index = np.where(QualityFactors == QualityFactor)[0]+1

    if Organs_Index[0]==1:
        gray_index = 3-2
        factor_index = QualityFactors_Index[0]+3-2
    else:
        gray_index   = (Organs_Index[0])*6+(Genders_Index[0])*3+1-10-2
        factor_index = (Organs_Index[0])*6+(Genders_Index[0])*3+1+QualityFactors_Index[0]-10-2
    #print gray_index,factor_index

    sheetX = xls.parse(1)  # proton

    Energy = sheetX.ix[:,0]

    absorbed_dose = sheetX.ix[:,gray_index]

    factor = sheetX.ix[0:EnergySize, factor_index]
    return Energy, absorbed_dose, factor

def DDCC_Ion(QualityFactor='ICRP60',Geom='Ap',Organ='Thymus',Gender='Female',particleName='He4'):

    xls = pd.ExcelFile("ICRP123/ion.xls")
    sheetX = xls.parse(0) #data
    EnergySize = int(sheetX.ix[0:0,1])
    QualityFactors  = sheetX.ix[0:1,3]
    Particles       = sheetX.ix[0:27,4]
    Organs          = sheetX.ix[0:30,5]
    Genders         = sheetX.ix[0:1, 6]

    #
    Organs_Index = np.where(Organs == Organ)[0]+1
    Genders_Index = np.where(Genders == Gender)[0]+1
    QualityFactors_Index = np.where(QualityFactors == QualityFactor)[0]+1

    if Organs_Index[0]==1:
        gray_index = 3-2
        factor_index = QualityFactors_Index[0]+3-2
    else:
        gray_index   = (Organs_Index[0])*6+(Genders_Index[0])*3+1-10-2
        factor_index = (Organs_Index[0])*6+(Genders_Index[0])*3+1+QualityFactors_Index[0]-10-2
    #print gray_index,factor_index
    #
    Particles_Index = np.where(Particles == particleName)[0]+1

    sheetX = xls.parse(Particles_Index[0])  # Ion

    Energy = sheetX.ix[:,0]

    absorbed_dose = sheetX.ix[:,gray_index]

    factor = sheetX.ix[0:EnergySize, factor_index]
    return Energy, absorbed_dose, factor

def DDCC_Pion(QualityFactor='ICRP60',Geom='Ap',Organ='Liver',Gender='Male',particleName='Positive pion'):

    xls = pd.ExcelFile("ICRP123/pion.xls")
    sheetX = xls.parse(0) #data
    EnergySize = int(sheetX.ix[0:0,1])

    QualityFactors  = sheetX.ix[0:1,3]
    Particles       = sheetX.ix[0:27,4]
    Organs          = sheetX.ix[0:30,5]
    Genders         = sheetX.ix[0:1, 6]

    #

    Organs_Index = np.where(Organs == Organ)[0]+1
    Genders_Index = np.where(Genders == Gender)[0]+1
    QualityFactors_Index = np.where(QualityFactors == QualityFactor)[0]+1

    if Organs_Index[0]==1:
        gray_index = 3-2
        factor_index = QualityFactors_Index[0]+3-2
    else:
        gray_index   = (Organs_Index[0])*6+(Genders_Index[0])*3+1-10-2
        factor_index = (Organs_Index[0])*6+(Genders_Index[0])*3+1+QualityFactors_Index[0]-10-2
    #print gray_index,factor_index
    #
    Particles_Index = np.where(Particles == particleName)[0]+1

    sheetX = xls.parse(Particles_Index[0])  # Ion

    Energy = sheetX.ix[:,0]

    absorbed_dose = sheetX.ix[:,gray_index]

    factor = sheetX.ix[0:EnergySize, factor_index]
    return Energy, absorbed_dose, factor
#DDCC_Pion()