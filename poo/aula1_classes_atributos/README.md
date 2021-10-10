#Aula 1 - Classes, métodos de instância e metodos de classe:
##Estrutura base
Como criar e utilizar classes, como também criar metodos de instância e métodos de classe.
para definir uma classe em python não é muito diferente do que o tradicional em outras linguagens,
para isso basta usar a diretiva class e dar o nome para classe e finalizar com 

####Exemplo de classe:
```python
class Pessoa:
```

##Construtor, atributos, variaveis
O método construtor segue o mesmo padrão, só que aqui o mesmo se chama __init__, como no exemplo abaixo e deve ter sempre o a variavel self passada como parametro,
esse atributo exerce função similiar ao ```this ``` do typescript

####init(construtor):
```python
class Pessoa:
    def __init__(self):
```


####atributos:
Os atributos devem ser passados após a passagem do atributo self, como no exemplo abaixo
```python
class Pessoa:
   def __init__(self, nome, idade):
```

####variaveis:
```python
class Pessoa:
    ano_corrente=2021
    def __init__(self, nome, idade):
```