import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import os # Importa a biblioteca os para interagir com o sistema operacional
import glob# Importa a biblioteca glob para encontrar arquivos que correspondem a um padrão específico


def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame: 
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) # Encontra todos os arquivos JSON na pasta especificada
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] # Lê cada arquivo JSON em um DataFrame do pandas e armazena em uma lista
    df_total = pd.concat(df_list, ignore_index=True) # Concatena todos os DataFrames em um único DataFrame
    return df_total # Retorna o DataFrame consolidado


def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"] # Cria uma nova coluna "Total" que é o produto da quantidade vendida pelo valor de venda
    return df # Retorna o DataFrame atualizado


def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in formato_saida: # Itera sobre os formatos de saída especificados
        if formato == 'csv':
            df.to_csv("dados.csv", index=False) # Salva o DataFrame como um arquivo CSV
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False) # Salva o DataFrame como um arquivo Parquet


def pipeline_calcular_kpi_de_vendas_consolidada(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta) # Extrai e consolida os dados dos arquivos JSON
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame) # Calcula o KPI de total de vendas
    carregar_dados(data_frame_calculado, formato_de_saida) # Salva os dados calculados nos formatos especificados