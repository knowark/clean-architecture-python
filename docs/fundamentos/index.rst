Fundamentos
###########

Podría decirse que *Clean Architecture* no inventa nada nuevo, sino que agrupa
metodologías, principios y patrones de diseño conocidos en la industria del
software desde hace décadas. Sin embargo, lo que *Clean Architecture* sí trae
a la mesa es su objetivo: crear aplicaciones flexibles que sean fáciles de
mantener en el tiempo.

SOLID
*****

- **S-ingle Responsability Principle**

    *Un módulo debería tener una, y sólo una, razón para cambiar*

    *Un módulo debería ser responsabilidad de un sólo actor*

.. todo::
   Ejemplo de clase "Empleado" con métodos calculatePay (CFO),
   reportHours (COO) y save (CTO)


- **O-pen/Closed Principle**

    *Un artefacto de software debería estar abierto para su extensión
    pero cerrado para su modificación*

.. todo::
   Esto impacta como estructuramos los componentes de nuestras aplicaciones,
   para dirigir las *dependencias* eficientemente. Se trata sobre todo de
   evitar ciclos de dependencias y de proteger aquellos componentes que cambian
   con menos frecuencia y son más abstractos (i.e. son de más alto *nivel*).

- **L-iskov Substitution Principle**

    *Lo que se quiere aquí es algo como la siguiente propiedad de substitución:
    Si para cada objeto *o1* de tipo *S* hay un objeto *o2* de tipo *T*, tal que
    para todos los programas *P* definidos en términos de *T*, el comportamiento
    de *P* no se modifica cuando *o1* es substituido por *o2* entonces *S* es
    un subtipo de *T*.

    *Barbara Liskov, 1988*

.. todo::
   Este principio podría ser la definición formal de lo que conocemos como
   *duck-typing*. Seguir este principio, nos permite crear aplicaciones que
   sean extensibles a través de *plugins*.


- **I-nterface Segregation Principle**

   *Es perjudicial depender de módulos que contienen más de lo que se necesita*

   *Varias interfaces específicas por cliente son mejores que una sóla interfaz
   de propósito general*

.. graphviz:: media/interface-segregation.dot

.. todo::
   No es tan crítico en Python al ser un lenguaje dinámico dónde un cambio en
   las dependencias no implica recompilación.

- **D-ependency Inversion Principle**

    *Los sistemas más flexibles son aquellos en los que las dependencias de
    código se refieren a abstracciones y no a concreciones*

.. graphviz:: media/dependency-inversion-1.dot
.. graphviz::

   digraph foo {
      "VS";
   }
.. graphviz:: media/dependency-inversion-2.dot

.. todo::
   Se debe tener cuidado con la *volatilidad* de componentes *concretos* y no
   depender de ellos.

Tipos de Programación
*********************

- **Programación Estructurada**

    *Impone disciplina en la transferencia directa de control*

    *Resuelve el problema de los 'GOTO' mediante la iteración y selección*

- **Programación Orientada a Objetos**

    *Impone disciplina en la la transferencia indirecta de control*

    *Resuelve el problema de los punteros a funciones mediante clases y objetos*

- **Programación Funcional**

    *Impone disciplina en la asignación*

    *Resuelve problemas de condiciones de carrera mediante la inmutabilidad*

Modelado del Dominio
********************

El núcleo de una aplicación es el dominio que tiene como propósito modelar.
Este dominio se representa a través de lo que llamamos, la lógica de negocio.

.. image:: media/bounded-context.png
   :width: 400px
   :height: 300px
   