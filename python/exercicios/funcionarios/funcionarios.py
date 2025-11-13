class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self) -> float:
        return self.salario

    def exibir_dados(self):
        print(f"\n--- Ficha: {self.__class__.__name__} ---")
        print(f"Nome: {self.nome}")
        print(f"Salário Base: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, bonus: float):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_pagamento(self) -> float:
        return self.salario + self.bonus

    def exibir_dados(self):
        print(f"Bônus: R$ {self.bonus:.2f}")


class Vendedor(Funcionario):
    def __init__(self, nome: str, salario: float, perc_comissao: float, total_vendas: float):
        super().__init__(nome, salario)
        self.perc_comissao = perc_comissao  
        self.total_vendas = total_vendas

    def calcular_pagamento(self) -> float:
        comissao = self.total_vendas * self.perc_comissao
        return self.salario + comissao

    def exibir_dados(self):
        super().exibir_dados() 
        print(f"Total Vendas: R$ {self.total_vendas:.2f}")
        print(f"Comissão ({self.perc_comissao * 100}%): R$ {self.total_vendas * self.perc_comissao:.2f}")