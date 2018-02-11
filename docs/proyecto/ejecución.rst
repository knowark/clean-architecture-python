Ejecución
*********

El repositorio contiene 6 ramas de desarrollo incremental:

- feat/01_models
- feat/02_repositories
- feat/03_coordinators
- feat/04_infrastructure
- feat/05_reports
- feat/06_main

Cada una de ellas construye una capa o componente de la aplicación. En el
proceso de recrear esta construcción, usaremos un enfoque de desarrollo
guiado por pruebas (i.e. *TDD*). Esto asegurará que los componentes que
diseñemos, se encuentren desacoplados desde el inicio y sean fáciles de
extender.

Todos iniciarán en la rama *feat/docs* la cuál no contiene código. En el
proyector se presentará el *estado* o rama objetivo. En la primera iteración
esta rama será la *feat/01_models*. En la segunda iteración, cuando hayamos
alcanzado el estado de la rama *feat/01_models*, la rama objetivo será la
*feat/02_repositories*. Así lo haremos sucesivamente hasta completar la 
aplicación.

Dedicaremos un tiempo máximo de 15 minutos a cada fase. Si al completarse los
15 minutos no se ha terminado la totalidad de la funcionalidad requerida,
lamentablemente tendremos que ejecutar **git reset --hard**. Por supuesto,
pueden guardar sus cambios en una rama temporal si quieren (e.g. my/01_models).
La idea es contar con el tiempo suficiente para abordar la totalidad de la
aplicación. No se preocupen, tendrán tiempo de sobra para seguir el paso a
paso en la comodidad de sus casas ;D

Comandos Importantes
====================

- Correr los tests con pytest:

    pytest -s --cov-report term-missing --cov-branch --cov taskit tests

- Empaquetar nuestra 

    pyinstaller -F taskit/__main__.py -n taskit

Finalmente
==========

**¡Manos a la obra!**
