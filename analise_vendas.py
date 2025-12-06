import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/vendas.csv")

print("\n=== RESUMO DAS VENDAS ===")
print(df.describe())

total = df["valor_total"].sum()
print(f"\nTotal vendido: R$ {total:.2f}")

vendas_produto = df.groupby("produto")
["valor_total"].sum()
print("\nVendas por produto:")
print(vendas_produto)

vendas_produto.plot(kind="bar")
plt.title("vendas por produto")
plt.ylabel("Total Vendido")
plt.xlabel("Produto")
plt.tight_layout()
plt.savefig("grafico_vendas.png")
plt.show()