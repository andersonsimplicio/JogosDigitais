import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Carregar o conjunto de dados de vinho
data = load_wine()

# Transformar em um DataFrame para facilitar a visualização
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Ver as primeiras linhas do DataFrame
print(df.head())
# Separar as variáveis independentes (X) da variável dependente (y)
X = df.drop('target', axis=1)
y = df['target']

# Dividir em conjunto de treino e teste (80% treino e 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)