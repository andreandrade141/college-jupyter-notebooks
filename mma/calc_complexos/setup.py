from project.operations import divisao, soma, conju, multiplicacao, subtracao

print("Bem vindo a configuracao da calculadora MMA top maneira!")
print("Vamos comecar.... Digite as partes reais e imaginarias de dois numeros quaisquer.")
print("Numero z1: \nParte Real: ")
x1 = input()
print("Numero z1: \nParte Imaginaria: ")
y1 = input()
print(f'O primeiro numero complexo é: {x1}+{y1}i \n')
print("Vamos ao próximo numero: \n")
print("Numero z2: \nParte Real: ")
x2 = input()
print("Numero z2: \nParte Imaginaria: ")
y2 = input()
print(f'O segundo numero complexo é: {x2}+{y2}i \n')
print("------------------------------------------------------------------------------------")
print("Resultados:")

num1 = (x1, y1)
num2 = (x2, y2)

resp1 = conju(num1)
resp2 = soma(num1, num2)
resp3 = subtracao(num1, num2)
resp4 = multiplicacao(num1, num2)
resp5 = divisao(num1, num2)

print(f'O conjugado de z1 é: {resp1}')
print(f'O resultado de z1 + z2 é: {resp2}')
print(f'O resultado de z1 - z2 é: {resp3}')
print(f'O resultado de z1 * z2 é: {resp4}')
print(f'O resultado de z1 / z2 é: {resp5}')


end = input()
