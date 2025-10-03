print('Bem vindo a Fábrica de Camisetas do Khauan Gabriel')


def escolha_modelo():
    #loop para que coloque a opcao correta caso erre ou digite uma inesistente
    while True:
        print('''
Entre com o modelo desejado
MCS - Manga Curta Simples
MLS - Manga Longa Simples
MCE - Manga Curta Com Estampa
MLE - Manga Longa Com Estampa
''')
        modelo = input('>>').upper()
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else:
            #caso coloque a opcao inesistente
            print('Escolha inválida, entre com o modelo novamente\n')


def num_camisetas():
    while True:
        try:
            num = int(input('Entre com o número de camisetas: '))
            if num > 20000:
                print(
                    'Não aceitamos tantas camisetas de uma vez.\nPor favor, entre com o número de camisetas novamente.\n')
                continue
            #os descontos que terao
            if num < 20:
                return num
            elif 20 <= num < 200:
                return num * 0.95
            elif 200 <= num < 2000:
                return num * 0.93
            elif 2000 <= num <= 20000:
                return num * 0.88

        except ValueError:
            print('Valor inválido. Digite apenas números inteiros.\n')


def frete():
    while True:
        try:
            print('''
Escolha o tipo de frete:
1 - Frete por transportadora - R$ 100.00
2 - Frete por Sedex - R$ 200.00
0 - Retirar pedido na fábrica - R$ 0.00
''')
            opcao_frete = int(input('>>'))
            if opcao_frete == 1:
                return 100.00
            elif opcao_frete == 2:
                return 200.00
            elif opcao_frete == 0:
                return 0.00
            else:
                print('Opção de frete inválida. Digite 1, 2 ou 0.\n')
        except ValueError:
            print('Valor inválido. Digite 1, 2 ou 0.\n')




modelo_valor_valido = escolha_modelo()
num_cam_valido = num_camisetas()
frete_valor = frete()

total = (modelo_valor_valido * num_cam_valido) + frete_valor
#a mensagem final com o preco com os descontos ou sem eles
print(
    f'\nTotal: R$ {total:.2f} (Modelo: {modelo_valor_valido:.2f} * Quantidade(com desconto): {num_cam_valido:.2f} + frete: {frete_valor:.2f})')