import json

with open('dados.json') as f:
    dados = json.load(f)

valores = [d['valor'] for d in dados if d['valor'] > 0]

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for v in valores if v > media)

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
