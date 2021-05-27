# 1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a.	tamanho da lista.
# b.	maior valor da lista.
# c.	menor valor da lista.
# d.	soma de todos os elementos da lista.
# e.	lista em ordem crescente.
# f.	lista em ordem decrescente.

# lista  = [5, 7, 2, 9, 4, 1, 3]
# print(f"O tamanho da lista é: {len(lista )}")
# maior_numero = max(lista)
# print(f"O maior número é: {maior_numero}")
# menor_numero = min(lista)
# print(f"O menor número é: {menor_numero}")
# soma = sum(lista)
# print(f"A soma da lista é: {soma}")
# lista.sort()
# lista.sort(reverse=True)

#4.Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece uma vogal.
# frase = input("Digite uma frase:\n ")
# vogais = 0
# espacos = 0
# for letra in frase:
#     if letra == " ":
#         espacos += 1
#     elif letra in "aeiou" :  
#         vogais += 1 
   
# print(f"As vogais e espaços aparecem: {vogais, espacos}")

# 5.Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores.Caso seja um número primo, o programa ainda deve informar que se trata de um número primo! 

# n = int(input("Digite um número n:\n "))
# primos = 0
# for i in range(1,n):
#     if n % i == 0:
#        print(i)

# 6.Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = input("Digite uma frase:\n ")
resposta = " "
for letra in frase:
    if not (letra in "aeiouAEIOU"):
      resposta += letra
print(resposta)      