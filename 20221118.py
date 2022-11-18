# def maiuscula(v):
#     return v.upper()


# p = input('Entre com seu nome: ')
# p = maiuscula(p)
# print(f'O seu nome é {p}')


'''
1.Faça um programa para imprimir:
• 1
 2 2
 3 3 3
 .....
 n n n n n n ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
imprima até a n-ésima linha.

'''
# def n_esima(p):
#     for i in range(p):
#         print(f'{i+1}'*(i+1))
#         #print()

# #n = int(input('Entre com um número inteiro: '))
# n_esima(6)
'''
2.Faça um programa para imprimir:
• 1
 1 2
 1 2 3
 .....
 1 2 3 ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima
até a n-ésima linha.
'''
# def n_esima(p):
#     for i in range(1, p+1):
#         # print(f'{i+1}')
#         for j in range(1, i+1):
#             print(j, end=' ')
#         print()

# n_esima(6)
'''
3.Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma
desses três argumentos.
'''
# def soma_tres(a, b, c):
#     return a + b + c

# a = int(input('Entre com o valor A: '))
# b = int(input('Entre com o valor B: '))
# c = int(input('Entre com o valor C: '))
# r = soma_tres(a, b, c)
# print(f'O resultado da soma é: {r}')

'''
4.Faça um programa, com uma função que necessite de um argumento. A função retorna o valor
de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''
# def p_n(valor):
#     if valor > 0:
#         return 'P'
#     else:
#         return 'N'

# resultado = p_n(0)
# print(resultado)

'''
5.Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e
custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir
o imposto sobre vendas.
'''
def somaImposto(taxaImposto, custo):
    r = ((taxaImposto/100)*custo)
    return r + custo

taxa = int(input('Entre com a taxa: '))
custo = int(input('Entre com o custo: '))
r = somaImposto(taxa, custo)
print(r)