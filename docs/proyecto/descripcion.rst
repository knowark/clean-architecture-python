Descripción
***********

Realizaremos una aplicación para gestionar nuestras tareas por realizar.
En general, la estructura de la aplicación estará compuesta por:

`Taskit Repo <https://github.com/nubark/clean-architecture-python.git>`_

|  - **Tarea** (task): Unidad básica de gestión del trabajo cuyos atributos serán:
|    UID (uid: str)
|    Nombre (name: str)
|    Fecha Límite (due_date: datetime)
|    Prioridad (priority: int)
|    ID Proyecto (project_id: str)
|    Etapa (stage: str)
|    Comentarios (comments: str)

|  - **Proyecto** (project): Contenedor de tareas con un mismo propósito cuyos
   atributos serán:
|    UID (uid: str)
|    Nombre (name: str)
|    Comentarios (comments: str)

La aplicación nos permitirá:

- Crear, leer, modificar y eliminar nuevas tareas y proyectos.
- Asignar tareas a proyectos específicos.
- Mover las tareas por las distintas etapas del proyecto hasta el
  estado de cierre.

Obtendremos información valiosa para analizar detalladamente
nuestro trabajo pudiendo:

- Reportar todas las tareas registradas.
- Reportar todos los proyectos registrados.
- Reportar todas las tareas pertenecientes a un mismo proyecto.
- Reportar todas las tareas con la misma etapa.
