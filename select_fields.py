import pandas as pd

df = pd.read_excel("Fulltable_20220429_EFGHSTUV 1.xlsx", usecols = "A,B")

print(type(df))