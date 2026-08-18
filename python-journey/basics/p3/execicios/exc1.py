nome = "joao paulo lira"
email = "emailfalsodolira@gmail.com"

#descubra o servidor do email
servidor = email[(email.find('@')+1):]
print(servidor)


#descubra o primeiro nome do usuario
primeiro_nome = nome.split()[0] #o slit() separa a string em uma lista de palavras e o [0] pega a primeira palavra da lista
print(primeiro_nome)


#criar uma mensagem personalizada dizendo "Usuario tal foi cadastrado com sucesso no email tal"

print(f"Usuario {primeiro_nome} foi cadastrado com sucesso no email {email}")

