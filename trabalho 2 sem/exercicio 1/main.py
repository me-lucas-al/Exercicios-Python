from produto import Produto

notebook = Produto(nome="Notebook Gamer", preco=4500.00, quantidade=10)
notebook.exibir_detalhes()

print(f"Acessando o nome: {notebook.nome}")
print(f"Acessando o preço: R$ {notebook.preco:.2f}")

print("\nAlterando o preço para R$ 4200.00...")
notebook.preco = 4200.00
print(f"Novo preço: R$ {notebook.preco:.2f}")

print("\nTentando alterar o preço para -100...")
notebook.preco = -100.00  
notebook.exibir_detalhes()

print("\nAdicionando 5 unidades ao estoque...")
notebook.atualizar_estoque(5)  

print("\nRemovendo 8 unidades do estoque...")
notebook.atualizar_estoque(-8) 
notebook.exibir_detalhes()

print("\nTentando remover 10 unidades (estoque atual é 7)...")
notebook.atualizar_estoque(-10) 
notebook.exibir_detalhes()