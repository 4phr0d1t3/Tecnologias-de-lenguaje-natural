import pandas as pd

df = pd.read_csv('corpus_noticias.csv', sep='&&&&&&&&', lineterminator='\r', header=None, engine='python')
print(df)