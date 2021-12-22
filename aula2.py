a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))



soma = a+ b
substracao = a - b
multiplicacao = a * b
divicao = a / b
resto = a % b

print('soma: {soma}. '
      '\n Subtração: {sub} '
      '\n Multiplicação: {multi} \n '
      'Divição: {div} '
      '\n Resto: {resto}'.format(soma = soma,sub = substracao,multi = multiplicacao,div = divicao,resto = resto))
