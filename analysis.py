import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "retail_sales_2024.csv")
img = BASE / "images"
img.mkdir(exist_ok=True)

df["profit"] = df["revenue"] - df["cost"]
df["margin"] = df["profit"] / df["revenue"]

print("Resumen general")
print(df[["orders", "revenue", "profit", "margin"]].describe())

print("\nIngresos por categoria")
print(df.groupby("category")["revenue"].sum().sort_values(ascending=False))

print("\nMargen promedio por region")
print(df.groupby("region")["margin"].mean().sort_values(ascending=False))

sales_month = df.groupby("month", as_index=False)["revenue"].sum()
plt.figure(figsize=(10, 5))
plt.plot(sales_month["month"], sales_month["revenue"], marker="o")
plt.title("Ingresos mensuales 2024")
plt.xlabel("Mes")
plt.ylabel("Ingresos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(img / "ingresos_mensuales.png", dpi=150)
plt.close()

sales_cat = df.groupby("category", as_index=False)["profit"].sum().sort_values("profit", ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(sales_cat["category"], sales_cat["profit"])
plt.title("Utilidad por categoria")
plt.xlabel("Categoria")
plt.ylabel("Utilidad")
plt.tight_layout()
plt.savefig(img / "utilidad_categoria.png", dpi=150)
plt.close()