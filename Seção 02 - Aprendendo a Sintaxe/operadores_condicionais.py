# Comparison operators (Operadores de comparação)
# > bigger then (maior que)
# < less than (menor que)
# >= bigger or equal (maior ou igual)
# <= less or equal (menor ou igual)
# == equal (igual)
# != it is not the same (não é igual)
# and e
# or ou


# Conditionals (Condicionais) - if, elif, else

# if conditionals (condição):
#    code executed if the condition is true (código executado se for verdadeira a condição)
# else:
#   code executed if the condition is false (código executado se for falsa a condição)


x = 10

if x % 2 == 0:
    print(x, "it's an even number")  # é um número par
else:
    print(x, 'is an odd number')  # é um número ímpar


a = 11
b = 20

if a > b:
    print('a is bigger than b')  # é maior que
elif a == b:
    print("a it's the same as b")  # é igual a
else:
    print('a less than b')  # é menor que


# Conditions for entering the cinema (Condições para entrar no cinema):
#   Pay admission and be over 18 years old (Pagar ingresso e ser maior que 18 anos)

paid_ticket = True  # pagou ingresso
greater_than_eighteen = False  # maior_de_dezoito

if paid_ticket and greater_than_eighteen:
    print('You may come in')  # Pode entrar
else:
    print('You cannot enter')  # Não pode entrar
