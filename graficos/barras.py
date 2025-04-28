import pandas as pd
import numpy as np

# Carregar os dados do CSV diretamente da URL
url = 'https://raw.githubusercontent.com/Ujeverson/datasets/main/insect.csv'
df = pd.read_csv(url)

# Exibir as primeiras linhas do DataFrame para conferência
print(df.head())


