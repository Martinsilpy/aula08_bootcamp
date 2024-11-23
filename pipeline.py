from etl import pipeline_calcular_kpi_de_vendas_consolidada

pasta_argumento: str = 'data' # Define o diretório onde os dados estão armazenados
formato_de_saida: list = ["csv"] # Define os formatos de saída desejados

pipeline_calcular_kpi_de_vendas_consolidada(pasta_argumento, formato_de_saida) # Executa a função pipeline para calcular o KPI de vendas consolidadas