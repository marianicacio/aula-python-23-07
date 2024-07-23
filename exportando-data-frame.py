import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'Dias1e2.xlsx'
arquivo_excel_2 = 'Dias3.xlsx'

#ler o conteudo e mandar para a variavel => Data Frame df
df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='Dia 1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='Dia 2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

print(df_dia_1)