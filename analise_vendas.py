import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler os dados
df = pd.read_csv("data/vendas.csv")

# 2. Mostrar resumo das vendas
print("Resumo das vendas:")
print(df.describe())

# 3. Calcular o total vendido
total_vendido = df["valor_total"].sum()
print(f"\nTotal vendido: R$ {total_vendido:.2f}")

# 4. Agrupar vendas por produto
vendas_por_produto = df.groupby("produto")["valor_total"].sum()
print("\nVendas por produto:")
print(vendas_por_produto)

# 5. Criar gráfico
vendas_por_produto.plot(kind="bar")
plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Total Vendido (R$)")
plt.tight_layout()
plt.show()
