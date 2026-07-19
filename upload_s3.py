import boto3
import os

# CONFIGURAÇÃO: Altere o nome do bucket. 
# Lembra que nomes de buckets no S3 precisam ser únicos no mundo todo, 
# então coloque algo bem específico com seu nome!
NOME_BUCKET = "autofinance-analytics-pipeline-gabriel-cardim" 
REGIAO = "us-east-1"  

# Inicializa o cliente do S3 usando as credenciais do seu computador
s3_client = boto3.client('s3', region_name=REGIAO)

def iniciar_pipeline():
    try:
        # 1. Cria o Bucket no S3
        print(f"Criando o bucket '{NOME_BUCKET}' na AWS...")
        s3_client.create_bucket(Bucket=NOME_BUCKET)
        print("Bucket criado com sucesso!\n")
    except Exception as e:
        # Caso o bucket já tenha sido criado por você antes, ele pula essa etapa
        print(f"Aviso/Erro no bucket: {e}\n")

    # 2. Dicionário mapeando o arquivo local para o caminho desejado no S3 (Data Lake)
    arquivos_para_upload = {
        "fipe_carros_2026.csv": "raw/dados_fipe/fipe_carros_2026.csv",
        "propostas_credito.csv": "raw/dados_credito/propostas_credito.csv"
    }
    
    # 3. Loop para fazer o upload dos arquivos
    print("Iniciando o upload dos dados para o S3...")
    for arquivo_local, caminho_s3 in arquivos_para_upload.items():
        if os.path.exists(arquivo_local):
            print(f"-> Enviando {arquivo_local}...")
            s3_client.upload_file(arquivo_local, NOME_BUCKET, caminho_s3)
            print(f"   Sucesso: Salvo em s3://{NOME_BUCKET}/{caminho_s3}")
        else:
            print(f"⚠️ Erro: O arquivo local '{arquivo_local}' não foi encontrado na pasta.")
            
    print("\n[ETAPA CONCLUÍDA]: Seus dados estão seguros na nuvem da AWS!")

if __name__ == "__main__":
    iniciar_pipeline()