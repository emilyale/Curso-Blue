senha = "moto123"
entrada = input("Digite a senha:\n")
numero = 9

while entrada != senha:
     print("Senha incorreta!")
     entrada = input("Digite a senha novamente:\n")
    

print("Senha correta!")
print("Bem vindo ao jogo da adivinhação!")
    
entrada2 = int(input("Tente adivinhar o número correto:\n"))

while entrada2 != numero:
     print("Você errou!")
     entrada2 = ("Tente novamente:\n")
     # if numero == entrada2:
     #      print("O número é maior que sua escolha")
     # else:
     #      print("O número é menor do que sua escolha")
     #      break
     

print("Parabéns, você acertou!")

         
