def menorFaturamento(faturamentos):
  menorFaturamento = faturamentos[0]

  for faturamentoDiario in faturamentos:
    if((faturamentoDiario != 0.0) & (faturamentoDiario < menorFaturamento)):
      menorFaturamento = faturamentoDiario
  return menorFaturamento

def maiorFaturamento(faturamentos):
  maiorFaturamento = 0.0

  for faturamentoDiario in faturamentos:
    if((faturamentoDiario != 0.0) & (faturamentoDiario > maiorFaturamento)):
      maiorFaturamento = faturamentoDiario
  return maiorFaturamento

def mediaMensal(faturamentos):
  faturamentoMensal = 0.0
  diasDoMes = 0.0

  for faturamentoDiario in faturamentos:
    if((faturamentoDiario != 0.0)):
      faturamentoMensal += faturamentoDiario
      diasDoMes += 1.0

  return (faturamentoMensal/diasDoMes)