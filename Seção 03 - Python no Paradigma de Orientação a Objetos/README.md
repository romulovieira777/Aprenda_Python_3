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



### Operadores Aritméticos em Python
| Operadores Aritméticos | Operação                  |
|------------------------|---------------------------|
| +                      | Soma os Valores           |
| -                      | Subtração dos Valores     |
| *                      | Multiplicação dos Valores |
| **                     | Calcula a Potência        |
| /                      | Divisão dos Valores       |
| %                      | Resto da Divisão          |
