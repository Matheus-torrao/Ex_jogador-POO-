from dataclasses import dataclass
from datetime import datetime

@dataclass
class Jogador:
    nome:str
    posicao:str
    data_nascimento:int
    nacionalidade:str
    altura:float
    peso:int
    
    def calcular_idade(self):
        data_atual = datetime.now()
        data_nascimento = datetime.strptime(self.data_nascimento, '%d/%m/%Y')
        idade = (data_atual.year - data_nascimento.year) 
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade       

    def exibir(self):
        print(f'nome: {self.nome}')
        print(f'Posição: {self.posicao}')
        print(f'Data de Nascimento: {self.data_nascimento}')
        print(f'Nacionalidade: {self.nacionalidade}')
        print(f'Altura: {self.altura}m')
        print(f'Peso: {self.peso}kg')
        print(f'Idade: {self.calcular_idade()} anos')

    def tempo_aposentadoria(self):
        ataque = 35
        meio_campo = 38
        defesa = 40

        idade = self.calcular_idade()
        posicao = self.posicao.lower()

        if idade <= ataque and posicao == 'ataque':
            restante = ataque - idade
            print(f'Restam {restante} anos para se aposentar da posição de ataque.')
        elif idade <= meio_campo and posicao == 'meia':
            restante = meio_campo - idade
            print(f'Restam {restante} anos para se aposentar da posição de meio campo.')

        elif idade <= defesa and posicao == 'defesa':
            restante = defesa - idade
            print(f'Restam {restante} anos para se aposentar da posição de defesa.')

        else:
            print('Você já está aposentado.')
     
@property
def nome(self):
    return self._nome
@property
def posicao(self):
    return self._posicao

@property
def data_nascimento(self):
    return self._data_nascimento

@property
def nacionalidade(self):
    return self._nacionalidade

@property
def altura(self):
    return self._altura

@property
def peso(self):
    return self._peso

@nome.setter
def nome (self, nome):
    self._nome = nome

@posicao.setter
def posicao (self, posicao):
    self._posicao = posicao

@data_nascimento.setter
def data_nascimento(self,data_nascimento):
    self._data_nascimento = data_nascimento

@nacionalidade.setter
def nacionalidade(self,nacionalidade):
    self._nacionalidade = nacionalidade

@altura.setter
def altura(self,altura):
    self._altura = altura

@peso.setter
def peso(self,peso):
    self._peso = peso





