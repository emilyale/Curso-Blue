# 1.Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

# n = int(input("Digite o número da tabuada:\n "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# # 2.Crie um código em Python para exibir a contagem de dígitos de um número inteiro positivo informado pelo usuário   

# n = input("Digite um número inteiro e positivo:\n ")
# print(f"O número tem, {len(n)}, digitos")

#3.	O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo: 

# valor_pao = float (input ("Digite o valor do pão:\n "). replace (',', '.'))
# print (f"Preço do pão: R${valor_pao}")
# print ("Panificadora Pão de Ontem - Tabela de preços ") 
# for i in range (1, 11): 
#   print (" {} - R $ {: .2f} ". format (i, valor_pao * i))

# 4.	Crie um código em Python que receba uma lista de nomes informados pelo usuário com tamanho indefinido (a lista deve ser encerrada quando o usuário digitar 0) e, na sequência, receba um nome para que seja verificado se este consta na lista ou não. Observação: ignorar diferenças entre maiúsculas e minúsculas.

# nomes = []

# for i in range(1000): #vai receber no máximo 1000 nomes
#     a = input("Digite um nome para acrescentar á lista ou 0 para sair:\n ").lower()
#     if a =="0":
#         break
#     else:
#         nomes.append(a)

# nome = input("Digite o nome para buscar na lista:\n ").lower()
# if nome in nomes:
#     print("O nome está na lista!")
# else:
#     print("O nome não está na lista!")    

#  6.	Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista. Ao final, seu script deverá fornecer a média geral do aluno.  
lista = []
n = int(input("Digite o número de matérias:\n ")) 

notas = []
for i in range(n):
    nota = float(input("Digite a nota da matéria:\n "))
    notas.append(nota)

media = sum(notas) 
print(f"A média final é: {media}")   
