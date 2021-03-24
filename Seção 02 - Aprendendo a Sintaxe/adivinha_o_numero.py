import random

print('Welcome to the game of guess the number')
# Bem vindo ao jogo de adivinha o número
print('You will have seven chances to guess the number')
# Você terá sete chances para adivinhar o número
prize_draw = random.randint(1, 100)  # Sorteio

kick = 0  # Chute
chances = 7  # Chances
attempts = 1  # tentativas
player = ''

name = input('Type your name: ')  # Digite seu nome
print('Enter a number between 1 and 100')  # Digite um número entre 1 e 100

while attempts <= 7:
    kick = int(input('Enter the number: '))  # Digite o número
    if kick < prize_draw:
        print('You missed. Your number is less than the draw, try again')
    # Você errou. Seu número é menor que o sorteado, tente novamente
        print(f'Attempts {attempts} in {chances}')  # Tentaviva
    elif kick == prize_draw:
        print(f'CONGRATULATIONS!!!! {player}')  # PARABÉNS
        print('You got it right with attempts')  # Você acertou com tentativas
        attempts = 8
    else:
        print('You were wrong, your number is greater than the draw.')
        # Você errou, seu número é maior que o sorteado.
    if attempts == 6:
        print('Last try')  # Última tentativa
    elif attempts == 7:
        print('End of the game')  # Fim do jogo
    attempts += 1
