print("---Bem-vindo a loja de marmitas do Khauan Gabriel---".center(50))
print("----------------------Cardápio----------------------")
print("|tamanho | Bife Acebolado(BA) | Filé de Frango (FF)|".center(50))
print("|    P   |      R$ 16,00      |      R$ 15,00      |")
print("|    M   |      R$ 18,00      |      R$ 17,00      |")
print("|    G   |      R$ 22,00      |      R$ 21,00      |")
print("----------------------------------------------------")

total_do_pedido = 0.0

# O loop principal que se repete para cada novo pedido
while True:
    preco = None

    # Pergunta o sabor
    Sabor = input("Digite o Sabor (BA/FF): ").upper()

    if Sabor == "BA":
        Tamanho = input("Escolha o tamanho (P/M/G): ").upper()
        if Tamanho == "P":
            preco = 16.00
        elif Tamanho == "M":
            preco = 18.00
        elif Tamanho == "G":
            preco = 22.00
        else:
            print("Tamanho inválido.")

    elif Sabor == "FF":
        Tamanho = input("Escolha o tamanho (P/M/G): ").upper()
        if Tamanho == "P":
            preco = 15.00
        elif Tamanho == "M":
            preco = 17.00
        elif Tamanho == "G":
            preco = 21.00
        else:
            print("Tamanho inválido.")

    else:
        print("Sabor inválido. Tente novamente.")

    # Se um preço foi definido
    if preco is not None:
        total_do_pedido += preco
        print(f"O preço do item é R$ {preco:.2f}")

    # Esta é a parte que te permite sair do loop
    resposta = input("Deseja adicionar mais alguma coisa? (sim/nao): ").lower()

    # Se a resposta for nao o loob parará
    if resposta == "nao":
        break

print(f"Total do seu pedido: R$ {total_do_pedido:.2f}")