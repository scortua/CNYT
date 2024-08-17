# NÚMEROS COMPLEJOS

Los números complejos son descubiertos por la humanidad en la busqueda de la solución de un polinomio, al cual despúes de un largo trabajo de historia se halló el número imaginario i y con eso encontraron una nueva representación de números llamados **números complejos**.

> a:= número real
> b:= número real
> a + bi := número complejo
> (a,b):= número complejo 

## OPERACIONES DE LOS NÚMEROS COMPLEJOS

Este como otros conjuntos, tambien tiene las propiedades aritméticas y gráficas que tienen otros conjuntos como el de los números reales y en esta carpeta se realizaron las siguiente operaciones.

```
La implementación de las operaciones matemáticas con complejos fue hecha en python 3.12
```

El proposito fue generar una libreria que permitiera a partir de tuplas la aritmética de los números complejos que se describen en seguida:

> Tener en cuenta para los ejemplos:
> (a,b) = a + bi 
> (c,d) = c + di
> Son números complejos.

- **Suma**
La suma de números complejos es muy similar a la suma de números reales, igual es muy fácil explicarlo al compararlo con la suma de vectores, pues la suma viene dada con la suma de cada coordenada, reales con reales e imaginarios con imaginarios.

        $(a,b) + (c,d) = (a+c,b+d)$
- **Multiplicación**
La multiplicación de números imaginarios es simplemente similar a la distribución de cada número.

        $(a,b) * (c,d) = (a+bi)(c+di)= (ac - bd, ad + bc)$
- **Resta**
La resta tiene la misma explicación de la suma que se habia dado anteriormente, solamente se cambia el signo de las componentes del número que resta.

        $(a,b) - (c,d) = (a - c, b - d)$
- **División**
La división llega a ser algo más complejo en la explicación, pero tampoco es imposible demostrar porque la división de un número complejo con otro es la que se muestra a continuación.

        $\frac{(a,b)}{(c,d)} = (\frac{ac + bd}{c^2 + d^2}, \frac{bc - ad}{c^2 + d^2})$
- **Modulo**
El modulo de un número complejo tiene la misma forma de hallar que la magnitud de un vector.

        $|(a,b)| = \sqrt{a^2 + b^2}$
- **Conjugado**
El conjugado de un número complejo es la simetria que tiene con el eje X o el eje real en este caso.

        $(a,b) => (a,-b)$
- **Cordenadas**
Existen un montón de coordenadas que se le pueden asignar, para los números complejos estan las coordenadas cartesianas y las polares que ya se han trabajado y explicado en cursos que se hablan de vectores.

        - Cartecianas
                $(a,b) = a + bi$
        - Polar
                $(r,θ)$ 
- **Fase**
La fase de un número complejo esta dado por el ángulo que forma y la región en la que se encuentra para ubicarlo correctamente. 

        $θ = arctan(\frac{a}{b})$

