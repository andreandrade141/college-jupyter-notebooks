"""
Calculadora de complexos em python. Projeto desenvolvido para a disciplina de MMA do 5º ano
de engenharia da computação da FHO|Uniararas.
Professor: Everton de Toledo Hanser
Alunos:
        André Luís Sebastião Andrade - 104004
        Gustavo Abdala - 101991
        Joel de Almeida Neto - 99469
        Gabriel Lucas Marques - 103407
        Éder Gonçalves- RA 72531

Autor do código: André Luís Sebastião Andrade.
"""


def main(num1, num2):
    realn1 = int(num1[0])
    imagn1 = int(num1[1])
    realn2 = int(num2[0])
    imagn2 = int(num2[1])
    return (realn1, imagn1, realn2, imagn2)


def conju(num1):
    conjz = f'{num1[0]}-{num1[1]}i'
    return conjz


def soma(num1, num2):
    nums = []
    nums = main(num1, num2)
    re = nums[0] + nums[2]
    im = nums[1] + nums[3]

    return f'{re}+{im}i'


def subtracao(num1, num2):
    nums = []
    nums = main(num1, num2)
    re = nums[0] - nums[2]
    im = nums[1] - nums[3]
    if im < 0:
        return f'{re}{im}i'
    return f'{re}+{im}i'


def multiplicacao(num1, num2):
    nums = []
    nums = main(num1, num2)
    re = nums[0] * nums[2]
    im = nums[1] * nums[3]

    return f'{re}+{im}i'


def divisao(num1, num2):
    nums = []
    nums = main(num1, num2)
    if nums[2] == 0 or nums[3] == 0:
        return "Operação: Divisão por zero é impossível"

    re = float(nums[0] / nums[2])
    im = float(nums[1] / nums[3])

    return f'{re}+{im}i'
