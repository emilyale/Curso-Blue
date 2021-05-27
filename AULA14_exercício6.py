def programa(perguntas_lista):
    if sum(perguntas_lista) == 2:
        contador = contador+1
        print("Você é suspeito!")
    elif sum(perguntas_lista) != 3 or perguntas_lista != 4:
        contador = contador == 1
        print("Você é cumplice!")
    elif sum(perguntas_lista) == 5:
        contador = contador +1
        print("Você é assasino!")
    else:
        contador = contador
        print("Você é inocente")
        return "Digite novamente"

pergunta1 = input("Telefonou para a vítima? (sim) ou (não)\n")
pergunta2 = input("Esteve no local do crime? (sim) ou (não)\n")
pergunta3 = input("Mora perto da vítima? (sim) ou (não)\n")
pergunta4 = input("Devia para a vítima? (sim) ou (não)\n")
pergunta5 = input("Ja trabalhou com a vítima? (sim) ou (não)\n")

perguntas_list = {pergunta1,pergunta2,pergunta3,pergunta4,pergunta5}
contador = 0
total = contador
print(programa(contador))
