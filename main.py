from utils.load_csv import df_from_csv

df = df_from_csv(name="nes_2019_variables", separator=";")
print(df.head())

col9 = df["NES_A01_MEAN9"].apply(lambda x: float(x.replace(",",".")))
col7 = df["NES_A01_MEAN7"].apply(lambda x: float(x.replace(",",".")))
col97 = col9 / col7