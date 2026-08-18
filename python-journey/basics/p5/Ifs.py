faturamento = 1000
custo = 600

lucro = faturamento - custo

custo = 1200

lucro = faturamento - custo

if lucro > 0:
    print("A empresa teve lucro de R$", lucro)
elif lucro < 0:
    print("A empresa teve prejuízo de R$", abs(lucro))
else:
    print("A empresa não teve lucro nem prejuízo.")

# > (maior que) < (menor que) >= (maior ou igual) <= (menor ou igual) == (igual) != (diferente) são operadores de comparação



