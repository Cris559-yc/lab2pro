import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = pd.read_csv("Amazon Big Billion Sale 2025 -Oct Mobile Phones.csv")

# ============================================================
# 2. Resumen estadístico
print("🔹 Resumen estadístico (numérico):")
print(df.describe())  # solo variables numéricas

print("\n🔹 Resumen estadístico (completo):")
print(df.describe(include='all'))  # incluye categóricas y numéricas

# ============================================================
# 3. Tipos de datos
print("\n🔹 Tipos de datos por columna:")
print(df.dtypes)

# ============================================================
# 4. Primeros y últimos registros
print("\n🔹 Primeros registros:")
print(df.head())

print("\n🔹 Últimos registros:")
print(df.tail())

# ============================================================
# 5. Ordenar resultados por precio (si existe la columna)
if "Price" in df.columns:
    print("\n🔹 Productos más baratos:")
    print(df.sort_values(by="Price", ascending=True).head(5))

    print("\n🔹 Productos más caros:")
    print(df.sort_values(by="Price", ascending=False).head(5))

# ============================================================
# 6. Medidas estadísticas sobre las columnas numéricas
if "Price" in df.columns:
    media_precio = df["Price"].mean()
    mediana_precio = df["Price"].median()
    std_precio = df["Price"].std()

    print("\n🔹 Estadísticas de 'Price':")
    print(f"Media: {media_precio:.2f}")
    print(f"Mediana: {mediana_precio:.2f}")
    print(f"Desviación estándar: {std_precio:.2f}")

if "Rating" in df.columns:
    media_rating = df["Rating"].mean()
    print(f"\n🔹 Rating promedio: {media_rating:.2f}")

if "Review_Count" in df.columns:
    media_reviews = df["Review_Count"].mean()
    print(f"\n🔹 Reseñas promedio: {media_reviews:.2f}")

# ============================================================
# 7. Gráficos opcionales (se abrirán en ventana aparte)

# Histograma de precios
if "Price" in df.columns:
    plt.figure(figsize=(8,5))
    plt.hist(df["Price"].dropna(), bins=30, edgecolor="black")
    plt.title("Distribución de Precios de Móviles")
    plt.xlabel("Precio (INR)")
    plt.ylabel("Cantidad de productos")
    plt.show()

# Gráfico de barras de las 10 marcas más frecuentes
# (tomamos la primera palabra del Product_Name como marca)
df["Brand"] = df["Product_Name"].str.split().str[0]

plt.figure(figsize=(10,5))
df["Brand"].value_counts().head(10).plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 10 marcas más frecuentes")
plt.xlabel("Marca")
plt.ylabel("Cantidad de productos")
plt.show()
