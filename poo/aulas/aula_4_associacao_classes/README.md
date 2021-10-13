#Aula 4 - Associação de Classes
##Estrutura base
Para essa aula iremos usar um exemplo simples, mas que ilustra bem esse relacionamento,
associação é quando uma classe referir-se a outra, porém, ambas podem existir sem a outra. para este exemplo vamos criar 
três classes, o Escritor que deve possuir um nome e uma ferramenta, a MaquinaDeEscrever que é uma ferramenta e a Caneta,
que é outra ferramenta.
```python
class Escritor:
    def __init__(self, nome):
        self._nome = nome
        self._ferramenta = None

    @property
    def nome(self):
        return self._nome

    @property
    def ferramenta(self):
        return self._ferramenta

    def definir_ferramenta(self, ferramenta):
        self.ferramenta = ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Caneta:
    def __init__(self, dono, marca):
        self._dono = dono
        self._marca = marca

    @property
    def marca(self):
        self._marca = self.marca

    @property
    def dono(self):
        return self._dono

    @dono.setter
    def dono(self, dono):
        self._dono = dono

    @classmethod
    def escrever(self):
        print('[Caneta]: escrevendo...')

    def quem_eh_meu_dono(self):
        print(f'[Caneta]: meu dono é {self.dono.nome}...')


class MaquinaDeEscrever:
    def __init__(self, dono):
        self._dono = dono

    @property
    def dono(self):
        return self._dono

    @dono.setter
    def dono(self, dono):
        self._dono = dono

    @classmethod
    def escrever(self):
        print('[Maquina de Escrever]: escrevendo...')

    def quem_eh_meu_dono(self):
        print(f'[Maquina de Escrever]: meu dono é {self.dono.nome}...')
```
Note a utilização dos getters e setters, caso não compreenda, recomendo que volte para aula 3.
esse relaciomento é feito através dos atributos da classe, dito isso basta iniciar um getter e um setter
para definir a ferramenta e podemos utilizar da seguinte forma:
``` python
# Um escritor deve ter uma ferramenta, assim como toda ferramenta tem um dono!
george_orwell = Escritor('George Orwell')
ray_bradbury = Escritor('Ray Bradbury')

# Ferramentas
maquina_de_escrever = MaquinaDeEscrever(george_orwell)
caneta = Caneta(george_orwell, 'Bic')

george_orwell.definir_ferramenta(maquina_de_escrever)
george_orwell.ferramenta.escrever()

george_orwell.definir_ferramenta(caneta)
george_orwell.ferramenta.escrever()

george_orwell.ferramenta.quem_eh_meu_dono()

caneta.dono = ray_bradbury

george_orwell.ferramenta.quem_eh_meu_dono()

```

executando o código você terá a seguinte saida:
``` bash
[Maquina de Escrever]: escrevendo...
[Caneta]: escrevendo...
[Caneta]: meu dono é George Orwell...
[Caneta]: meu dono é Ray Bradbury...
```
Observe que após alterar o dono da caneta, ela também reflete a mudança no escritor, e quando chamamos a seguinte função 
```george_orwell.ferramenta.quem_eh_meu_dono()```, ela mostra o novo dono da ferramenta.