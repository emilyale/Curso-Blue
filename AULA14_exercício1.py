
num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

s = num1 + num2 
s2 = num1 * num2 
s3 = num1 // num2

if num1 > num2:
   print("O numero 1 é maior")
else:
   print("O número 2 é maior")  

if s % 2:
    print("É impar")
else:
    print("É par")    

if s2 > 40:
    print(s2 / s3)    
else:
    print("Não é maior que 40")    

print(f"A soma dos números é {s}")
print(f"A multiplicação dos números é {s2}")
print(f"A divisão inteira dos número é {s3}")