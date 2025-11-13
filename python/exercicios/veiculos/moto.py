from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def descrever(self):
        return f"Moto: {self.marca} ,{self.modelo} {self._ano} ,{self.cilindradas} cc"