#cpf = input("Digite seu CPF (Apenas numeros): ")

#if len(str(cpf)) != 11:
#    print("CPF invalido! Precisa de 11 digitos.")
#elif not cpf.isdigit(): #isdigit() verifica se todos os caracteres da string sao numeros
#    print("CPF invalido! Digite apenas numeros.")
#else:
#    print("CPF valido!")

#definindo função de separador
def Separador():
    print("\n" + "---------------------------------------------------------" + "\n")
#listas em python

lista_compras = ["arroz", "feijao", "macarrao", "carne", "frango"]

print("\nImprime o primeiro item da lista:")
print(lista_compras[0]) #imprime o primeiro item da lista
Separador()

print("Imprime o ultimo item da lista:")
print(lista_compras[-1]) #imprime o ultimo item da lista
Separador()

lista_compras.append("leite") #adiciona um item no final da lista
print("Lista após adicionar leite:")
print(lista_compras)
Separador()

lista_compras.remove("carne") #remove um item da lista
print("Lista após remover carne:")
print(lista_compras)
Separador()

print("Lista após remover o ultimo item:")
lista_compras.pop() #remove o ultimo item da lista
print(lista_compras)
Separador()

lista_compras[1] = "feijao preto" #altera o item da lista na posicao 1

print("Lista após alterar o segundo item:")
print(lista_compras) #imprime a lista completa
Separador()

print("Posição do item 'frango' na lista:")
print(lista_compras.index("frango")) #retorna a posicao do item na lista
Separador()

print("Itens da lista a partir da posicao do item 'frango' menos 2 até o final:")
print(lista_compras[lista_compras.index("frango")-2:]) #retorna os itens da lista a partir da posicao do item "frango" menos 2 ate o final da lista
Separador()

item_removido = lista_compras.pop(-2)# remove o item da lista na posicao -2 e retorna o item removido
print(f"O item {item_removido} foi removido da lista.")
print(lista_compras)
Separador()

print("Lista após inverter a ordem:")
lista_compras.reverse() #inverte a ordem dos itens da lista
print(lista_compras)
Separador()

print("Lista após ordenar em ordem alfabetica:")
lista_compras.sort() #ordena os itens da lista em ordem alfabetica
print(lista_compras)
Separador()

print("Lista após ordenar em ordem alfabetica inversa:")
lista_compras.sort(reverse=True) #ordena os itens da lista em ordem alfabetica inversa
print(lista_compras)
Separador()

lista_compras.insert(1, "banana")#adiciona o item "banana" na posicao 1 da lista
print("Lista após adicionar banana na posicao 1:")
print(lista_compras)
Separador()

print("Quantidade de vezes que o item 'banana' aparece na lista:")
print(lista_compras.count("banana")) #retorna a quantidade de vezes que o item "banana" aparece na lista
Separador()