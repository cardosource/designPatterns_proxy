from abc import ABCMeta, abstractmethod


# Interface
class Valetransporte(metaclass=ABCMeta):

    @abstractmethod
    def passagem_onibus(self):
        pass


# Objeto real
class Carteirinha(Valetransporte):

    def __init__(self):
        self.senha = None
        self.numero_registro = "Mt-024"
    
    def __get_numero_registro(self):

        return self.numero_registro
    
    def __possui_carga(self):
        print(f'Verificando registro unico {self.__get_numero_registro()}')

        return True

    def set_senha(self, senha):
        self.senha = senha
    
    def passagem_onibus(self):
        if self.__possui_carga():
            print('Linha transiente a qualquer bairro.')
            return True
        else:
            print('Lamentamos no entanto podera mudar de plano para passagens intermunicipais')
            return False


# Proxy
class CartaoIndividual(Valetransporte):

    def __init__(self):
        self.Carteirinha = Carteirinha()
    
    def passagem_onibus(self):
        senha = input('[ password ]: Por gentileza digite a senha : ')
        self.Carteirinha.set_senha(senha)
        return self.Carteirinha.passagem_onibus()


# Cliente
class Cliente:

    def __init__(self):
        print('Passageiro:...')
        self.meucartao = CartaoIndividual()
        self.passagem = None
    
    def fazer_pagamento(self):
        self.passagem = self.meucartao.passagem_onibus()
    
    def __del__(self):
        if self.passagem:
            print('Obrigo, aproveito o transporte publico')
        else:
            print('Obrigo, aproveito o transporte intermunicipais...')



if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()
