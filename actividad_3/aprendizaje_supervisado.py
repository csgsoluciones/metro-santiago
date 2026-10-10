# =====================================================
# ACTIVIDAD N.° 3 - APRENDIZAJE SUPERVISADO
# METRO DE SANTIAGO
#
# Autores:
# Daisy Nicol Malagón Ramírez
# Guillermo Andrés Carrillo Sánchez
# =====================================================

# Librerías
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# -----------------------------------------------------
# PRESENTACIÓN DEL PROGRAMA
# -----------------------------------------------------

print("Actividad N.° 3 - Aprendizaje Supervisado")
print("Metro de Santiago")
print("-" * 50)

# -----------------------------------------------------
# CREACIÓN DEL CONJUNTO DE DATOS
# -----------------------------------------------------

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Generar 100 registros de pasajeros entre 100 y 999
cantidad_pasajeros = np.random.randint(100, 1000, 100)

# Generar 100 horas aleatorias entre 0 y 23
hora_dia = np.random.randint(0, 24, 100)

# Crear lista de demoras
demora = []

# Generar la variable objetivo
for pasajeros in cantidad_pasajeros:
    if pasajeros > 600:
        demora.append(1)
    else:
        demora.append(0)

# Crear DataFrame
datos = pd.DataFrame({
    "Cantidad_Pasajeros": cantidad_pasajeros,
    "Hora_Dia": hora_dia,
    "Demora": demora
})

# Mostrar primeros registros
print("\nPrimeros registros:")
print(datos.head())

# -----------------------------------------------------
# DEFINICIÓN DE VARIABLES
# -----------------------------------------------------

# Variables predictoras
X = datos[["Cantidad_Pasajeros", "Hora_Dia"]]

# Variable objetivo
y = datos["Demora"]

# -----------------------------------------------------
# DIVISIÓN DEL CONJUNTO DE DATOS
# -----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# -----------------------------------------------------
# ENTRENAMIENTO DEL MODELO
# -----------------------------------------------------

modelo = DecisionTreeClassifier(random_state=42)

modelo.fit(X_train, y_train)

# -----------------------------------------------------
# PREDICCIÓN
# -----------------------------------------------------

y_pred = modelo.predict(X_test)

# -----------------------------------------------------
# EVALUACIÓN
# -----------------------------------------------------

precision = accuracy_score(y_test, y_pred)

print("\nPrecisión del Modelo:")
print(f"{precision:.2f}")

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# -----------------------------------------------------
# INGRESO DE DATOS POR TECLADO
# -----------------------------------------------------

pasajeros = int(input("\nIngrese cantidad de pasajeros: "))
hora = int(input("Ingrese la hora (0-23): "))

nuevo_caso = pd.DataFrame({
    "Cantidad_Pasajeros": [pasajeros],
    "Hora_Dia": [hora]
})

resultado = modelo.predict(nuevo_caso)

print("\nResultado de la predicción")

if resultado[0] == 1:
    print("Es probable que exista demora.")
else:
    print("No se espera demora.")
