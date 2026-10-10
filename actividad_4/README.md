# Sistema de Agrupamiento de Pasajeros - Metro de Santiago

Proyecto desarrollado en Python para aplicar técnicas de Aprendizaje No Supervisado utilizando el algoritmo K-Means, con el objetivo de identificar grupos de pasajeros con características similares según la cantidad de pasajeros y la hora del día.

# Descripción
Este proyecto utiliza un conjunto de datos relacionado con la operación del Metro de Santiago y aplica técnicas de Machine Learning para identificar agrupaciones de registros con características similares.

A diferencia del Aprendizaje Supervisado, en este caso el algoritmo no posee respuestas correctas previamente definidas, sino que descubre patrones y grupos de manera automática.

El sistema fue desarrollado utilizando:

* Python

* Pandas

* Scikit-Learn

# Objetivo
Desarrollar un modelo de aprendizaje no supervisado capaz de identificar agrupaciones de pasajeros en el Metro de Santiago utilizando la cantidad de pasajeros y la hora del día como variables de análisis.

# Dataset Utilizado
El conjunto de datos fue almacenado en un archivo CSV y contiene:

Cantidad de pasajeros

Hora del día

Las variables utilizadas son:

Variable Descripción Cantidad_Pasajeros Número de pasajeros registrados Hora_Dia Hora del día entre 0 y 23

Ejemplo de datos:

Cantidad_Pasajeros,Hora_Dia
120,8
150,9
180,10
220,11
250,12
300,13
...
# Tecnologías Utilizadas
* Python 3.11

* Pandas

* Scikit-Learn

* Visual Studio Code

# Modelo Utilizado
El proyecto utiliza el algoritmo:

# K-Means

Este algoritmo pertenece al Aprendizaje No Supervisado y permite identificar grupos con características similares sin necesidad de utilizar una respuesta conocida.

La configuración utilizada fue:

modelo = KMeans(
    n_clusters=2,
    random_state=42
)
Agrupamientos Detectados
El modelo identificó automáticamente dos grupos:

Grupo 0
Promedio obtenido:

246.25 pasajeros
Interpretación:

Baja afluencia de pasajeros
Grupo 1
Promedio obtenido:

913.75 pasajeros
Interpretación:

Alta afluencia de pasajeros
Resultados Obtenidos
El algoritmo K-Means agrupó correctamente los registros del dataset en dos categorías:

Grupo de baja afluencia de pasajeros.

Grupo de alta afluencia de pasajeros.

Estos resultados permiten identificar patrones de comportamiento en los datos del Metro de Santiago sin utilizar una variable objetivo.

# Que puede realizar este proyecto:

Descubrir agrupaciones automáticamente.
Estructura del Proyecto
actividad_4
│
├── dataset_metro.csv
├── aprendizaje_no_supervisado.py
└── README.md

# Autores

Daisy Nicol Malagón Ramírez
Guillermo Andrés Carrillo Sánchez

# Repositorio
https://github.com/csgsoluciones/metro-santiago.git