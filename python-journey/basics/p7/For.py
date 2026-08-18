import time

"""print("Iniciando contagem:")
time.sleep(1)

for i in range(11):
    print(i)
    time.sleep(1)


print("Kabumm!!!")
"""
#==========================================
"""lista_precos = [1500, 1000, 800, 2000]

taxa_imposto = 0.1
taxa_imposto2 = 0.15
total_imposto = 0

for preco in lista_precos:
    if preco < 1000:
        total = preco * taxa_imposto
        preco += total
        print(f"\nO preço total com imposto é de:\nR$ {preco:,.2f}  \nO imposto cobrado foi de:\nR$ {total:,.2f} equivalente a {taxa_imposto}%")
        print("_____________________________________________________")
    else:
        total = preco * taxa_imposto2
        preco += total
        print(f"\nO preço total com imposto é de:\nR$ {preco:,.2f}  \nO imposto cobrado foi de:\nR$ {total:,.2f} equivalente a {taxa_imposto2}%")
        print("_____________________________________________________")

    total_imposto += total

print (f"O total de imposto pago foi de: R$ {total_imposto:,.2f}")
"""

#====================================================================

vendas_23 = {"jan": 15000, "fev":10000, "mar":5000}
vendas_24 = {"jan": 16000, "fev":11000, "mar":5100}

#calculo percentual de crescimento
#16000/15000 - 1 -> qnts %

for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1

    print(f"No mês de {mes} o crescimento foi de {crescimento:.2f}%")