# importando as bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# importando os dados  de treinamento
dados_train = pd.read_csv("train.csv")
dados_train.head(5)
# Fazendo analise dos dados
dados_train.describe()

# Informações
dados_train.info()
"""
    As informações mostram que não tem dados faltantes
"""
dados_train.columns
dados_train.hist(bins=30, figsize=(30, 15))
plt.show()

# analise de variaveis unidmensintal
dados_train["Region"].unique()

dados_train["Region"].value_counts()


def grafico_tipo_objeto(dados):
    contagem_categoricas = dados.value_counts()
    contagem_categoricas.plot(kind="bar")

    plt.title("Frequência da categorias")
    plt.xlabel("Categoria")
    plt.ylabel("Contagem")

    plt.show()
