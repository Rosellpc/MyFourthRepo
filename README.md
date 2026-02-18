# 🧑‍💼 Sistema de Recursos Humanos (RRHH) en Python

Sistema de gestión de empleados desarrollado en **Python**, orientado a la administración básica de Recursos Humanos desde consola.  
Permite gestionar empleados, salarios y credenciales de forma **segura**, aplicando **Programación Orientada a Objetos (POO)** y persistencia de datos mediante archivos CSV.

---

## 📌 Características principales

- ➕ Registro de nuevos empleados
- 📋 Listado de empleados
- 💰 Actualización de salarios con verificación de contraseña
- 🔐 Gestión segura de contraseñas (SHA-256)
- 🗑 Eliminación de empleados
- 💾 Persistencia automática de datos en archivo CSV
- 🔄 Carga de datos al iniciar el sistema

---

## 🧠 Arquitectura del proyecto

El sistema está diseñado bajo principios de **POO**, separando responsabilidades:

### 🔹 Clase `Empleado`
Responsable de:
- Almacenar información del empleado
- Proteger datos sensibles
- Validar credenciales
- Actualizar salario y contraseña

### 🔹 Clase `SistemaRRHH`
Responsable de:
- Gestionar el ciclo de vida de los empleados
- Manejar la persistencia de datos
- Proveer el menú interactivo
- Centralizar la lógica del sistema

---

## 🔐 Seguridad

- Las contraseñas **no se almacenan en texto plano**
- Se utiliza **SHA-256** para el hash de credenciales
- Los atributos sensibles están protegidos mediante encapsulación (`_` y `__`)

> ⚠️ Nota: Este sistema es educativo/prototipo.  
> Para producción se recomienda usar `bcrypt` o `argon2`.

---

## 📂 Persistencia de datos

Los empleados se almacenan en un archivo:

```text
empleados.csv
