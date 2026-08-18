faturamento = 1_600
margem_lucro = 0.25
custo = 600
lucro = faturamento - custo

texto = "O lucro do mes foi de: " + str(lucro) + " reais"

print(texto)

texto = f"O lucro do mes foi de {lucro} reais"
print(texto)

email = "EMAIL@gmail.com "
#email = email.lower()

print(email.lower()) #deixa todas as letras minusculas
print(email.strip().lower())#desconsidera espaços em branco ou vazios

print(len(email)) #quantidade de caracteres na string
print(email[5])

print(email.find("@")) #retorna a posicao do caractere na string

print(email[0:5]) #retorna os caracteres da posicao 0 a 4
print(email[0:]) #retorna os caracteres da posicao 0 ate o final
print(email[(email.find('@')+1):])#retorna os caracteres da posicao do @ ate o final


texto = f"O lucro do mes foi de {lucro:,.1f} reais" #formata o numero com 1 casa decimal e separador de milhar
print(texto)
texto = f"O lucro do mes foi de {margem_lucro:,.1%}" #formata o numero como porcentagem com 1 casa decimal
print(texto)


