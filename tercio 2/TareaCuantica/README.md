
# Tarea: Teoría Cuántica Básica, Observables y Medidas
## Ingeniería Electrónica y de Sistemas
**Autor**: Santiago Cortes Tovar  
**Materia**: CNYT

## Descripción General:
Esta tarea explora conceptos fundamentales de la teoría cuántica, incluyendo la simulación de un sistema cuántico y la obtención de probabilidades relacionadas con estados cuánticos (ket). Se abordan dos problemas principales:

### 1. Simulación de un sistema cuántico descrito en la Sección 4.1
El sistema modela una partícula confinada en un conjunto discreto de posiciones a lo largo de una línea. A continuación, se realizan dos cálculos importantes:

1. **Cálculo de la probabilidad de encontrar la partícula en una posición específica**:
    - Se ingresa un vector ket de estado, compuesto por amplitudes complejas.
    - Este vector se normaliza y, posteriormente, se calcula la probabilidad de encontrar la partícula en una posición dada, utilizando la fórmula:
    $P(x_j) = \frac{|C_j|^2}{\\sum{|C_i|^2}}$

2. **Probabilidad de transición entre dos vectores de estado**:
    - Se proporcionan dos vectores ket de estado.
    - Se normalizan ambos vectores y se calcula el producto interno entre ellos, lo cual equivale a la amplitud de transición.

### 2. Código Implementado
El código en Python implementado permite:
- Solicitar al usuario la cantidad de elementos en el vector ket.
- Llenar el vector con números complejos ingresados por el usuario.
- Normalizar el vector y calcular la probabilidad de encontrar la partícula en una posición particular.
- Calcular la probabilidad de transición entre dos vectores ket distintos.


