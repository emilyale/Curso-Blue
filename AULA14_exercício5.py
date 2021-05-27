frase = "boa noite"

vogais = 0
resposta = " "
for letra in frase:
    if letra in "aeiou" :  
        vogais += 1 

for letra in frase:
    if not (letra in "aeiou"):
      resposta += letra

   
print(f"As vogais  aparecem: {vogais}")
print(f"Sem vogais: {resposta}")  
print(f"Foram retiradas {vogais} letras da frase")