print("Bem-vindo a loja do Khauan Gabriel")
valor = 0

# Informa o valor de compra
valor = int(input("Entre com o valor do pedido:"))

# Informa a quantidade de parcela
parcela = int(input("Entre com a quantidade de parcela:"))

if parcela < 4:
     juros = 0

elif parcela < 6:
    juros = 4

elif parcela <9:
    juros  = 8

elif parcela < 13:
    juros = 16

else:
    juros = 32

# Valor final com o juros
valor_final = valor + (valor * juros/100)

#valor de cada parcela
valor_parcela = valor_final / parcela

#Valores finais
print(f"o valor de cada parcela é: R$ {valor_parcela:.2f}")
print(f"O valor total parcelado é: R$ {valor_final :.2f}")