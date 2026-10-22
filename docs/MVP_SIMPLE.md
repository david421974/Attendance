# MVP Simple · Control de attendance

Este MVP mantiene la idea inicial del proyecto: ofrecer un flujo sencillo de acceso y consulta de información, construyendo una base sólida para futuras funcionalidades relacionadas con asistencia, presencia y reuniones.

---

# Objetivo

Validar una primera versión funcional que permita:

- Acceso de usuarios mediante autenticación básica.
- Visualización de información resumida de actividad.
- Persistencia de datos mediante SQLite.
- Preparar la arquitectura para futuras ampliaciones sin incrementar complejidad innecesaria.

---

# Funcionalidades incluidas

## Backend FastAPI

Endpoints disponibles:

- `POST /api/login`
  - Valida credenciales de usuario.

- `GET /api/mvp/resumen`
  - Devuelve información resumida para mostrar en la interfaz.

## Frontend Angular

Incluye:

- Formulario de inicio de sesión.
- Mensajes de validación.
- Visualización de métricas básicas.
- Preparado para incorporar nuevas funcionalidades en futuras iteraciones.

---

# Credenciales Demo

## Administrador

```text
Usuario: admin
Contraseña: 1234
```

## Invitado

```text
Usuario: invitado
Contraseña: demo
```

---

# Arquitectura Actual

```text
attendance/
├─ main.py
├─ app/
│  ├─ database.py
│  ├─ models/
│  │  ├─ __init__.py
│  │  └─ usuario.py
│  └─ services/
├─ database/
│  └─ attendance.db
├─ angular/frontend/
└─ docs/
```

---

# Base de Datos

## Tecnología seleccionada

### SQLite

El MVP utiliza SQLite como mecanismo de persistencia.

### Motivos

- No requiere instalación de servicios adicionales.
- No requiere permisos de administrador.
- Reduce la complejidad de despliegue.
- Facilita el desarrollo en entornos corporativos restringidos.
- Permite evolucionar rápidamente durante las primeras fases del proyecto.

### Evolución prevista

La arquitectura se construye utilizando SQLModel para permitir una futura migración a PostgreSQL con cambios mínimos.

```text
Estado actual

SQLite
   ↓
SQLModel
   ↓
FastAPI

Evolución futura

PostgreSQL
     ↓
SQLModel
     ↓
FastAPI
```

---

# Flujo de Confirmación de Reuniones

## Objetivo

Determinar si una persona está realmente presente en una reunión programada.

La finalidad es mejorar la calidad de la información de asistencia y presencia, evitando depender únicamente de las invitaciones de calendario.

---

## Flujo funcional

```text
Calendario corporativo
        │
        ▼
Detección de reunión
        │
        ▼
Notificación al usuario
        │
        ▼
¿Estás presente en esta reunión?
        │
   ┌────┼────┐
   ▼    ▼    ▼
  Sí    No   Más tarde
   │    │        │
   ▼    ▼        ▼
Presente  Ausente  Nuevo recordatorio
```

---

## Experiencia de usuario

Ejemplo:

```text
Sprint Planning
10:00 - 11:00
```

La aplicación detecta la reunión y muestra:

```text
¿Estás presente en la reunión "Sprint Planning"?
```

Opciones disponibles:

- ✅ Sí, estoy presente
- ❌ No estoy presente
- ⏰ Recordármelo más tarde

---

## Información registrada

Para cada confirmación se almacenará:

```text
Usuario
Reunión
Fecha
Hora
Respuesta
Tiempo de respuesta
```

Ejemplo:

```text
Usuario: Ibar Vivas
Reunión: Sprint Planning
Fecha: 22/10/2026
Hora: 10:01
Respuesta: Presente
```

---

## Beneficios esperados

- Mayor precisión en la información de asistencia.
- Confirmación explícita por parte del usuario.
- Generación de métricas fiables.
- Base para cuadros de mando e informes futuros.
- Posibilidad de detectar ausencias recurrentes o reuniones sin participación activa.

---

# Hoja de Ruta

## Fase 1 · MVP Actual

✅ Login básico

✅ Resumen de actividad

✅ Frontend Angular

✅ Backend FastAPI

✅ Persistencia con SQLite

✅ Arquitectura basada en SQLModel

---

## Fase 2 · Usuarios y Persistencia

⏳ CRUD completo de usuarios

⏳ Gestión de sesiones

⏳ Historial de actividad

⏳ Configuración básica de usuarios

---

## Fase 3 · Reuniones

⏳ Integración con calendario corporativo

⏳ Detección automática de reuniones

⏳ Solicitud de confirmación de presencia

⏳ Registro histórico de respuestas

---

## Fase 4 · Métricas

⏳ Dashboard de asistencia

⏳ Indicadores individuales

⏳ Indicadores por equipo

⏳ Informes de seguimiento

---

## Fase 5 · Escalado Organizativo

⏳ Departamentos

⏳ Roles

⏳ Gestión de responsables

⏳ Informes para managers

⏳ Exportación de datos

---

# Arranque del Proyecto

## Backend

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## Frontend

```bash
cd angular/frontend
npm start
```

---

## URLs

Frontend:

```text
http://localhost:4200
```

API Swagger:

```text
http://localhost:8000/docs
```

---

# Arranque Conjunto

Desde la raíz del proyecto:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-dev.ps1
```

### Opciones útiles

```powershell
# Mostrar únicamente los comandos
powershell -ExecutionPolicy Bypass -File .\scripts\start-dev.ps1 -DryRun
```

```powershell
# Backend en nueva ventana y frontend en la actual
powershell -ExecutionPolicy Bypass -File .\scripts\start-dev.ps1 -SameWindow
```

---

# Mensaje de Presentación

> Hemos desarrollado una primera versión funcional orientada a validar el flujo principal de autenticación y visualización de información operativa. La solución utiliza SQLite para minimizar dependencias y facilitar su despliegue en entornos con restricciones de instalación. La arquitectura ha sido diseñada para evolucionar progresivamente hacia funcionalidades de control de presencia, gestión de reuniones y análisis de asistencia, manteniendo una base técnica escalable desde el inicio.