### :computer: Comandos em Python que foram usados nos Arquivos acima: :rocket:
**O que faz a função __init__:**

Ativa as propriedades da classe para um objeto específico, uma vez criada e correspondida à classe correspondente.

**Sintaxe**

~~~py
__init__(<parâmetros>):
~~~

**Exemplo**

~~~py
__init__(self,  title, author, publisher, isbn, year)
~~~

**O que faz a função class:**

O mecanismo de herança permite múltiplas classes base (herança múltipla).

**Sintaxe**

~~~py
class(<parâmetros>):
~~~

**Exemplo**

~~~py
class Book:

    def __init__(self,  title, author, publisher, isbn, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
~~~

**O que faz a função def:**

É para definir uma função que é uma sequência de comandos que executa alguma tarefa e que tem um nome.

**Sintaxe**

~~~py
def nome(<parâmetros>):
    comandos:
~~~

**Exemplo**

~~~py
def hello(meu_nome):
    print('Olá',meu_nome)
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

**O que faz a função from:**

É usada para especificar a biblioteca.

**Sintaxe**

~~~py
import <biblioteca> from <caminho>
~~~

**Exemplo**

~~~py
from calculadora import Calculator
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

**O que faz a função property:**

Permite que você declare uma função para obter o valor de um atributo.

**Sintaxe**

~~~py
@property
~~~

**Exemplo**

~~~py
@property
    def title(self):
        return self.__title
~~~

**O que faz a função return:**

É utilizada para declarar a informação a ser retornada pela função.

**Sintaxe**

~~~py
return(<condição>):
~~~

**Exemplo**

~~~py
def soma(x,y):
    num = x * y
    return num
~~~

**O que faz a função self:**

Representa o objeto que herdará essas propriedades.

**Sintaxe**

~~~py
self(<condição>):
~~~

**Exemplo**

~~~py
def __init__(self,  title, author, publisher, isbn, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
~~~

*O que faz a função setter:**

Permite você inserir dados em uma variável.

**Sintaxe**

~~~py
@title.setter
~~~

**Exemplo**

~~~py
@title.setter
    def title(self, title):
        self.__title = title
~~~

*O que faz a função super:**

É utilizado entre heranças de classes, ele nos proporciona extender/subscrever métodos de uma super classe (classe pai) para uma sub classe (classe filha), atrávez dele definimos um novo comportamento para um determinado método construido na classe pai e herdado pela classe filha.
**Sintaxe**

~~~py
super().__init__(<parâmetros>)
~~~

**Exemplo**

~~~py
    def __init__(self, name, weight):  # Nome, Peso
        self.name = name
        self.weight = weight


class Daughter(Father):
    def __init__(self, name, weight, hair):  # Cabelo
        super().__init__(name, weight)
        self.hair = hair
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
