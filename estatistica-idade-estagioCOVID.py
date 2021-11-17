 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

df = pd.read_csv('dados-ms.csv', delimiter=";", encoding="latin1")

#Como a idade influencia na sua taxa de internação 

#Age per severity case dataSheet
age_severity_df = pd.read_csv('dados-ms.csv', delimiter=";", encoding="latin1", usecols=['idade', 'evolucaoCaso', ])

# 0 to 14 years old
age14_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 0) & (age_severity_df['idade'] <= 14)]
age_14_totalAmount = age14_severity_df.shape[0]

age_14_death_df = age14_severity_df.loc[(age14_severity_df['evolucaoCaso']) == 'Óbito']
age_14_death_quant = age_14_death_df.shape[0]

age_14_cure_df = age14_severity_df.loc[(age14_severity_df['evolucaoCaso']) == 'Cura']
age_14_cure_quant = age_14_cure_df.shape[0]

age_14_homeTreatment_df = age14_severity_df.loc[(age14_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_14_homeTreatment_quant = age_14_homeTreatment_df.shape[0]

age_14_hospitalized_df = age14_severity_df.loc[(age14_severity_df['evolucaoCaso']) == 'Internado']
age_14_hospitalized_quant = age_14_hospitalized_df.shape[0]

age_14_hospitalizedInICU_df = age14_severity_df.loc[(age14_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_14_hospitalizedInICU_quant = age_14_hospitalizedInICU_df.shape[0]

# 15 to 20 years old
age20_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 15) & (age_severity_df['idade'] <= 20)]
age_20_totalAmount = age20_severity_df.shape[0]

age_20_death_df = age20_severity_df.loc[(age20_severity_df['evolucaoCaso']) == 'Óbito']
age_20_death_quant = age_20_death_df.shape[0]

age_20_cure_df = age20_severity_df.loc[(age20_severity_df['evolucaoCaso']) == 'Cura']
age_20_cure_quant = age_20_cure_df.shape[0]

age_20_homeTreatment_df = age20_severity_df.loc[(age20_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_20_homeTreatment_quant = age_20_homeTreatment_df.shape[0]

age_20_hospitalized_df = age20_severity_df.loc[(age20_severity_df['evolucaoCaso']) == 'Internado']
age_20_hospitalized_quant = age_20_hospitalized_df.shape[0]

age_20_hospitalizedInICU_df = age20_severity_df.loc[(age20_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_20_hospitalizedInICU_quant = age_20_hospitalizedInICU_df.shape[0]

# 21 to 30 years old 
age30_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 21) & (age_severity_df['idade'] <= 30)]
age_30_totalAmount = age30_severity_df.shape[0]

age_30_death_df = age30_severity_df.loc[(age30_severity_df['evolucaoCaso']) == 'Óbito']
age_30_death_quant = age_30_death_df.shape[0]

age_30_cure_df = age30_severity_df.loc[(age30_severity_df['evolucaoCaso']) == 'Cura']
age_30_cure_quant = age_30_cure_df.shape[0]

age_30_homeTreatment_df = age30_severity_df.loc[(age30_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_30_homeTreatment_quant = age_30_homeTreatment_df.shape[0]

age_30_hospitalized_df = age30_severity_df.loc[(age30_severity_df['evolucaoCaso']) == 'Internado']
age_30_hospitalized_quant = age_30_hospitalized_df.shape[0]

age_30_hospitalizedInICU_df = age30_severity_df.loc[(age30_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_30_hospitalizedInICU_quant = age_30_hospitalizedInICU_df.shape[0]

# 31 to 40 years old 
age40_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 31) & (age_severity_df['idade'] <= 40)]
age_40_totalAmount = age40_severity_df.shape[0]

age_40_death_df = age40_severity_df.loc[(age40_severity_df['evolucaoCaso']) == 'Óbito']
age_40_death_quant = age_40_death_df.shape[0]

age_40_cure_df = age40_severity_df.loc[(age40_severity_df['evolucaoCaso']) == 'Cura']
age_40_cure_quant = age_40_cure_df.shape[0]

age_40_homeTreatment_df = age40_severity_df.loc[(age40_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_40_homeTreatment_quant = age_40_homeTreatment_df.shape[0]

age_40_hospitalized_df = age40_severity_df.loc[(age40_severity_df['evolucaoCaso']) == 'Internado']
age_40_hospitalized_quant = age_40_hospitalized_df.shape[0]

age_40_hospitalizedInICU_df = age40_severity_df.loc[(age40_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_40_hospitalizedInICU_quant = age_40_hospitalizedInICU_df.shape[0]

# 41 to 50 years old 
age50_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 41) & (age_severity_df['idade'] <= 50)]
age_50_totalAmount = age50_severity_df.shape[0]

age_50_death_df = age50_severity_df.loc[(age50_severity_df['evolucaoCaso']) == 'Óbito']
age_50_death_quant = age_50_death_df.shape[0]

age_50_cure_df = age50_severity_df.loc[(age50_severity_df['evolucaoCaso']) == 'Cura']
age_50_cure_quant = age_50_cure_df.shape[0]

age_50_homeTreatment_df = age50_severity_df.loc[(age50_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_50_homeTreatment_quant = age_50_homeTreatment_df.shape[0]

age_50_hospitalized_df = age50_severity_df.loc[(age50_severity_df['evolucaoCaso']) == 'Internado']
age_50_hospitalized_quant = age_50_hospitalized_df.shape[0]

age_50_hospitalizedInICU_df = age50_severity_df.loc[(age50_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_50_hospitalizedInICU_quant = age_50_hospitalizedInICU_df.shape[0]

# 51 to 60 years old
age60_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 51) & (age_severity_df['idade'] <= 60)]
age_60_totalAmount = age60_severity_df.shape[0]

age_60_death_df = age60_severity_df.loc[(age60_severity_df['evolucaoCaso']) == 'Óbito']
age_60_death_quant = age_60_death_df.shape[0]

age_60_cure_df = age60_severity_df.loc[(age60_severity_df['evolucaoCaso']) == 'Cura']
age_60_cure_quant = age_60_cure_df.shape[0]

age_60_homeTreatment_df = age60_severity_df.loc[(age60_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_60_homeTreatment_quant = age_60_homeTreatment_df.shape[0]

age_60_hospitalized_df = age60_severity_df.loc[(age60_severity_df['evolucaoCaso']) == 'Internado']
age_60_hospitalized_quant = age_60_hospitalized_df.shape[0]

age_60_hospitalizedInICU_df = age60_severity_df.loc[(age60_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_60_hospitalizedInICU_quant = age_60_hospitalizedInICU_df.shape[0]

# 61 to 70 years old 
age70_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 61) & (age_severity_df['idade'] <= 70)]
age_70_totalAmount = age70_severity_df.shape[0]

age_70_death_df = age70_severity_df.loc[(age70_severity_df['evolucaoCaso']) == 'Óbito']
age_70_death_quant = age_70_death_df.shape[0]

age_70_cure_df = age70_severity_df.loc[(age70_severity_df['evolucaoCaso']) == 'Cura']
age_70_cure_quant = age_70_cure_df.shape[0]

age_70_homeTreatment_df = age70_severity_df.loc[(age70_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_70_homeTreatment_quant = age_70_homeTreatment_df.shape[0]

age_70_hospitalized_df = age70_severity_df.loc[(age70_severity_df['evolucaoCaso']) == 'Internado']
age_70_hospitalized_quant = age_70_hospitalized_df.shape[0]

age_70_hospitalizedInICU_df = age70_severity_df.loc[(age70_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_70_hospitalizedInICU_quant = age_70_hospitalizedInICU_df.shape[0]

# 71 to 80 years old 
age80_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 71) & (age_severity_df['idade'] <= 80)]
age_80_totalAmount = age80_severity_df.shape[0]

age_80_death_df = age80_severity_df.loc[(age80_severity_df['evolucaoCaso']) == 'Óbito']
age_80_death_quant = age_80_death_df.shape[0]

age_80_cure_df = age80_severity_df.loc[(age80_severity_df['evolucaoCaso']) == 'Cura']
age_80_cure_quant = age_80_cure_df.shape[0]

age_80_homeTreatment_df = age80_severity_df.loc[(age80_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_80_homeTreatment_quant = age_80_homeTreatment_df.shape[0]

age_80_hospitalized_df = age80_severity_df.loc[(age80_severity_df['evolucaoCaso']) == 'Internado']
age_80_hospitalized_quant = age_80_hospitalized_df.shape[0]

age_80_hospitalizedInICU_df = age80_severity_df.loc[(age80_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_80_hospitalizedInICU_quant = age_80_hospitalizedInICU_df.shape[0]

# 81 to 90 years old 
age90_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 81) & (age_severity_df['idade'] <= 90)]
age_90_totalAmount = age90_severity_df.shape[0]

age_90_death_df = age90_severity_df.loc[(age90_severity_df['evolucaoCaso']) == 'Óbito']
age_90_death_quant = age_90_death_df.shape[0]

age_90_cure_df = age90_severity_df.loc[(age90_severity_df['evolucaoCaso']) == 'Cura']
age_90_cure_quant = age_90_cure_df.shape[0]

age_90_homeTreatment_df = age90_severity_df.loc[(age90_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_90_homeTreatment_quant = age_90_homeTreatment_df.shape[0]

age_90_hospitalized_df = age90_severity_df.loc[(age90_severity_df['evolucaoCaso']) == 'Internado']
age_90_hospitalized_quant = age_90_hospitalized_df.shape[0]

age_90_hospitalizedInICU_df = age90_severity_df.loc[(age90_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_90_hospitalizedInICU_quant = age_90_hospitalizedInICU_df.shape[0]


# 91 to 110 years old 
age110_severity_df = age_severity_df.loc[(age_severity_df['idade'] >= 91) & (age_severity_df['idade'] <= 110)]
age_110_totalAmount = age110_severity_df.shape[0]

age_110_death_df = age110_severity_df.loc[(age110_severity_df['evolucaoCaso']) == 'Óbito']
age_110_death_quant = age_110_death_df.shape[0]
age_110_death_rate = age_110_death_quant/age_110_totalAmount 
print(age_110_death_rate)

age_110_cure_df = age110_severity_df.loc[(age110_severity_df['evolucaoCaso']) == 'Cura']
age_110_cure_quant = age_110_cure_df.shape[0]
age_110_cure_rate = age_110_cure_quant/age_110_totalAmount 
print(age_110_cure_rate)

age_110_homeTreatment_df = age110_severity_df.loc[(age110_severity_df['evolucaoCaso']) == 'Em tratamento domiciliar']
age_110_homeTreatment_quant = age_110_homeTreatment_df.shape[0]
age_110_homeTreatment_rate = age_110_homeTreatment_quant/age_110_totalAmount 
print(age_110_homeTreatment_rate)

age_110_hospitalized_df = age110_severity_df.loc[(age110_severity_df['evolucaoCaso']) == 'Internado']
age_110_hospitalized_quant = age_110_hospitalized_df.shape[0]
age_110_hospitalized_rate = age_110_hospitalized_quant/age_110_totalAmount 
print(age_110_hospitalized_rate)

age_110_hospitalizedInICU_df = age110_severity_df.loc[(age110_severity_df['evolucaoCaso']) == 'Internado em UTI']
age_110_hospitalizedInICU_quant = age_110_hospitalizedInICU_df.shape[0]
age_110_hospitalizedInICU_rate = age_110_hospitalizedInICU_quant/age_110_totalAmount 
print(age_110_hospitalizedInICU_rate)


#criação de estatisticas a partir dos dados tratados
ageList = ['0-14', '15-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-110'] 
studyListDeath = [age_14_death_quant, age_20_death_quant, age_30_death_quant, age_40_death_quant, age_50_death_quant, age_60_death_quant, age_70_death_quant, age_80_death_quant, age_90_death_quant, age_110_death_quant]
studyList_Hospitalized = [age_14_hospitalized_quant, age_20_hospitalized_quant, age_30_hospitalized_quant, age_40_hospitalized_quant, age_50_hospitalized_quant, age_60_hospitalized_quant, age_70_hospitalized_quant, age_80_hospitalized_quant, age_90_hospitalized_quant, age_110_hospitalized_quant]
studyList_HospitalizedICU = [age_14_hospitalizedInICU_quant, age_20_hospitalizedInICU_quant, age_30_hospitalizedInICU_quant, age_40_hospitalizedInICU_quant, age_50_hospitalizedInICU_quant, age_60_hospitalizedInICU_quant, age_70_hospitalizedInICU_quant, age_80_hospitalizedInICU_quant, age_90_hospitalizedInICU_quant, age_110_hospitalizedInICU_quant]
studyListCure = [age_14_cure_quant, age_20_cure_quant, age_30_cure_quant, age_40_cure_quant, age_50_cure_quant, age_60_cure_quant, age_70_cure_quant, age_80_cure_quant, age_90_cure_quant, age_110_cure_quant]

death_rate = []

#g´rafico da taxa de mortos pela idade 
def death_rate_by_age():
    
    plt.bar(ageList, studyListDeath, label="Óbitos")
    plt.title("Taxa de óbitos pela COVID-19 por idade")
    plt.xlabel("Idade")
    plt.ylabel("Número de mortes")
    plt.legend()
    plt.show()

#relação de internados, internados na uti por idade
def hospitalized_rate_by_age():
    
    plt.bar(ageList, studyList_Hospitalized, label="Internados")
    plt.bar(ageList, studyList_HospitalizedICU, label="Internados na UTI")
    plt.title("Taxa de Internação da COVID-19 por idade")
    plt.xlabel("Idade")
    plt.ylabel("Número de mortes")
    plt.legend()
    plt.show()

#relação de cura por idade
def cure_rate_by_age():

    plt.bar(ageList, studyListCure, label="Quantidade de pacientes curados")
    plt.title("Taxa de Cura da COVID-19 por idade")
    plt.xlabel("Idade")
    plt.ylabel("Número de pacientes curados por idade")
    plt.legend()
    plt.show()

def cure_by_death_by_hospitalized():

    #calcular a porcentagem e fazer o gráfico pela porcentagem 
    
    plt.bar(ageList, studyListCure, label = "Pacientes Curados")
    plt.bar(ageList, studyList_Hospitalized, label = "Internado")
    plt.bar(ageList, studyList_HospitalizedICU, label="Internado na UTI")
    plt.bar(ageList, studyListDeath, label="Óbito")
    plt.title("Relação de mortes, internação e óbito por idade")
    plt.xlabel("Idade")
    plt.ylabel("Estado do Paciente")
    plt.legend()
    plt.show()


#relação de tratamento domicilar por idade
#fazer as porcenagens 

#death_rate_by_age()
#hospitalized_rate_by_age()
#cure_rate_by_age()
#cure_by_death_by_hospitalized()







