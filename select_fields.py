import pandas as pd

import os
data_path = os.path.dirname(os.path.abspath(__file__)) + "/data"
data_prontos = os.path.dirname(os.path.abspath(__file__)) + "/data/prontos"

# Pessoa - Id = , Motorista = A = 0
# PosGeo - Long = B = 1, Lat = C = 2, Bairro = AD = 29, Rua = AE = 30, Cidade = AC = 28, GPS_FILE = AB = 27, Limite_Velocidade = AH = 33, Hierarquia_CWB = AF = 31, Hierarquia_CTB = AG = 32
# Viagem - Data = D = 3, Duracao = M = 12, Km/h = O = 14, Carona = V = 21
# Conduta - Usa_Cinto = W = 22, Usa_Celular = X = 24

# colunas = ["A, B, C, AD, AR, AC, AB, AH, AF, AG, D, M, O, V, W, X"]
# colunas = [0, 1, 2, 29, 30, 28, 27, 33, 31, 32, 3, 12, 14, 21, 22, 24]
df_escola_raw = pd.read_excel(data_path + "/Dados escolas atualizado.xlsx")
df = pd.read_excel(data_path + "/Fulltable_20220429_EFGHSTUV 1.xlsx")

# Salva o DataFrame no msm diretorio
df_escola = df_escola_raw[["CO_ENTIDADE", "DS_ENDERECO", "QT_SALAS_UTILIZADAS", "IN_QUADRA_ESPORTES_COBERTA", "IN_PISCINA"]]
df_estrada = df[["NOME_RUA", "BAIRRO", "CIDADE", "LIMITE_VEL", "HIERARQUIA_CWB", "HIERARQUIA_CTB"]]
# Nao achei o "momento" do trecho
df_trecho = df[["TIME_ACUM", "ALTITUDE_FT", "LONG", "LAT", "PR", "WSB", "UMP_YN", "VALID_TIME", "SPD_KMH", "ACEL_MS2"]]
# Vou precisar mudar esse DAY_CORR para dia e mes
# Nao achei o HoraIncio, HoraTermino e Duracao
df_viagem = df[["DAY_CORRIGIDO", "ID", "GPS_FILE", "PR"]]
df_condutor = df[["DRIVER"]]

# print(df_estrada)
# print(df_trecho)
# print(df_viagem)

df_condutor.to_csv(data_prontos + "/Condutor.csv", index = False)
df_escola.to_csv(data_prontos + "/Escola.csv", index = False)
df_estrada.to_csv(data_prontos + "/Estrada.csv", index = False)
df_trecho.to_csv(data_prontos + "/Trecho.csv", index = False)
df_viagem.to_csv(data_prontos + "/Viagem.csv", index = False)