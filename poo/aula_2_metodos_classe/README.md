#Aula 2 - Métodos de classe
##Estrutura base
Os métodos de classe são funções python decladas dentro de uma classe, como no exemplo abaixo:
```python
class Pessoa:
    def falar(self, frase):
        print(frase)
```

além disso para chamar métodos de classe basta executar partindo de uma instancia:
```python
pessoa = Pessoa()
pessoa.falar('Olá, eu sou uma pessoa')
```
o retorno desta execução será um print no terminal com a frase ```Olá, eu sou uma pessoa```. é importante lembrar que uma
função declarada dessa forma é na realidade um método de classe, é importante lembrar disso pois o python usa um esquema de 
decoradores para decorar um método como estatico ou não.

##Métodos Estaticos
Nesse ponto as coisas começam a mudar um pouco, ao invés de declara a função como ```static```, como de costume em outras liguagens.  
Aqui usamos um decorador para dizer que a função pertence a classe e não a instância, tendo como resultado um médoto estatico.
```python
class Pessoa:
    ano_atual = 2021
    @staticmethod
    def cacular_ano_nascimento_pela_idade(cls, idade):
        return cls.ano_atual - idade
```
####Obs:
Vale lembrar também que o parametro ```self``` dentro de métodos estaticos recebe o nome de ```cls``` por convênção,
porém você pode atribuir qualquer nome a esse parametro

A utilização do método ```cacular_ano_nascimento_pela_idade``` é diferente da ```fala```, no caso basta chamar a classe e ultilizar o método, não sendo necessaria a inicialização de uma instância:
```python
class Pessoa:
    ano_atual = 2021
    @staticmethod
    def cacular_ano_nascimento_pela_idade(cls, idade):
        return cls.ano_atual - idade
    
    
data_nascimento = Pessoa.cacular_ano_nascimento_pela_idade(25)
```

