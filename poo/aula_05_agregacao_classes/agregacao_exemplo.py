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


pessoa = Pessoa('Uigor Marshall', 54)
pessoa.adicionar_endereco('Fortaleza', 'Aldeota', 1919)
pessoa.adicionar_endereco('Veneza', 'Alphon', 1325)
pessoa.adicionar_endereco('Maringados', 'São Jorge', 208)
pessoa.listar_enderecos()
del pessoa
print('Fim da execução do projeto')
