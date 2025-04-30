
#1. Construir um algoritmo para calcular e apresentar o total de salários pagos de funcionários, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no salário para sair.
# não podemos usar o for porque precisa de um valor
# numérico para indicar a quantidade de repetições
# na função range(), exemplo for contador in range(7)
total = 0
salario = float(input('Digite o salario: '))#O salario vai ser registrado 1 vez ate entrar no laço
while salario > 0:
  total = total + salario


  salario = float(input('Digite o salario: '))#será repitido até o salario "der pal" no while (a condição não ser mais aceita)
  print('total dos salarios:',total)