import json

def calcular_faturamento(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        dados = json.load(arquivo)

    faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

    if not faturamentos:
        return None, None, 0

    menorf = min(faturamentos)
    maiorf = max(faturamentos)
    mediam = sum(faturamentos) / len(faturamentos)

    acima_da_media = sum(1 for valor in faturamentos if valor > mediam)

    return menorf, maiorf, acima_da_media

caminho_arquivo = r"3\faturamento.json"

menor, maior, acima_media = calcular_faturamento(caminho_arquivo)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média mensal: {acima_media}")
