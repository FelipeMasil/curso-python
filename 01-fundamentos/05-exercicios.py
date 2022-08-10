# Crie um programa que imprima os principais indicadores da loja de bebidas no ultimo ano;

qtdeCoca = float(input(f'Quantidade de Coca-Cola: '))
qtdePepsi = float(input(f'Quantidade de Pepsi: '))

precoCoca = float(input(f'Preço unitário Coca: '))
precoPepsi = float(input(f'Preço unitário Pepsi: '))

custoLoja = float(input('Custo da loja: '))

coca = qtdeCoca * precoCoca
pepsi = qtdePepsi * precoPepsi

faturamento = format((coca + pepsi) - custoLoja, '.2f')

print('O faturamento anual da loja foi de R$' + str(faturamento))
