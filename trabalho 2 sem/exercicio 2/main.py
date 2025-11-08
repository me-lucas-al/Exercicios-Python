from funcionarios import Funcionario, Gerente, Vendedor

func_comum = Funcionario(nome="João Silva", salario=2000.00)
gerente = Gerente(nome="Maria Souza", salario=6000.00, bonus=1500.00)
vendedor = Vendedor(nome="Carlos Lima", salario=1800.00, perc_comissao=0.05, total_vendas=20000.00)

lista_funcionarios = [func_comum, gerente, vendedor]

print("--- Processando Folha de Pagamento (Polimorfismo) ---")

for func in lista_funcionarios:
    func.exibir_dados() 
    
    pagamento = func.calcular_pagamento() 
    
    print(f"==> Pagamento Total: R$ {pagamento:.2f}")