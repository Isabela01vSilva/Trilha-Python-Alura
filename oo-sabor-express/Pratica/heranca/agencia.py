from pratica.heranca.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero
    
    def __str__(self):
        return self._nome