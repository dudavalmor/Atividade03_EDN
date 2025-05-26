nome = input("Digite o nome do vendedor: ");
salario = float(input("Digite o salário fixo do vendedor: "));
totalVendas = float(input("Digite o total de vendas do vendedor: "));

comissao = totalVendas * 0.15;
salarioFinal = salario + comissao;

print(f"TOTAL = R$ {salarioFinal:.2f}");