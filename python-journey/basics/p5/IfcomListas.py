import time;
produtos = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Sal", "Óleo", "Leite", "Café", "Farinha", "Manteiga"]


sair = False

while not sair:
    print("1- Cadastrar produto")
    print("2- Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            novo_produto = input("Digite o nome do produto que deseja adicionar à lista: ")
            if not novo_produto.isdigit():
                if novo_produto in produtos:
                    print(f"O produto {novo_produto} já está na lista.")
                    print("Lista de produtos atual:")
                    print(produtos)
                else:
                    produtos.append(novo_produto)
                    print(f"O produto {novo_produto} foi adicionado à lista.")
                    print("Lista de produtos atualizada:")
                    print(produtos)
            else:
                print("Entrada inválida. Por favor, digite um nome de produto válido.")
        case "2":
            print("Saindo do programa...")
            time.sleep(1)
            sair = True
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")

