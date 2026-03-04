# ============================================================
# PRÁCTICA 1: Análisis Visual de Datos de Producción
# Alumna: Yulenny Bonilla
# Descripción: Análisis de producción en fábrica de componentes
#              electrónicos usando pandas y matplotlib
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Hacer graficos visualmente atractivos

# --- Configuración visual general ---
sns.set_style('whitegrid')  # Estilo de fondo para los gráficos
plt.rcParams['figure.figsize'] = (10, 6)  # Tamaño de las figuras por defecto

# ============================================================
# 1. CARGAR EL DATASET
# ============================================================

df = pd.read_csv('data/produccion.csv')

# Exploración inicial del dataset
print("=== PRIMERAS FILAS DEL DATASET ===")
print(df.head())

print("\n=== INFORMACIÓN GENERAL ===")
print(df.info())

print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(df.describe())

# ============================================================
# 2. HISTOGRAMAS - Distribución de variables numéricas
# ============================================================

# Histograma de cantidad producida
plt.figure()
plt.hist(df["cantidad_producida"], bins=8, color="steelblue", edgecolor="black")
plt.title("Distribución de Cantidad Producida por Turno")
plt.xlabel("Cantidad Producida")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("graficos/histograma_cantidad.png")
plt.show()
print("Histograma de cantidad guardado.")

# Histograma de defectos
plt.figure()
plt.hist(df["defectos"], bins=8, color="salmon", edgecolor="black")
plt.title("Distribución de Defectos por Turno")
plt.xlabel("Número de Defectos")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("graficos/histograma_defectos.png")
plt.show()
print("Histograma de defectos guardado.")