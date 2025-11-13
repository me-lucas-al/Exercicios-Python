from carro import Carro
from moto import Moto
from veiculo import Veiculo
# 1. Instanciando objetos
meu_carro = Carro("Ford", "Focus", 2020, 4)
minha_moto = Moto("Honda", "CB500", 2022, 500)
veiculo_generico = Veiculo("Marca Genérica", "Modelo Base", 1950)

# 2. Testando Getters e Setters (Properties)
print(f"Ano do carro: {meu_carro.ano}") # Testando o getter @property

# Tentando setar um ano válido
meu_carro.ano = 2021
print(f"Ano do carro atualizado: {meu_carro.ano}")

# Tentando setar um ano inválido
meu_carro.ano = 1800 # Deve mostrar uma mensagem de erro

# Testando o getter de 'ligado'
print(f"Carro está ligado? {meu_carro.ligado}") # Deve ser False

# 3. Testando métodos de ligar/desligar
meu_carro.ligar() # Deve ligar
print(f"Carro está ligado? {meu_carro.ligado}") # Deve ser True
meu_carro.ligar() # Deve avisar que já está ligado

meu_carro.desligar() # Deve desligar
print(f"Carro está ligado? {meu_carro.ligado}") # Deve ser False

print("-" * 20)

# 4. Testando Polimorfismo
# Criamos uma lista de veículos de diferentes tipos
lista_veiculos = [meu_carro, minha_moto, veiculo_generico]

# Iteramos e chamamos o MESMO método 'descrever()'
# Cada objeto saberá qual versão do método executar
print("--- Descrições Polimórficas ---")
for veiculo in lista_veiculos:
    print(veiculo.descrever())

# Saída esperada para esta parte:
# Carro: Ford Focus, 2021, 4 portas.
# Moto: Honda CB500, 2022, 500cc.
# Veículo Marca Genérica Modelo Base, ano 1950.