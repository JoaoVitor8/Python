print("Velocidade máxima da via = 80")
print("Velocidade mínima da via = 40")
C = int(input("A velocimetro está em? "))
if(C <= 80 and C >= 40):
    print("Se beber não dirija")
elif(C < 40):
    print("Abaixo da velocidade permitida")
else:
    print("Acima da velocidade permitida")
    C = C - 80
    print(f"Você foi multado em R${C * 7:.2f}")
