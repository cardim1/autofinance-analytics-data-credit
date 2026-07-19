import pandas as pd
import numpy as np

print("Carregando a base de carros reais da FIPE...")
df_carros = pd.read_csv("fipe_carros_2026.csv")

# Pega apenas os códigos FIPE únicos para associar às simulações dos clientes
codigos_fipe_disponiveis = df_carros["codigo_fipe"].unique()

print("Configurando simulação de crédito da Fintech...")
np.random.seed(42)  # Mantém a consistência dos dados gerados
n_propostas = 100000  # Vamos simular 100 mil propostas de financiamento

dados_financas = {
    "id_proposta": range(200001, 200001 + n_propostas),
    "id_cliente": np.random.randint(10000, 99999, size=n_propostas),
    # Escolhe um carro aleatório da FIPE para cada proposta
    "codigo_fipe": np.random.choice(codigos_fipe_disponiveis, size=n_propostas),
    # Score de Crédito (300 a 1000)
    "score_credito": np.random.randint(300, 1000, size=n_propostas),
    # Renda Mensal simulada entre R$ 3.000 e R$ 30.000
    "renda_mensal": np.round(np.random.uniform(3000, 30000, size=n_propostas), 2),
    # Percentual de entrada que o cliente tem (10% a 70% do valor do carro)
    "percentual_entrada": np.round(np.random.uniform(0.10, 0.70, size=n_propostas), 2)
}

df_credito = pd.DataFrame(dados_financas)

# Salva a tabela de propostas de crédito em CSV
df_credito.to_csv("propostas_credito.csv", index=False)

print(f"Sucesso! O arquivo 'propostas_credito.csv' foi gerado com {len(df_credito)} propostas simuladas.")