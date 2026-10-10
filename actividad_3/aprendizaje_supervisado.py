# =====================================================
# ACTIVIDAD N.° 3 - APRENDIZAJE SUPERVISADO
# METRO DE SANTIAGO
# Autores:
# Daisy Nicol Malagón Ramírez
# Guillermo Andrés Carrillo Sánchez
# =====================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("Actividad N.° 3 - Aprendizaje Supervisado")
print("Metro de Santiago")
print("-" * 50)

# =====================================================
# CREACIÓN DEL CONJUNTO DE DATOS
# =====================================================

np.random.seed(42)

cantidad_pasajeros = np.random.randint(100, 1000, 100)
hora_dia = np.random.randint(0, 24, 100)

demora = []

for pasajeros in cantidad_pasajeros:
    if pasajeros > 600:
        demora.append(1)
    else:
        demora.append(0)

datos = pd.DataFrame({
    "Cantidad_Pasajeros": cantidad_pasajeros,
    "Hora_Dia": hora_dia,
    "Demora": demora
})

print("\nPrimeros registros:")
print(datos.head())

# =====================================================
# VARIABLES
# =====================================================

X = datos[["Cantidad_Pasajeros", "Hora_Dia"]]
y = datos["Demora"]

# =====================================================
# DIVISIÓN DE DATOS
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# =====================================================
# ENTRENAMIENTO
# =====================================================

modelo = DecisionTreeClassifier(random_state=42)

modelo.fit(X_train, y_train)

# =====================================================
# PREDICCIÓN
# =====================================================

y_pred = modelo.predict(X_test)

# =====================================================
# EVALUACIÓN
# =====================================================

precision = accuracy_score(y_test, y_pred)

print("\nPrecisión del Modelo:")
print(f"{precision:.2f}")

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# =====================================================
# EJEMPLO DE PREDICCIÓN
# =====================================================

nuevo_caso = pd.DataFrame({
    "Cantidad_Pasajeros": [750],
    "Hora_Dia": [18]
})

resultado = modelo.predict(nuevo_caso)

print("\nEjemplo de Predicción")
print("Pasajeros:", nuevo_caso["Cantidad_Pasajeros"][0])
print("Hora:", nuevo_caso["Hora_Dia"][0])

if resultado[0] == 1:
    print("Predicción: Es probable que exista demora.")
else:
    print("Predicción: No se espera demora.")
