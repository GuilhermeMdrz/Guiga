print('-=' * 10, 'Atividade 01', '-=' * 10,)
Raio = float(input('Raio do cilíndro: '))
Altura = float(input('Altura do cilíndro: '))
Volume = 3.14 * Raio * Raio * Altura
print(f'O volume desse cilíndro é igual a {Volume}')
print('-=' * 27)

print('-=' * 10, 'Atividade 02', '-=' * 10,)
F = int(input('Temperatura em Fahrenheit: '))
C = (F-32)*(5/9)
print(f'{F}° Fahrenheit correspondem a {C:.1f}° Celsius.')
if C < 17:
    print('Está fazendo frio!')
else:
    if 17 <= C <= 25:
        print('A temperatura está agradável!')
    else:
        print('Está fazendo calor!')
print('-=' * 27)

print('-=' * 10, 'Atividade 03', '-=' * 10,)
Lmaior = float(input('Digite a largura da parede maior: '))
Lmenor = float(input('Digite a largura da parede menor: '))
Altura = float(input('Digite a altura da sua parede: '))
Área = ((Lmaior * Altura) * 2) + ((Lmenor * Altura) * 2) + (Lmaior * Lmenor)
Tinta = Área / 12
print(f'A soma da área das paredes e do teto é igual a {Área}m2. E para pintar essa área serão necessários {Tinta:.2f} baldes de tinta.')
print('-=' * 27)

print('-=' * 10, 'Atividade 04', '-=' * 10,)
num = int(input('Digite um número: '))
if num % 3 == 0:
    print(f'{num} é divisível por 3.')
else:
    print(f'{num} não é divisível por 3.')
if num % 7 == 0:
    print(f'{num} é divisível por 7.')
else:
    print(f'{num} não é divisível por 7.')
print('-=' * 27)

print('-=' * 10, 'Atividade 05', '-=' * 10,)
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} é um número PAR.')
else:
    print(f'{num} é um número ÍMPAR.')
print('-=' * 27)

print('-=' * 10, 'Atividade 06', '-=' * 10,)
dia = int(input('Digite um numero e descubra a qual dia da semana ele corresponde: '))
if dia <= 0:
    print(f'{dia} não corresponde a nenhum dia da semana.')
elif dia == 1:
    print(f'{dia} corresponde a Domingo.')
elif dia == 2:
    print(f'{dia} corresponde a Segunda-feira.')
elif dia == 3:
    print(f'{dia} corresponde a Terça-feira.')
elif dia == 4:
    print(f'{dia} corresponde a Quarta-feira.')
elif dia == 5:
    print(f'{dia} corresponde a Quinta-feira.')
elif dia == 6:
    print(f'{dia} corresponde a Sexta-feira.')
elif dia == 7:
    print(f'{dia} corresponde a Sábado.')
else:
    print(f'{dia} não corresponde a nenhum dia da semana.')
print('-=' * 27)

print('-=' * 10, 'Atividade 07', '-=' * 10,)
velocidade = int(input('Velocidade registrada no sensor: '))
if velocidade <= 50:
    print('Velocidade permitida.')
elif velocidade <= 55:
    print('Advertência.')
elif velocidade <= 65:
    print('Infração leve!')
elif velocidade <= 70:
    print('Infração média!')
elif velocidade <= 75:
    print('Infração grave!')
else:
    print('Infração gravíssima!')
print('-=' * 27)

print('-=' * 10, 'Atividade 08', '-=' * 10,)
nascimento = int(input('Ano de Nascimento:'))
idade = 2024 - nascimento
if idade >= 16:
    print(f'Com {idade} anos você já pode votar!')
    if idade >= 18:
        print('E também já pode tirar a Carteira de Habilitação!')
else:
    print(f'Com {idade } anos você não pode nem votar nem tirar a Carteira de Habilitação')
print('-=' * 27)

print('-=' * 10, 'Atividade 09', '-=' * 10,)
nome = input('Digite seu nome: ')
idade = int(input('Digite quantos anos você tem:'))
dias = 365 * idade
print(f'{nome}, você na viveu no mínimo {dias} dias.')
print('-=' * 27)

print('-=' * 10, 'Atividade 10', '-=' * 10,)
pães = int(input('Quantos pães foram vendidos? '))
broas = int(input('Quantas broas foram vendidas? '))
soma = (pães * 0.6) + (broas * 1.5)
polpança = (soma * 10) / 100
print(f'Ao vender {pães} pães franceses e {broas} broas, foram arrecadados R${soma:.2f}, e devem ser depositados na polpança R${polpança:.2f}. ')
print('-=' * 27)
