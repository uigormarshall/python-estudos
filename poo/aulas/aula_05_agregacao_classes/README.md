#Aula 5 - Agregação de classes
## Definição:
A agregação acontece quando uma classe A, existe somente se as suas classes agregadas existem.
Para exemplificar isso em código,
iremos usar as classes ```Pessoa``` e ```Endereco```, onde o endereço só existe se houver uma pessoa
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def __del__(self):
        print(f'[Deletando]: {self.nome}')

    def adicionar_endereco(self, cidade, bairro, numero):
        self.enderecos.append(Endereco(cidade, bairro, numero))

    def listar_enderecos(self):
        print(f'{self.nome} seus endereços são:')
        for endereco in self.enderecos:
            print(f'- Cidade {endereco.cidade}, rua {endereco.bairro}, número {endereco.numero}')


class Endereco:
    def __init__(self, cidade, bairro, numero):
        self.cidade = cidade
        self.bairro = bairro
        self.numero = numero

    def __del__(self):
        print(f'[Deletando]: Cidade {self.cidade}, Bairro {self.bairro}, número {self.numero},')
```
#### Função __del__:
A função ```__del__``` serve para executar algo no momento em que objeto vai ser apagado da memoria,
no fim de todo programa, o garbage colletion do python faz a limpeza da memoria deletando as variaveis declaradas.
outra forma comum de ver esse metodo em execução é na chamada do ```del```, como no exemplo:

``` python
pessoa = Pessoa('Uigor Marshall', 54)
del pessoa
```

se você deletar uma pessoa como no exemplo, a saida no terminal será:
``` bash
[Deletando]: Uigor Marshall
``` 
nesse momento o comportamento de agregação ainda não é nitido, pois ainda não temos nenhum endereço cadastrado no usuário,
para adicionar um endereço basta chamar o metodo ``` adicionar_endereco``` :
``` python
pessoa = Pessoa('Uigor Marshall', 54)
pessoa.adicionar_endereco('Fortaleza', 'Aldeota', 1919)
pessoa.adicionar_endereco('Veneza', 'Alphon', 1325)
pessoa.adicionar_endereco('Maringados', 'São Jorge', 208)
pessoa.listar_enderecos()
```

a execução do metodo listar_enderecos deve retornara o resultado da agregação da seguinte forma:

``` bash
Uigor Marshall seus endereços são:
- Cidade Fortaleza, rua Aldeota, número 1919
- Cidade Veneza, rua Alphon, número 1325
- Cidade Maringados, rua São Jorge, número 208
``` 

para finalizar a demonstração basta deletar a pessoa, utilizando o comando del, a saida do terminal irá notificar o delete
dos endereços relacionados a pessoa. Finalizando assim o comportamento de uma agregação de classe.
``` python
del pessoa
``` 
o resultado do delete de cliente:
``` bash
[Deletando]: Uigor Marshall
[Deletando]: Cidade Maringados, Bairro São Jorge, número 208,
[Deletando]: Cidade Veneza, Bairro Alphon, número 1325,
[Deletando]: Cidade Fortaleza, Bairro Aldeota, número 1919,
``` 