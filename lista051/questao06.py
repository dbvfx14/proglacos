'''Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da
multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).'''

denver = int(input("Digite um número menor ou igual a 50: "))
produto = denver
contador = 1

while produto < 250:
    print(f"{denver} x 3*{contador} = {produto}")
    produto *= 3
    contador += 1