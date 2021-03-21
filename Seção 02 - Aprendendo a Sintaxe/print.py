# Print function (Função print)
day = 19
month = 4
year = 2018
name = 'José'
surname = 'Silva'
height = 1.9


# The student José da Silva has height equal to 1.90 (O aluno José da Silva tem altura igual a 1.90)
# %s for strings (para strings)
# %d whole (inteiros)
# %f decimals (decimais)

print('The student ' + name + ' ' + surname)  # O aluno
print('The student ', name, surname)  # O aluno
print(day, month, year, sep='/')
print('Student %s was approved ' % name)  # Aluno foi aprovado
print('Welcome %s' % name)
print('The student %s %s, has height equal to %f ' % (name, surname, height))  # O aluno tem altura igual a

# Conversion functions (Funções de conversão)
# int(3)
# float(3.14)
# str('2.3')

print('Student ' + name, 'has height equal to ' + str(height))
