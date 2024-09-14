print('-=' * 10, 'Atividade 01', '-=' * 10,)
num1 = float(input('Primeira nota:'))
num2 = float(input('Segunda nota:'))
média = (num1 + num2) / 2
print(f'A média aritmética entre {num1} e {num2} é igual a {média:.2f}')
print('-=' * 27)

print('-=' * 10, 'Atividade 02', '-=' * 10,)
anos = int(input('Digite quantos anos você tem de serviço:'))
valor = int(input('Digite o valor da bonificação: R$'))
bonificação = anos * valor
print(f'Você recebera uma bonificação de R${bonificação:.2f}')
print('-=' * 27)

print('-=' * 10, 'Atividade 03', '-=' * 10,)
nome = input('Nome de produto:')
produto = float(input('Valor do produto: R$'))
desconto = int(input('Valor do desconto:'))
valor = produto - (produto * desconto / 100)
print(f'O produto {nome} após um desconto de {desconto}% custará R${valor:.2f}')
print('-=' * 27)
