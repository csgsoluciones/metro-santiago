# =====================================================
# ACTIVIDAD N.° 3 - APRENDIZAJE SUPERVISADO
# METRO DE SANTIAGO
#
# Autores:
# Daisy Nicol Malagón Ramírez
# Guillermo Andrés Carrillo Sánchez
# =====================================================

# Librerías
# Importamos pandas para crear tablas de datos
# Importamos numpy que nos genera números aleatorios y realiza cálculos numéricos
import pandas as pd
import numpy as np

# Ahora importamos las librerías de sklearn para dividir el conjunto de datos, crear el modelo de árbol de decisión y evaluar el modelo
from sklearn.model_selection import train_test_split

# importamos DecisionTreeClassifier para crear el modelo de árbol de decisión
from sklearn.tree import DecisionTreeClassifier

# Importamos las métricas de sklearn para evaluar el modelo
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# -----------------------------------------------------
# PRESENTACIÓN DEL PROGRAMA
# -----------------------------------------------------

# Mostramos el nombre de la actividad y el tema a tratar
print("Actividad N.° 3 - Aprendizaje Supervisado")
print("Metro de Santiago")
print("-" * 50)

# -----------------------------------------------------
# CREACIÓN DEL CONJUNTO DE DATOS
# -----------------------------------------------------

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Generar 100 registros de pasajeros entre 100 y 999
# Es una de las líneas más importantes del código, ya que nos permite generar un conjunto de datos aleatorio para simular la cantidad de pasajeros en el metro de Santiago.
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

# Selecciona las variables que usará el modelo para hacer la predicción. En este caso, se seleccionan las columnas "Cantidad_Pasajeros" y "Hora_Dia" del DataFrame "datos" y se asignan a la variable X.
X = datos[["Cantidad_Pasajeros", "Hora_Dia"]]

# Variable objetivo: Será lo que el modelo intentará predecir. En este caso, se selecciona la columna "Demora" del DataFrame "datos" y se asigna a la variable y.
y = datos["Demora"]

# -----------------------------------------------------
# DIVISIÓN DEL CONJUNTO DE DATOS
# -----------------------------------------------------

# significa que se dividirá el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba. El conjunto de entrenamiento se utilizará para entrenar el modelo, mientras que el conjunto de prueba se utilizará para evaluar su rendimiento.
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

# significa que se utilizará el modelo entrenado para hacer predicciones sobre el conjunto de prueba. El resultado de la predicción se almacenará en la variable y_pred.
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
