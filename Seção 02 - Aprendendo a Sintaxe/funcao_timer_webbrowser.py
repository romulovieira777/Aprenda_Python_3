'''
Create a function that reminds me to stop studying and take a break every 2 hours
Work starts from 8 to 12

Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2 horas
Trabalho inicia de 8 às 12
'''

import webbrowser
import time

breaks = 2
counter = 0
print('The rest control program has been activated ')  # O programa de controle de descanso foi ativado

while counter < breaks:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=JKM0dSAtl-E&list=RDOpMm5JO0wtU&index=3')
    counter = counter + 1
