lista_compras = ["maçã", "banana", "laranja"]
lista_precos = [3.5, 2.0, 4.0]

dic_produtos = {
    "maçã": 3.5,
    "banana": 2.0,
    "laranja": 4.0
} #é sempre o par chave:valor

print(dic_produtos)
#pegar um item
produto = "banana"
posicao = lista_compras.index(produto)

preco = lista_precos[posicao]

print(produto, preco)


#pegar o valor de uma chave no dicionário
print(dic_produtos["maçã"])

#adicionar um item
#editar um item
dic_produtos["maçã"] *= 1.2



dic_produtos["avelã"] = 6.5

print(dic_produtos["maçã"])

#remover um item
item_remove = dic_produtos.pop("maçã")


print(dic_produtos)
print(item_remove)


