import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "employee_attrition.csv")
img = BASE / "images"
img.mkdir(exist_ok=True)

print("Tasa general de rotacion")
print(df["left_company"].mean())

print("\nRotacion por departamento")
print(df.groupby("department")["left_company"].mean().sort_values(ascending=False))

print("\nPromedios segun permanencia")
print(df.groupby("left_company")[["satisfaction_score", "overtime_hours", "monthly_salary", "tenure_years"]].mean())

attr_dept = df.groupby("department", as_index=False)["left_company"].mean().sort_values("left_company", ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(attr_dept["department"], attr_dept["left_company"])
plt.title("Tasa de rotacion por departamento")
plt.xlabel("Departamento")
plt.ylabel("Tasa de rotacion")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(img / "rotacion_departamento.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["satisfaction_score"], df["overtime_hours"], alpha=0.5)
plt.title("Satisfaccion vs horas extra")
plt.xlabel("Satisfaccion")
plt.ylabel("Horas extra")
plt.tight_layout()
plt.savefig(img / "satisfaccion_horas_extra.png", dpi=150)
plt.close()