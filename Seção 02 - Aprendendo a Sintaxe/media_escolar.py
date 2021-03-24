print('The program is running')  # O programa esta em execução
name = input('Type your name: ')  # Digite seu nome
matter = input('Enter the name of the story: ')  # Digite o nome da matéria
print('Now you need to enter the four notes')  # Agora você precisa informar as quatro notas
counter = 0
soma = 0
while counter < 4:
    note = int(input('Enter your note: '))  # Digite sua nota
    soma += note
    counter += 1

average = soma / counter
if average < 7:
    print('Student', name,  'you have FAILED. Your average in', matter, 'he was', average)
    # Aluno, você foi REPROVADO. Sua média em foi.
else:
    print('CONGRATULATIONS')  # PARABÉNS
    print('Student', name, 'You were approved. Your average in', matter, 'he was', average)
    # Aluno, você foi APROVADO. Sua média em foi
