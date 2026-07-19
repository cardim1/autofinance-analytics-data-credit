import pandas as pd
from datasets import load_dataset

print("Conectando ao Hugging Face e baixando os dados de forma otimizada...")

# 1. Carrega o dataset usando streaming (não baixa o arquivo de 900MB inteiro de vez)
dataset = load_dataset("alanwgt/fipex-veiculos-brasil", split="train", streaming=True)

print("Filtrando os dados para carros de 2026 (Meses 1 a 6)...")

# 2. Aplica os filtros idênticos aos que você validou na query do site
dataset_filtrado = dataset.filter(
    lambda x: x["tipo_veiculo"] == "carro" 
    and x["ano_referencia"] == 2026 
    and 1 <= x["mes_referencia"] <= 6
)

# 3. Converte o resultado filtrado para um DataFrame do Pandas
df_fipe = pd.DataFrame(list(dataset_filtrado))

# 4. Salva o arquivo CSV limpo para ser utilizado
df_fipe.to_csv("fipe_carros_2026.csv", index=False)

print(f"Sucesso! O arquivo 'fipe_carros_2026.csv' foi gerado com {len(df_fipe)} linhas.")