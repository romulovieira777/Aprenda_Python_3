### :computer: Comandos em Python que foram usados nos Arquivos acima: :rocket:
**O que faz a função append:**

Adiciona qualquer valor completo, por exemplo, se enviarmos um objeto, ele adiciona o objeto, se enviarmos uma lista, ele adiciona a lista inteira ao invés de seus itens.

**Sintaxe**

~~~py
append(<variável>):
~~~

**Exemplo**

~~~py
lista_04.append('Gorila')
~~~

**O que faz a função elif:**

É parecida com else, porém a usamos quando queremos atribuir uma condição para else.

**Sintaxe**

~~~py
elif(<variável>)
~~~

**Exemplo**

~~~py
age = int(input('Enter your age: '))

if (age >= 0) and (age <= 12):
    print('Your are Child!')
elif (age >= 13) and (age <= 17):
    print(' Your are a Teenager!')
~~~

**O que faz a função else:**

A instrução else é uma instrução dependente, isto é, uma instrução que não pode ser utilizada sozinha. A instrução else só é executada se a condição do if for falsa.

**Sintaxe**

~~~py
else:
~~~

**Exemplo**

~~~py
idade = 18
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')
~~~

**O que faz a função float:**

Devolve um número de ponto flutuante construído a partir de um número ou string.

**Sintaxe**

~~~py
float(<variável>)
~~~

**Exemplo**

~~~py
nota1 = float(input("Entre com a primeira nota: "))
~~~

**O que faz a função for:**

Executa um ciclo para cada elemento do objeto que está sendo iterado.

**Sintaxe**

~~~py
for <variável> in <objeto iterável>:
    bloco de instrução
~~~

**Exemplo**

~~~py
for numero in range(1, 6):
    print(numero)
~~~

**O que faz a função if:**

É uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.

**Sintaxe**

~~~py
if(<variável>)
~~~

**Exemplo**

~~~py
idade = 18
if idade < 20:
    print('Você é jovem!')
~~~

**O que faz a função import:**

É uma linha com o caminho completo para o arquivo python que contem o módulo que se deseja importar.

**Sintaxe**

~~~py
import <biblioteca>
~~~

**Exemplo**

~~~py
import re
~~~

**O que faz a função in:**

Verifica se o operando a sua esquerda, está contido na lista a sua direita.

**Sintaxe**

~~~py
 in (<variável>)
~~~

**Exemplo**

~~~py
2 and 3 in range(1,6)
~~~

**O que faz a função input:**

É para entrada de dados feita pelo usuário.

**Sintaxe**

~~~py
input(<variável>)
~~~

**Exemplo**

~~~py
nome = input('Entre com o nome do aluno: ')
~~~

**O que faz a função insert:**

Insere um dado à lista na posição cujo índice seja igual ao informado e os elementos que estiverem após o novo elemento, terão seus índices alterados automaticamente.

**Sintaxe**

~~~py
insert(<variável>):
~~~

**Exemplo**

~~~py
cars.insert(0, 'Hilux')
~~~

**O que faz a função int:**

Converte um dado string para um número inteiro.

**Sintaxe**

~~~py
int(<variável>)
~~~

**Exemplo**

~~~py
number_01 = int(input('Enter the first number: '))
~~~

**O que faz a função keys:**

Permite percorrer somente as chaves do dicionário.

**Sintaxe**

~~~py
keys( <posição>, <variável> ):
~~~

**Exemplo**

~~~py
people.keys()
~~~

**O que a função len faz:**

Retorna a quantidade de elementos contidos numa lista.

**Sintaxe**

~~~py
len(<variável>)
~~~

**Exemplo**

~~~py
print(len(our_text))
~~~

**O que faz a função pop:**

Retorna um elemento da lista e no mesmo instânte, remove-o.

**Sintaxe**

~~~py
pop( <posição> ):
~~~

**Exemplo**

~~~py
cars.pop(3)
~~~

**O que faz a função print:**

Imprimir um argumento passado na tela.

**Sintaxe**

~~~py
print(<variável>)
~~~

**Exemplo**

~~~py
print('Olá, Mundo!')
~~~

**O que a função range faz:**

Permite-nos especificar o início da sequência, o passo, e o valor final.

**Sintaxe**

~~~py
range(<variável>):
~~~

**Exemplo**

~~~py
range(0, 10)
~~~

**O que faz a função remove:**

Remove uma lista de valores do primeiro jogo.

**Sintaxe**

~~~py
remove( <variável> ):
~~~

**Exemplo**

~~~py
cars.remove('Hilux')
~~~

**O que faz a função str:**

Converte um dado para string.

**Sintaxe**

~~~py
str( <variável> ):
~~~

**Exemplo**

~~~py
str(height)
~~~

**O que faz a função time.sleep:**

É usada para adicionar um atraso de tempo ao seu código.

**Sintaxe**

~~~py
time.sleep( <variável> ):
~~~

**Exemplo**

~~~py
time.sleep(10)
~~~

**O que faz a função type:**

Retorna o tipo de um objeto.

**Sintaxe**

~~~py
type( <variável> ):
~~~

**Exemplo**

~~~py
print(type(tuple_01))
~~~

**O que faz a função values:**

Traz todos os valores do dicionário.

**Sintaxe**

~~~py
values()
~~~

**Exemplo**

~~~py
print(collect.values())
~~~

**O que faz a função webbrowser.open:**

Pode ser utilizada para abrir uma URL através do navegador padrão do usuário.

**Sintaxe**

~~~py
webbrowser.open()
~~~

**Exemplo**

~~~py
webbrowser.open('https://www.youtube.com/watch?v=JKM0dSAtl-E&list=RDOpMm5JO0wtU&index=3')
~~~

**O que a função while faz:**

Repete a sequência de comandos definida em seu corpo enquanto a <condição> permanece verdadeira.

**Sintaxe**

~~~py
while(<condição>):
~~~

**Exemplo**

~~~py
numero = 1
while numero < 6:
    print(numero)
    numero += 1
~~~


### Operadores Aritméticos em Python
| Operadores Aritméticos | Operação                  |
|------------------------|---------------------------|
| +                      | Soma os Valores           |
| -                      | Subtração dos Valores     |
| *                      | Multiplicação dos Valores |
| **                     | Calcula a Potência        |
| /                      | Divisão dos Valores       |
| %                      | Resto da Divisão          |


### Operadores Condicionais em Python
| Operadores Condicionais | Operação                  |
|-------------------------|---------------------------|
| >                       | Maior que                 |
| <                       | Menor que                 |
| >=                      | Maior ou igual            |
| <=                      | Menor ou igual            |
| ==                      | Igual                     |
| !=                      | Diferente                 |
| and                     | E                         |
| or                      | Ou                        |
