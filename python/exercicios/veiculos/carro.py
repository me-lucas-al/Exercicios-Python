from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def descrever(self):
        return f"Carro: {self.marca} ,{self.modelo} ,{self._ano} ,{self.portas}"