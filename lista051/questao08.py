'''Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.'''

# regra 1 da estrutura de repetiçao:
# declarar var contador no valor incial da repetiçao
cont = 0

# regra 2: testar a estrutura (while com var contador) no valor fim da repetiçao
while ( cont <= 20 ):
    # bloco que sera repetido varias vezes
    resto = cont % 2
    if ( resto == 1 ):
        print(cont)

    # regra 3: incrementar a var contador na ultima linha dentro do bloco
    cont = cont + 1