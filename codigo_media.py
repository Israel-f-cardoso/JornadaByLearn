def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno tirou', media)
  return media

def verificar_aprovacao(media):
  if media >= 7:
    print('Aluno Aprovado :)')
  else:
    print('Aluno Reprovado :(')

aluno = [10 , 8, 9 , 2]
media = calcular_media(aluno)
verificar_aprovacao(media)