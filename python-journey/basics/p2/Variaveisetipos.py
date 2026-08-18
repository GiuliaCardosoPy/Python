
def Separador():
    print("-------------------------------------" + "\n")
faturamento = 1000 #= significa receber um valor
custo = 600

Separador()
print("Faturamento do mes: ", faturamento)
Separador()
print("Custo do mes: ", custo)
Separador()
novas_vendas = 1000
faturamento += novas_vendas 
#+= significa somar o valor a variavel
lucro = faturamento - custo

imposto = 0.2 * lucro
#imposto é um float pq utilizou um float na multiplicacao

novo_lucro = lucro - imposto
Separador()
print("Lucro do mes apos novas vendas: ",lucro)
Separador()
print("Imposto a pagar: ",imposto)
Separador()
print("Novo lucro: ",novo_lucro)


margem_lucro = novo_lucro / faturamento
Separador()
print("Margem de lucro: ",margem_lucro, "%")

#======================================================
#Aulas sobre tipos de variaveis

#numeros inteiros ex: int
number = 10
#numeros decimais ex: float
number = 10.5
#textos ex: strings
text = "Ola, mundo!"
#numeros booleanos ex: bool (true ou false)
is_true = True
is_false = False

#operadores

#mod -> %
#resto da divisao inteira
divisao = 10 % 3
Separador()
print("Resto da divisao de 10 por 3: ",divisao)
Separador()
#floor division -> //
divisao_inteira = 10 // 3
print("Divisao inteira de 10 por 3: ",divisao_inteira)