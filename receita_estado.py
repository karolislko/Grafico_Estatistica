import matplotlib.pyplot as plt

# Dados
estados = ['Bahia', 'Pernambuco', 'Rio de Janeiro']
receita_media = [175000, 220000, 245000]  # Receita média por estado

# Criando o gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(estados, receita_media, color=['blue', 'green', 'orange'])
plt.title('Receita Média por Estado')
plt.xlabel('Estado')
plt.ylabel('Receita Média (R$)')
plt.grid(axis='y')
plt.show()
