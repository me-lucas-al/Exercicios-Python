class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    @property
    def quantidade(self) -> int:
        return self.__quantidade


    @nome.setter
    def nome(self, novo_nome: str):
        if novo_nome.strip():  
            self.__nome = novo_nome
        else:
            print("Erro: O nome não pode ser vazio.")

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: O preço não pode ser negativo.")


    def atualizar_estoque(self, valor: int):

        nova_quantidade = self.__quantidade + valor
        
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
            print(f"Estoque de '{self.__nome}' atualizado para {self.__quantidade} unidades.")
        else:
            print(f"Erro: Operação inválida. Estoque não pode ficar negativo.")
            print(f"(Estoque atual: {self.__quantidade}, Tentativa de remoção: {-valor})")

    def exibir_detalhes(self):
        print("--- Detalhes do Produto ---")
        print(f"Nome: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Quantidade: {self.__quantidade} unidades")
        print("---------------------------")