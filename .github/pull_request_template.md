### Descripción del cambio
Este Pull Request introduce la implementación completa de un **Sistema de Recursos Humanos (RRHH)** desarrollado en Python, orientado a la gestión básica de empleados desde consola.

El sistema permite:
- Crear, listar, actualizar y eliminar empleados.
- Gestionar salarios de forma segura mediante verificación de contraseña.
- Cambiar contraseñas con almacenamiento encriptado.
- Persistir los datos en un archivo CSV para mantener la información entre ejecuciones.

Se ha aplicado **Programación Orientada a Objetos (POO)**, encapsulación de datos y buenas prácticas de seguridad básica.

---

### ¿Cuál es el contexto de este cambio?
Este cambio responde a la necesidad de contar con un sistema simple, extensible y seguro para la administración de empleados, ideal como base para:
- Proyectos educativos.
- Prototipos de sistemas administrativos.
- Evolución futura hacia una aplicación con interfaz gráfica o backend.

Además, el proyecto sirve como ejercicio práctico de:
- Manejo de archivos (`csv`)
- Encapsulación y control de acceso a atributos
- Encriptación de contraseñas usando `hashlib (SHA-256)`

---

### ¿Cómo se probaron estos cambios?
Los cambios fueron probados manualmente mediante el menú interactivo del sistema, validando los siguientes flujos:

1. Creación de empleados con salario y contraseña.
2. Listado correcto de empleados registrados.
3. Actualización de salario validando contraseña.
4. Cambio de contraseña con verificación previa.
5. Eliminación de empleados.
6. Persistencia correcta de datos en `empleados.csv` al cerrar el sistema.
7. Carga automática de empleados desde el archivo CSV al reiniciar el programa.

---

### ¿Existen tickets relacionados?
No existen tickets asociados actualmente.  
Este PR corresponde a la implementación inicial del sistema.

---

### Captura de pantalla (si aplica)
No aplica.  
El sistema es una aplicación de consola sin interfaz gráfica.

---

### Checklist
- [x] He seguido las convenciones de estilo de código de este repositorio.
- [x] He aplicado principios de Programación Orientada a Objetos.
- [x] La información sensible (contraseñas) se almacena de forma encriptada.
- [x] El sistema fue probado manualmente y funciona según lo esperado.
- [x] El código está documentado mediante docstrings y comentarios claros.

---

### Otros comentarios
Este sistema puede escalar fácilmente hacia:
- Uso de bases de datos (SQLite / PostgreSQL).
- Separación por capas (MVC).
- Integración con pruebas unitarias.
- Interfaz gráfica o API REST.

Quedo atento a sugerencias de mejora o refactorización.
