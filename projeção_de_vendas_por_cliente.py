import matplotlib.pyplot as plt

# Dados
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
aumento_medio_por_cliente = [10, 12, 15, 14, 13, 11, 10, 12, 15, 14, 13, 11]
projecao_vendas_por_cliente = [200, 210, 220, 215, 212, 205, 200, 210, 220, 215, 212, 205]

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(meses, aumento_medio_por_cliente, marker='o', label='Aumento Médio por Cliente (R$)')
plt.plot(meses, projecao_vendas_por_cliente, marker='o', label='Projeção de Vendas por Cliente (R$)')
plt.title('Aumento Médio e Projeção de Vendas por Cliente por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor (R$)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
