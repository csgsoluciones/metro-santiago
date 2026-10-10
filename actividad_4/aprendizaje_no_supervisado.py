# =====================================================
# ACTIVIDAD N.° 4 - APRENDIZAJE NO SUPERVISADO
# METRO DE SANTIAGO
#
# Integrantes:
# Daisy Nicol Malagón Ramírez
# Guillermo Andrés Carrillo Sánchez
# =====================================================

# Librería para manejar tablas de datos
import pandas as pd

# Importa el algoritmo que formará grupos de forma automática
from sklearn.cluster import KMeans

# Solo muestra el encabezado del programa
print("Actividad N.° 4 - Aprendizaje No Supervisado")
print("Metro de Santiago")
print("-" * 50)

# -----------------------------------------------------
# CARGA DEL DATASET
# -----------------------------------------------------

# Leemos el archivo CSV y lo transformamos en un DataFrame de pandas para poder manipularlo más fácilmente
df = pd.read_csv("dataset_metro.csv")

# Mostramos el dataset completo
print("\nDataset del Metro de Santiago:")
print(df)

# -----------------------------------------------------
# SELECCIÓN DE VARIABLES
# -----------------------------------------------------

# Variables que utilizaremos para crear los grupos
X = df[["Cantidad_Pasajeros", "Hora_Dia"]]

print("\nVariables seleccionadas:")
print(X)

# -----------------------------------------------------
# CREACIÓN DEL MODELO K-MEANS
# -----------------------------------------------------

# Crearemos dos grupos
modelo = KMeans(
    n_clusters=2,
    random_state=42
)

# Entrenamos el modelo
modelo.fit(X)

# -----------------------------------------------------
# RESULTADOS
# -----------------------------------------------------

# Guardamos el grupo asignado a cada registro
df["Grupo"] = modelo.labels_

# Mostramos los resultados del agrupamiento
print("\nResultados de agrupamiento:")
print(df)

print("\nResumen de grupos encontrados:")

for grupo in sorted(df["Grupo"].unique()):
    cantidad = len(df[df["Grupo"] == grupo])
    print(f"Grupo {grupo}: {cantidad} registros")

print("\nRegistros del Grupo 0:")
print(df[df["Grupo"] == 0])

print("\nRegistros del Grupo 1:")
print(df[df["Grupo"] == 1])

print("\nRegistros del Grupo 1:")
print(df[df["Grupo"] == 1])

# -----------------------------------------------------
# ANÁLISIS DE LOS GRUPOS
# -----------------------------------------------------

# Calculamos el promedio de pasajeros para cada grupo
promedio_grupo_0 = df[df["Grupo"] == 0]["Cantidad_Pasajeros"].mean()
promedio_grupo_1 = df[df["Grupo"] == 1]["Cantidad_Pasajeros"].mean()

# Mostramos el análisis de los grupos
print("\nAnálisis de grupos:")
print(f"Promedio de pasajeros Grupo 0: {promedio_grupo_0:.2f}")
print(f"Promedio de pasajeros Grupo 1: {promedio_grupo_1:.2f}")

if promedio_grupo_0 < promedio_grupo_1:
    print("\nGrupo 0: Baja afluencia de pasajeros")
    print("Grupo 1: Alta afluencia de pasajeros")
else:
    print("\nGrupo 0: Alta afluencia de pasajeros")
    print("Grupo 1: Baja afluencia de pasajeros")
