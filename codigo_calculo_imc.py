def numero_quadrado(numero):
  quadrado = numero * numero
  return quadrado

def imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada
  return meu_imc

meu_imc = imc(79, 1.70)
print(f'O meu imc é {meu_imc:.2f}')