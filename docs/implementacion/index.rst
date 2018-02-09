Implementación
##############


!Arquitectura que Grita!
************************

El propósito de nuestras aplicaciones debe hacerse notar de primera mano.

La Regla de las Dependencias
****************************

Las dependencias de una aplicación deben dirigirse en la vía de mayor
abstracción.

Capas y Fronteras
*****************

Los componentes de una aplicación se comunican entre sí a través de fronteras
bien definidas.

Los Detalles
************

Las consideraciones de infraestructura son sólo *detalles* del sistema.
La base de datos, el framework web, las librerías de consola, son sólo
herramientas de nuestras aplicaciones y no su esencia.

```
For the framework author, coupling to his or her own framework is not a risk...

The author wants you to couple to the framework, because once coupled in this
way, it is very hard to break away.
```

El Componente Principal
***********************

El más sucio de los componentes. Es el encargado de instanciar el arbol de
dependencias para crear la aplicación final.