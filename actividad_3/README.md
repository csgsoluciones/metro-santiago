# Sistema de Predicción de Demoras - Metro de Santiago

Proyecto desarrollado en Python para aplicar técnicas de Aprendizaje Supervisado utilizando un Árbol de Decisión, con el objetivo de predecir posibles demoras en el Metro de Santiago según la cantidad de pasajeros y la hora del día.

## Descripción
Este proyecto genera un conjunto de datos simulado relacionado con la operación del Metro de Santiago y utiliza Machine Learning para identificar patrones que permitan predecir la ocurrencia de demoras.

El sistema fue desarrollado utilizando:

Python
Pandas
NumPy
Scikit-Learn

## Objetivo

Desarrollar un modelo de aprendizaje supervisado capaz de predecir posibles demoras en el servicio de Metro de Santiago utilizando la cantidad de pasajeros y la hora del día como variables de entrada.

## Dataset Utilizado

El conjunto de datos fue generado de forma automática mediante NumPy y contiene:

Cantidad de pasajeros
Hora del día
Estado de demora
Las variables utilizadas son:

Variable	Descripción
Cantidad_Pasajeros	Número de pasajeros registrados
Hora_Dia	Hora del día entre 0 y 23
Demora	0 = No existe demora, 1 = Existe demora
La regla utilizada para generar la variable objetivo fue:

if pasajeros > 600:
    demora.append(1)
else:
    demora.append(0)
Tecnologías Utilizadas
Python 3.11
Pandas
NumPy
Scikit-Learn
Modelo Utilizado
El proyecto utiliza el algoritmo:

Árbol de Decisión (DecisionTreeClassifier)
Este algoritmo aprende patrones presentes en los datos de entrenamiento y posteriormente genera predicciones sobre nuevos casos ingresados por el usuario.

División de Datos
Los datos fueron divididos en:

70% Entrenamiento
30% Prueba
Mediante:

train_test_split()
Métricas de Evaluación
Para evaluar el rendimiento del modelo se utilizaron:

Accuracy Score
Matriz de Confusión
Classification Report
Resultados obtenidos:

Accuracy: 100%
Precision: 100%
Recall: 100%
F1-Score: 100%
Ejemplo de Uso
Ejemplo de entrada:

Ingrese cantidad de pasajeros: 900
Ingrese la hora (0-23): 18
Salida:

Resultado de la predicción
Es probable que exista demora.
Otro ejemplo:

Ingrese cantidad de pasajeros: 100
Ingrese la hora (0-23): 13
Salida:

Resultado de la predicción
No se espera demora.
Estructura del Proyecto
actividad_3
│
├── aprendizaje_supervisado.py
└── README.md

## Autores

* Daisy Nicol Malagón Ramírez

* Guillermo Andrés Carrillo Sánchez

## Repositorio

https://github.com/csgsoluciones/metro-santiago.git