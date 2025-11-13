class Veiculo:
    def __init__(self, marca, modelo, ano, ligado = False):
        self.marca = marca
        self.modelo = modelo
        self._ano = ano
        self._ligado = ligado

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 1900:
            print(f"O ano não pode ser maior do que 1900, porém o ano digitado foi {ano}")
        else: 
            self._ano = ano

    @property 
    def ligado(self):
        return self._ligado

    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False

    def descrever(self):
        return f"Veículo: {self.marca}, {self.modelo}, {self._ano}"