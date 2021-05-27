#Exercício 0 – Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. Enquanto a soma não for 50, ele deve continuar repetindo.

# numero1 = int(input("Digite o número :\n"))
# numero2 = int(input("Digite o número :\n"))

# while numero1 + numero2 != 50:
#     print("Incorreto, não é 50")
#     numero1 = int(input("Digite o número :\n"))
#     numero2 = int(input("Digite o número :\n"))
# print("a soma está correta")

#Exercício 1 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.
# senha = "lg123"
# entrada = input("Digite a senha:\n")
# while entrada != senha:
#     print("Senha incorreta!")
#     entrada = input("Digite a senha novamente:\n")
    
# print("Senha correta")

# Exercício 4 – Codifique um jogo da FORCA. A pessoa digita uma palavra e tem que acertar a palavra digitada.
palavra = "bolacha"
entrada = input("Jogo da forca, digite uma palavra e tente acertar:\n")

while entrada != palavra:
    print("palavra incorreta!")
    entrada = input("Tente novamente:\n")

print("Você ganhou, parabéns!")    






