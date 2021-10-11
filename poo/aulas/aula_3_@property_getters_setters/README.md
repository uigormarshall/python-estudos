#Aula 3 - @property, getters e setters

## Definição:
####Getters
Este recurso é utilizado para obter dados de uma função, normalmente usada para mutar os dados no processo de requisição.
um detalhe importante é o fato de que um getter pode existir sem setter, porém o contrario 

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.nome
```

####Setters
São utilizados para definir o valor de um atributo, funciona como uma função
para declarar o valor de algo, noralmente são usados para validar um input, antes do mesmo ser definido na classe.
##Estrutura base
Como dito anteriormente um setter precisa de um getter para poder existir, a estrutura pode ser vista nesse exemplo:
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, value):
        self._nome = value
```

##Exemplos:
Para fins de demontração iremos usar o setter para colocar a primeira letra do nome em caixa alta,
para isso será feito o uso dos getters/setters.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    #veja o uso do capitalize para tornar a primeira letra maiuscula
    @nome.setter
    def nome(self, nome):
        self._nome = nome.capitalize()
```
ao criar uma instancia da classe ```Pessoa```, note que o nome será processado pelo setter e terá seu primeiro caractere
alterado para uma letra maiuscula.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    #veja o uso do capitalize para tornar a primeira letra maiuscula
    @nome.setter
    def nome(self, nome):
        self._nome = nome.capitalize()

pessoa = Pessoa( 'Forrest Gump')
print(pessoa.nome)
```
o retorno do getter é transformado pelo setter, e deve retornar:
```Forrest gump```