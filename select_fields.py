import pandas as pd
# import os
# data_path = os.path.dirname(os.path.abspath(__file__))

# Pessoa - Id = , Motorista = A = 0
# PosGeo - Long = B = 1, Lat = C = 2, Bairro = AD = 29, Rua = AE = 30, Cidade = AC = 28, GPS_FILE = AB = 27, Limite_Velocidade = AH = 33, Hierarquia_CWB = AF = 31, Hierarquia_CTB = AG = 32
# Viagem - Data = D = 3, Duracao = M = 12, Km/h = O = 14, Carona = V = 21
# Conduta - Usa_Cinto = W = 22, Usa_Celular = X = 24

# colunas = ["A, B, C, AD, AR, AC, AB, AH, AF, AG, D, M, O, V, W, X"]
colunas = [0, 1, 2, 29, 30, 28, 27, 33, 31, 32, 3, 12, 14, 21, 22, 24]
df = pd.read_excel("Fulltable_20220429_EFGHSTUV 1.xlsx", usecols = colunas)

# Salva o DataFrame no msm diretorio
df.to_csv("dados_filtrados.csv", index = False)