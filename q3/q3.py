import json
import faturamento

with open("dados.json", encoding='utf-8') as dados_json: dados = json.load(dados_json)

faturamentos = []

for dado in dados:
    faturamentos.append(dado['valor'])

menorFaturamento = faturamento.menorFaturamento(faturamentos)
maiorFaturamento = faturamento.maiorFaturamento(faturamentos)
mediaMensal = faturamento.mediaMensal(faturamentos)
diasDoMes = 0

print(f'Menor faturamento: {menorFaturamento:.2f}')
print(f'Maior faturamento: {maiorFaturamento:.2f}')

for faturamentoDiario in faturamentos:
  if((faturamentoDiario != 0.0) & (faturamentoDiario > mediaMensal)):
    diasDoMes += 1

print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", diasDoMes)