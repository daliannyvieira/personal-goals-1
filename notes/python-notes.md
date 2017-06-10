## Notes


# Python

## Conceitos:

- Instância é quando você usa uma classe para criar um objeto qualquer, dizemos que isto é uma “instância”, ou objeto. 
- Python é case sensitive
- Módulos são grupos de funções organizadas
- Classe é uma forma de unir dados e comportamentos
- Métodos são as funções de uma instância
- Atributos são os dados de uma instância
- Python é Snake Case: Snake case (or snake_case) is the practice of writing compound words or phrases in which the elements are separated with one underscore character (_) and no spaces, with each element's initial letter usually lowercased within the compound and the first letter either upper or lower case—as in "foo_bar" and "Hello_world".
- Python 3 usa uma forma de [arredondar](https://docs.python.org/3.5/library/functions.html#round), que também é chamado de Banker's rounding e sempre arredonda para o próximo valor par.
- Um syntax sugar, docinho de sintaxe da linguagem, apenas simplifica algo que seria trabalhoso, mas não muda a característica da linguagem. Então, ao invés de escrever dez vezes o número 20, podemos simplificar e escrever 10 * 20.
- [Library do Python](https://docs.python.org/3/library/) para qualquer dúvida.

## Variáveis
Variável é um objeto (uma posição, frequentemente localizada na memória) capaz de reter e representar um valor ou expressão.

Sintaxe: <nome da variável> = <valor que quero armazenar> </valor><br/>

### Regras:
- podem ser usados algarismos, letras ou _
- nunca devem começar com um algarismo
- não podemos usar palavras-chave naturais ao Python, por exemplo if, while, etc. (lista completa: import keyword e print keyword.kwlist).

## Tipos de variáveis:

- Númericos: inteiros (int), ponto flutuante (float), complexos (complex) (compreende todos os números complexos. São representados por dois números de ponto flutuante (um para a parte real e um para a parte imaginária, junto com o j)
Exemplos:
Inteiros : a = 3 <br/>
Float: b = 2.0 <br/>
Complex: g = 3+4j <br/>

- Literais: Armazenam caracteres ou sequências de caracteres (strings)
Strings (str) compreende todos os caracteres dentro de aspas (simples ou duplas)
Exemplos:
d = "stefani"
e = "2.0"
f = "123"

- Lógicos: Armazenam verdadeiro ou falso. Booleanos (bool)
Bool  compreende respostas do tipo True ou False
Exemplos:
x = "True"
z = "False"

PS: Se tiver dúvida em saber qual o tipo de variável que você está usando, digite type(<nomedavariavel>)
PS 2: Para transformar um tipo de variável em outra: int() ou float(), complex() ou str()

### Atribuição Múltipla
Sintaxe: <variável1>,<variável2> = <valor da variável1>, <valor da variável2> <br/>
Exemplo:
>>> a, b, c = 2, 3, 4
>>> a, b, c
(2, 3, 4)<br/>

### Mudar Variável 
Exemplos:
>>> a, b, c = 'Jet' <br/>
>>> a, b, c <br/>
('J', 'e', 't') <br/>

>>> a,b = b,a <br/>
>>> a,b,c <br/>
('e','J','t') <br/>


## Operadores Aritméticos

- +: soma
- -: subtração
- /:divisão
- // : divisão de inteiros
- % : módulo (resto da divisão)
- "*" : multiplicação
- ** : potenciação

## Operadores Lógicos

- ">": maior
- ">=": maior ou igual
- <: menor
- <=: menor ou igual
- !=: diferente
- not: Operador lógico que representa negação (inverso) da variável atual. Exemplo: Se a variável for verdade, torna-se falsa e vice-versa
- or: Operador lógico onde a resposta da operação é verdade se e somente se pelo menos uma das variáveis de entrada for verdade
- and: Operador lógico onde a resposta da operação é verdade se ambas as variáveis de entrada forem verdade.

Pesquisar sobre Tabela verdade, para saber resultados True OR False, True AND False...

## Concatenação de caracteres/strings
Concatenação é um termo usado em computação para designar a operação de unir o conteúdo de duas strings.
Ex: ‘<string>’ + ‘<string>’ <br/>

Ex 2:>>>“a”+ “b” <br/>
>>>‘ab’

- python não concatena inteiro com string igual javascript
Exemplo:
>>> idade1 = 10
>>> idade2 = "20"
>>> print(idade1 + idade2) // Resultado: Erro

## Dicas Strings

- "\n" – pula linha
- "\t" – tab (4 espaços)
- "\b" - backspace
- "\\" = \
- pular linha é \n ou “”” (no começo e final)

## String

Para fim de exemplo: abc = " Hello World "

- uppercase: todos os caracteres maiúsculos
Ex:>>> abc.upper() <br/>
>>> " HELLO WORLD " <br/>

- lowercase: todos os caracteres minúsculos 
Ex:>>> abc.lower() <br/>
>>> " hello world " <br/>

- strip: remove caracteres de uma string
Ex:>>> abc.strip() <br/>
>>> "Hello World" <br/>

- split: separa os caracteres por um separados (espaço, tab, enter, "/", +, etc)
Ex:>>> abc.split() <br/>
>>> ["Hello" , "World"] <br/>

- count: procura quantas ocorrências da busca existem na string
Ex:>>> abc.count("l") <br/>
>>> 3 <br/>

- swapcase: Esse método troca as letras da string para maiúsculas
Ex: >>> abc.swap() <br/>
>>> " hELLO wORLD " <br/>

- len: retorna o número de caracteres de uma string
Ex: >>> len(str) <br/>
>>> 11

- capitalize: coloca apenas o primeiro caractere maiúsculo
Ex: >>> abc.capitalize() <br/>
>>> " Hello world " <br/>

- title: coloca a primeira letra de cada palavra com letra maiúscula
>>> abc.title() <br/>
>>> " Hello World " <br/>

- startswith ou endswith: testa se um texto começa/termina com um elemento (é um teste lógico)
Ex: >>> Ex: a = '''Gatos amam mais as pessoas do que elas permitiriam. Mas eles têm sabedoria suficiente para manter isso em segredo.''' <br/>
>>> a.startswith('G')  (a variável a começa com a letra G?) <br/> 
True <br/>
>>> a.startswith('n') <br/>
False <br/>
>>> a.endswith('.') <br/>
True <br/>

- find: procura uma string dentro de um texto e retorna a posição de seu primeiro caractere. Se ele encontrar, ele mostra a posição do primeiro caracter, senão ele retorna -1.
Ex: >>> a = 'Existem duas maneiras de nos refugiarmos das misérias da vida: música e gatos.' <br/>
>>> a.find('t') <br/>
4 <br/>

>>> a.find('a', 11) <br/>
14 (procura a posição da letra a, a partir da posição 11) <br/>

>>> a.find('!') <br/>
-1   (não encontrou nada) <br/>

- replace: troca uma string por outra dentro de um texto
Ex: >>> a = 'Existem duas maneiras de nos refugiarmos das misérias da vida: música e gatos.' <br/>
>>> a.replace('misérias', 'mazelas') <br/>
'Existem duas maneiras de nos refugiarmos das mazelas da vida: música e gatos.' <br/>

- [Interpolação de Strings](https://pyformat.info/#simple)
Interpolar é a inserção de um trecho de texto dentro de outro. <br/>

Exemplo:
>>> print("Tentativa {} de {}".format(rodada, total_tentativas)) (Variável rodada e total de tentativas com valores)


Outros:

- Acessar último elemento: lista [-1]
- Junção de listas: lista.extend(lista2)
- Inserir em uma posição específica: lista.insert(0, “maria”) // inserir maria na posição 0
- Para remover elementos: lista.remove(x)
- Para retornar determinado valor da lista: lista.pop(x)
- Para limpar lista: lista.clear()
- Para saber qual posição do elemento: lista.index(x) 
- Para ordenar em ordem crescente: lista.sort()


## Índices

Índice em uma string: número que indica a posição de cada caractere na string.
ex: >>> a = “RUSSO AZUL” <br/>
>>> a[0] <br/>
>>> ‘R’ <br/>

Fatias de uma string: Retorna uma string, começando pelo índice colocado e terminando no anterior ao segundo índice.
Ex:>>> a[6:9]  (A partir do índice 6 até o índice 8) <br/>
>>> “AZU” <br/>

>>> a[6:]  (quando omitimos um índice, é mostrado o caractere do extremo (final) correspondente) <br/>
>>> ‘AZUL’ <br/>

>>> a[-1:] <br/>
>>> 'L'  (mostra último caractere do extremo correspondente) <br/>

Incremento de Fatias: Permite pegar caracteres alternados, e até mesmo inverter uma string.
Exemplos:
>>> a[6:10:2]  (índice a partir do 6 até o 9(nunca pega o último) e pulando de 2 em 2) <br/>
>>> “AU” <br/>

Para inverter: 
>>> a[::-1] <br/>
>>> “LUZA OSSUR” <br/>


## Listas e Tuplas (Lista se chama Array em outras linguagens)

Uma lista em Python é uma sequência ou coleção ordenada de valores. Cada valor na lista é identificado por um índice. O valores que formam uma lista são chamados elementos ou itens. Listas são similares a strings, que são uma sequência de caracteres, no entanto, diferentemente de strings, os itens de uma lista podem ser de tipos diferentes.

Tuplas: Não pode ser alterada, imutáveis

CASO ESPECIAL: para criar uma tupla de um único elemento, não funciona colocar o elemento entre parênteses. O Python fica em dúvida se é um elemento entre parênteses ou uma tupla.
Ex: >>> a = (1,) <br/>
>>> a <br/>
(1,) <br/>
>>> type(a) <br/>
<class 'tuple'> <br/>

Exemplos Lista:
lista = [1, 2, “marcos”, “yankees”, 8.72]  // Os elementos começam a contar em 0 é o 1, 1 é o 2, 2 é o marcos, etc…, para acessá-lo: <br/>
lista[0] que retorna 1 <br/>

Dúvida geral sobre diferença de listas e tuplas: - Mas, pra que existe tupla se ela não poder ser mudada? <br/>
A resposta é que, quando vamos criar uma variável que pode ser mudada posteriormente, precisamos de mais espaço (bits) para armazená-la. Então quando usamos uma tupla, estamos economizando espaço. Obviamente, que se formos usar uma variável que queremos aumentar ao longo do código, é melhor usar listas mutáveis.

## Listas

- append: para adicionar um item
Ex: >>> a = ['Gato', 'de'] <br/>
>>> a.append('Botas') <br/>
>>> print(a) <br/>
['Gato', 'de', 'Botas'] <br/>

- Join: para grudar os elementos de uma sequência de strings, usando um parâmetro fornecido: 'parametro'.join(<nomedavariavel>)
Ex: >>> chas = ['Camomila', 'Hortela', 'Cidreira'] <br/>
>>> '/'.join(chas) <br/>
'Camomila/Hortela/Cidreira' <br/>

- Split também se aplica

## Marcadores de variáveis
Servem para referenciar uma variável dentro de um print.
Ex: >>> a = 3.0112 <br/>
>>> print('Resultado = {}' .format(int(a))) <br/>
Resultado = 3 <br/>

Para quantidade de casas decimais: <br/>
>>> d = 3.0112 <br/>
>>> print('Resultado = {:.2f}' .format(d))  (:.2f quer dizer 2 casas após a vírgula) <br/>
Resultado = 3.01 <br/>

Mais informações: [pyformat](https://pyformat.info/)
- Para tirar mais dúvidas de comandos válidos para uma variável: [dir](https://docs.python.org/2/library/functions.html#help) e [help](https://docs.python.org/2/library/functions.html#dir)

## Condicionais

- Estruturas de Controle: if, else, elif
- Estruturas de iteração ou loop: for, while 


- Se tiver dúvida sobre, consulte a [Documentação Python](https://wiki.python.org.br/IntroPython)

## Entrada de dados (Input)

Sintaxe: <variável> = input(<"mensagem para o usuário entrar com o dado>")
Ex: hq = input('Entre com o nome de seu personagem de quadrinho favorito: ') <br/>
Entre com o nome de seu personagem de quadrinho favorito: <br/>

OBS: Mas o input() sempre retorna uma string (ele entende que o usuário digitou um texto). Se quero a entrada de um número, então preciso transformar a variável que foi lida como string em uma variável tipo numérico (usando o int( ), por exemplo).

Sintaxe 2 : <variável> = <tipo de número*>(input("<mensagem para o usuário entrar com o dado>"))  (No caso o tipo de número pode ser: int(), float(), str())
Ex: gasto = int(input('Escreva quantos quadrinhos em média você compra por semana: ')) <br/>
Escreva quantos quadrinhos em média você compra por semana: <br/>


## Importar módulos 

Exemplo: import math (importar módulo math, de funções matemáticas)

- math.ceil(x): menor inteiro maior ou igual a x. Exemplo: math.ceil(3.14) retorna 4    // Para lembrar: teto

- math.fabs(x): valor absoluto de x. Exemplo: math.fabs(-10) retorna 10.0

- math.fatorial(x): calcula fatorial de x. Exemplo: math.fatorial(3) retorna 6, pois 3! = 3*2*1 = 6

- math.floor(x): maior inteiro menor ou igual a x. Exemplo: math.floor(3.14) retorna 3  //Para lembrar: piso


## Dicionários
Dicionário relaciona termos chave com valores para cada um. Como se fossem várias variáveis, unidas por um motivo.

d = {‘marcos’:28, ‘joao’:30, ‘maria’:20}
d[‘marcos’]  (saber a idade de marcos) retorna 28

d.keys()      //chaves do dicionários
del d[‘joao´]      // deletar joão e dicionário não garante ordem

“marcos” in d retorna true  // marcos está no dicionario? Sim

Para saber quais os valores do seu dicionário: d.values()


## Range
Função range() retorna uma série numérica no intervalo enviado como argumento. <br/>

Sintaxe: range(start, stop[, step])

for contador in range(1,11,3):<br/>
    print(contador)<br/>
(Para contador no intervalo de 1 a 11, pulando 3 em 3, imprimir contador.O range imprime um número abaixo do final, vai imprimir de 1 a 10 pulando 3 em 3.) <br/>

lista = [x for x range(11) if x % 2 == 0] <br/>
lista <br/>
resultado: [0,2,4,6,8,10]

lista [x for x in range (1,11) if x%2 ==0] <br/>
lista <br/>
resultado: [2,4,6,8,10]

lista = [x ** 2 for x in range(1, 11)] <br/>
lista <br/>
resultado: [1,4,9,16,25,36,49,64,81,100]

## Funções
Funções são sub-rotinas no código que servem para executar um procedimento muitas vezes, evitando que você tenha que
reescrevê-lo mais de uma vez. Uma funcionalidade importante é o fato que, caso precise realizar alguma alteração ou correção, ela vai ser feita nesta sub-rotina e não em diversas partes do código.

- Para saber quais funções são [Built-in](https://docs.python.org/3/library/functions.html)(embutidas sem precisar importar)

