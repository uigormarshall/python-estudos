# Esse arquivo tras alguns exemplos de associação, entre as ferramentas(MaquinaDeEscrever e Caneta) e seu dono o
# Escritor.

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

#Demonstração de vinculo associativo, veja que ao alterar o dono da caneta
#Ele também é mudado dentro da ferramenta do George Orwell
george_orwell.ferramenta.quem_eh_meu_dono()

caneta.dono = ray_bradbury

george_orwell.ferramenta.quem_eh_meu_dono()
