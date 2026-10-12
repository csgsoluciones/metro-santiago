# Sistema de Predicción de Demoras - Metro de Santiago

Proyecto desarrollado en Python que aplica aprendizaje supervisado, mediante un Árbol de Decisión, para predecir posibles demoras en el Metro de Santiago según la cantidad de pasajeros y la hora del día. Continúa el proyecto de transporte masivo de las actividades anteriores.

## Objetivo

Desarrollar un modelo de aprendizaje supervisado capaz de predecir si existirá una demora en el servicio, utilizando como variables de entrada la cantidad de pasajeros y la hora del día.

## Fuentes de datos

No se utilizó una fuente de datos real. Por esa razón se desarrolló un conjunto de datos simulado que representa una muestra de la operación del Metro. El dataset se genera automáticamente al ejecutar el script, con NumPy y una semilla fija (`np.random.seed(42)`), por lo que los resultados son reproducibles en cualquier computador.

## Descripción de los datos

El conjunto contiene 100 registros: 60 sin demora y 40 con demora.

| Variable | Tipo | Descripción |
|---|---|---|
| Cantidad_Pasajeros | Numérica (100 a 999) | Número de pasajeros registrados |
| Hora_Dia | Numérica (0 a 23) | Hora del día |
| Demora | Categórica (0 o 1) | 0 = no existe demora, 1 = existe demora. Es la variable a predecir |

La variable objetivo se generó con la siguiente regla:

```python
if pasajeros > 600:
    demora.append(1)
else:
    demora.append(0)
```

## Tecnologías utilizadas

- Python 3.12
- Pandas
- NumPy
- Scikit-Learn

## Modelo utilizado

Se utilizó un Árbol de Decisión (`DecisionTreeClassifier`), que aprende patrones a partir de los datos de entrenamiento y luego genera predicciones sobre casos nuevos ingresados por el usuario.

## División de datos

Mediante `train_test_split()` los datos se dividieron en:

- 70% para entrenamiento (70 registros)
- 30% para prueba (30 registros)

## Métricas de evaluación

Se utilizaron tres métricas:

- Accuracy Score
- Matriz de Confusión
- Classification Report

## Resultados obtenidos

- Precisión del modelo: 1.00
- Matriz de confusión: `[[19 0] [0 11]]`. Los 30 registros de prueba fueron clasificados correctamente (19 sin demora y 11 con demora).

Como la variable Demora se generó con una regla fija basada únicamente en la cantidad de pasajeros, el árbol aprende esa regla con un solo corte y alcanza una precisión perfecta. Con datos reales no se esperaría un resultado tan exacto.

## Cómo ejecutar

Instalar las librerías (una sola vez):

```
pip install pandas numpy scikit-learn
```

Ejecutar el programa desde la carpeta `actividad_3`:

```
python aprendizaje_supervisado.py
```

El programa muestra los primeros registros y las métricas del modelo, y luego solicita por teclado la cantidad de pasajeros y la hora para realizar una predicción.

## Pruebas realizadas

| Pasajeros | Hora | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| 100 | 14 | Sin demora | No se espera demora |
| 900 | 18 | Con demora | Es probable que exista demora |
| 50 | 8 | Sin demora | No se espera demora |
| 900 | 3 | Con demora | Es probable que exista demora |

En las pruebas se observa que, con estos datos simulados, el resultado depende de la cantidad de pasajeros y no de la hora: 900 pasajeros producen demora tanto a las 18 como a las 3.

## Estructura del proyecto

```
actividad_3/
├── aprendizaje_supervisado.py
└── README.md
```

## Autores y aportes

- Daisy Nicol Malagón Ramírez
- Guillermo Andrés Carrillo Sánchez

## Repositorio

https://github.com/csgsoluciones/metro-santiago