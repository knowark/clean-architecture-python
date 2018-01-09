# Proyecto *Taskit*

Realizaremos una aplicación para gestionar nuestras tareas por realizar. En general, la estructura de la aplicación estará compuesta por:

- **Tarea** (task): Unidad básica de gestión del trabajo cuyos atributos serán:
  - UID (uid: str)
  - Nombre (name: str)
  - Fecha Límite (due_date: datetime)
  - Prioridad (priority: int)
  - ID Proyecto (project_id: str)
  - ID Etapa (stage_id: str)
  - Comentarios (comments: str)

- **Proyecto** (project): Contenedor de tareas con un mismo propósito cuyos atributos serán:
  - UID (uid: str)
  - Nombre (name: str)
  - Etapas (stage_ids: List[str])
  - Comentarios (comments: str)

- **Etapa** (stage): Estado en el que puede estar cada tarea. Un proyecto tiene múltiples etapas. Sus atributos son:
  - UID (uid: str)
  - Nombre (name: str)
  - Cierre (closure: bool)

La aplicación nos permitirá:

- Crear, leer, modificar y eliminar nuevas tareas, proyectos y etapas.
- Asignar tareas a proyectos específicos.
- Definir la prioridad y fecha límite de cada tarea.
- Mover las tareas por las distintas etapas del proyecto hasta el estado de cierre.

Igualmente, implementaremos algunas restricciones:

- Un proyecto sólo podrá tener una etapa de cierre.
- No se podrán eliminar tareas en estado de cierre.
- Habrá un proyecto, entre todos, que se usará por defecto cuando no se especifique alguno en las tareas.

Finalmente, obtendremos información valiosa para analizar detalladamente nuestro trabajo pudiendo:

- Reportar las tareas con fecha límite igual o inferior al día actual, los próximos 7 días, etc.
- Reportar las tareas que se encuentran en un mismo proyecto.
- Reportar las tareas que se encuentran en una misma etapa (a través de todos los proyectos).
