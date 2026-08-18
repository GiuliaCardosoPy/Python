dic_produtos = {
    "maçã": 3.5,
    "banana": 2.0,
    "laranja": 4.0
} #é sempre o par chave:valor

produto_buscado = input("Digite o nome do produto que deseja buscar:").strip().lower()

if produto_buscado in dic_produtos:
    print(f"O produto {produto_buscado} está na lista!")
    print("O preço dele hoje é de:")
    print(f"R$ {dic_produtos[produto_buscado]:,.2f}")
    
else:
    print(f"O produto {produto_buscado} não está na lista.")
    