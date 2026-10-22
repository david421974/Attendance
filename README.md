# Control de attendance

Proyecto en desarrollo para gestionar la asistencia de personas a actividades o jornadas dentro de un equipo/interproyecto. La idea principal es permitir registrar quién está presente, desde qué equipo procede, en qué convocatoria o actividad participa y mantener ese registro de forma organizada para su consulta posterior.

Este repositorio está en una fase inicial de prototipo funcional. Ya se ha dejado una base web con acceso inicial y una pantalla de login, pero aún queda definir parte de la lógica de negocio, autenticación, almacenamiento y flujo de validación de usuarios.

---

## ¿Qué es este proyecto?

Es una aplicación web para controlar la asistencia de personas asociadas a equipos, con la finalidad de:

- registrar la participación de un usuario;
- identificar al usuario y a su equipo;
- validar la asistencia en una actividad concreta;
- guardar un histórico de attendances o registros;
- facilitar la consulta posterior de esos datos.

La intención inicial del proyecto es cubrir casos como:

- registro individual de personas asociadas a equipos;
- participación en actividades concretas (por ejemplo Talent Up lunes o Talent Up jueves);
- control de asistencia con datos de ubicación, fecha y hora;
- almacenamiento de la información para consulta posterior.

---

## Estado actual del proyecto

### Implementado

- Base de aplicación web con FastAPI.
- Pantalla de acceso / login con interfaz HTML.
- Estructura de carpetas inicial para seguir desarrollando la app.
- Entorno de ejecución listo con `uv`.

### Pendiente de desarrollo

- autenticación real (SSO o login con usuarios registrados);
- registro y validación de personas frente a su equipo;
- captura de localización / geolocalización;
- registro de fecha y hora de asistencia;
- formulario de actividad en curso;
- almacenamiento persistente en base de datos o Excel/SharePoint;
- historial y consultas de registros;
- gestión de usuarios y equipos;
- diseño de frontend definitivo;
- despliegue y entorno de producción.

---

## Funcionalidades implementadas actualmente

Hasta el momento, lo que sí existe es lo siguiente:

- servidor FastAPI funcionando en Python;
- ruta principal de acceso a `/login`;
- template HTML para la pantalla de inicio de sesión;
- estilo visual simple con Tailwind CSS para una primera versión de frontend.

Esto supone una base válida para continuar con el desarrollo del flujo principal del proyecto, pero aún no es una versión completa de negocio.

---

## Requisitos previos

Necesitas tener instalado en tu equipo:

- Python 3.12 o superior
- `uv` (gestor de paquetes y entorno recomendado para este proyecto)
- Git
- Un navegador moderno (Chrome, Edge, Firefox)

También conviene tener claro que este proyecto está pensado para seguir evolucionando. En este punto, aún falta definir parte de la infraestructura de datos y autenticación.

---

## Instalación y configuración

1. Clona el repositorio:

```bash
git clone https://github.com/david421974/attendance.git
cd attendance
```

2. Crea o sincroniza el entorno virtual con `uv`:

```bash
uv sync
```

3. Si el entorno no está creado todavía, también puedes hacerlo manualmente con:

```bash
uv venv
```

4. Activa el entorno si lo necesitas desde terminal:

- En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

- En Git Bash / bash:

```bash
source .venv/Scripts/activate
```

---

## Cómo arrancar la aplicación

Desde la raíz del proyecto, la forma recomendada por la propia documentación de FastAPI es:

```bash
uv run fastapi dev
```

### ¿Por qué se recomienda `uv run fastapi dev`?

FastAPI recomienda este comando porque está pensado para que el proyecto se ejecute de forma más sencilla y consistente durante el desarrollo:

- `uv run`: ejecuta el comando dentro del entorno del proyecto, sin depender de que el entorno esté activado manualmente.
- `fastapi dev`: usa la CLI de FastAPI para arrancar la aplicación en modo desarrollo.
- este modo está pensado para facilitar pruebas rápidas y recarga automática al detectar cambios en el código.
- además, mantiene una experiencia más clara para proyectos que siguen la estructura recomendada por FastAPI, sin tener que recordar la sintaxis exacta de `uvicorn` cada vez.

En otras palabras, es la opción más directa y recomendada para comenzar a desarrollar, porque te evita errores de entorno y te da un arranque más amigable para el desarrollo local.

### Alternativa equivalente con uvicorn

También puedes arrancarlo manualmente así:

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### ¿Qué hace este comando?

- `uv run`: ejecuta la app en el entorno del proyecto.
- `uvicorn`: levanta el servidor web.
- `main:app`: indica que la aplicación FastAPI está en `main.py` y la variable `app`.
- `--reload`: reinicia automáticamente el servidor al detectar cambios.
- `--host 0.0.0.0`: permite acceder desde localhost y desde red local si hace falta.
- `--port 8000`: sirve la app en el puerto 8000.

Una vez arrancado, abre esta dirección en el navegador:

```text
http://localhost:8000/login
```

---

## Cómo verificar que funciona correctamente

### Verificación rápida

1. Arranca la app con el comando anterior.
2. Abre la URL `http://localhost:8000/login`.
3. Debes ver una pantalla con el título: `Iniciar Sesión`.
4. En la interfaz aparecerán campos para usuario/email y contraseña.

### Verificación desde terminal

Si quieres comprobarlo sin navegador, puedes hacer una petición HTTP:

```bash
curl -i http://127.0.0.1:8000/login
```

Si la aplicación responde con `200 OK`, la ruta está funcionando.

---

## Estructura principal del proyecto

```text
attendance/
├── main.py                 # punto de entrada de la aplicación FastAPI
├── pyproject.toml          # configuración del proyecto y dependencias
├── README.md               # documentación del proyecto
├── .venv/                  # entorno virtual local
├── database/               # carpeta para almacenamiento o datos del proyecto
├── src/                    # módulos o lógica interna del proyecto
├── templates/              # plantillas HTML del frontend
│   └── login.html          # pantalla inicial de acceso
└── uv.lock                 # lock file generado por uv
```

### Archivos clave

- `main.py`: contiene la app FastAPI y la ruta de login.
- `templates/login.html`: interfaz principal del acceso.
- `pyproject.toml`: define dependencias y configuración del proyecto.
- `src/`: lugar donde irán módulos de negocio, validaciones y lógica adicional.
- `database/`: será el punto de almacenamiento de registros o integración con Excel/SharePoint.

---

## Pendiente de completar

Esta sección recoge la información que aún falta por definir para cerrar la documentación técnica y funcional del proyecto.

### Datos que faltan por concretar

- nombre final del proyecto y repositorio público definitivo;
- arquitectura exacta de frontend (si será HTML, React, Vue, etc.);
- mecanismo de autenticación: SSO, login local o integración con Microsoft;
- modelo de datos completo: usuarios, equipos, actividades, registros y convocatorias;
- definición de la tabla/estructura para almacenar asistencias;
- origen final del almacenamiento: Excel, SharePoint, base de datos SQL o NoSQL;
- reglas de validación de personas y equipos;
- campos exactos de geolocalización y permiso de ubicación;
- flujo de pantalla tras login y listado de actividades;
- criterios de negocio sobre qué cuenta como asistencia válida;
- requisitos de despliegue y entorno de producción.

### Recomendación

Antes de seguir con más desarrollo, conviene cerrar una hoja de requisitos con:

1. quiénes son los usuarios finales;
2. qué datos necesitan registrar;
3. dónde se almacenarán;
4. qué validaciones deben aplicarse;
5. qué flujo de acceso y permisos tendrá cada persona.

---

## Requisitos funcionales del proyecto (visión general)

El proyecto busca cubrir, al menos, estas necesidades:

- validar que una persona se registra desde su equipo;
- asociar los equipos a personas físicas;
- registrar GGID, nombre personal y nombre del equipo;
- pedir la localización, fecha y hora;
- permitir seleccionar la actividad en curso;
- apoyar actividades como Talent Up lunes y Talent Up jueves;
- guardar la información para consulta posterior;
- registrar la convocatoria o motivo de asistencia;
- almacenar la información en un sistema que pueda consultarse y reutilizarse.

---

## Observaciones importantes

- La aplicación está todavía en una fase inicial de prototipo.
- El frontend no está cerrado ni definido en una arquitectura definitiva.
- El almacenamiento final aún no está definido de manera completa.
- La lógica de negocio y autenticación deben completarse antes de considerar el sistema listo para uso real.

---

## Siguiente paso recomendado

El siguiente gran bloque de trabajo debería ser:

1. definir la autenticación y el flujo de acceso;
2. decidir el modelo de datos y almacenamiento;
3. construir el formulario principal de attendance;
4. conectar la app con la base de datos o SharePoint/Excel;
5. validar el flujo completo de registro y consulta.

Si quieres, el siguiente paso puede ser dejar una segunda versión del README más orientada a GitHub, con badges, capturas y un apartado de “roadmap” más visual.

```
attendance
├─ .python-version
├─ angular
│  └─ angular-app
│     └─ frontend
│        ├─ .editorconfig
│        ├─ .prettierrc
│        ├─ angular.json
│        ├─ package-lock.json
│        ├─ package.json
│        ├─ public
│        │  └─ favicon.ico
│        ├─ README.md
│        ├─ src
│        │  ├─ app
│        │  │  ├─ app.config.ts
│        │  │  ├─ app.html
│        │  │  ├─ app.routes.ts
│        │  │  ├─ app.scss
│        │  │  ├─ app.spec.ts
│        │  │  └─ app.ts
│        │  ├─ index.html
│        │  ├─ main.ts
│        │  └─ styles.scss
│        ├─ tsconfig.app.json
│        ├─ tsconfig.json
│        └─ tsconfig.spec.json
├─ angular-app
├─ data
│  ├─ database
│  │  └─ db.sql
│  └─ datos_ficticiosh.py
├─ main.py
├─ pyproject.toml
├─ README.md
├─ src
│  ├─ attendance
│  │  └─ __init__.py
│  └─ __init__.py
├─ templates
│  └─ login.html
├─ usuario
│  ├─ registro.py
│  └─ __init__.py
└─ uv.lock

```
```
attendance
├─ .python-version
├─ angular
│  └─ angular-app
│     └─ frontend
│        ├─ .editorconfig
│        ├─ .prettierrc
│        ├─ angular.json
│        ├─ package-lock.json
│        ├─ package.json
│        ├─ public
│        │  └─ favicon.ico
│        ├─ README.md
│        ├─ src
│        │  ├─ app
│        │  │  ├─ app.config.ts
│        │  │  ├─ app.html
│        │  │  ├─ app.routes.ts
│        │  │  ├─ app.scss
│        │  │  ├─ app.spec.ts
│        │  │  └─ app.ts
│        │  ├─ index.html
│        │  ├─ main.ts
│        │  └─ styles.scss
│        ├─ tsconfig.app.json
│        ├─ tsconfig.json
│        └─ tsconfig.spec.json
├─ angular-app
├─ data
│  ├─ database
│  │  └─ db.sql
│  └─ datos_ficticiosh.py
├─ main.py
├─ pyproject.toml
├─ README.md
├─ src
│  ├─ attendance
│  │  └─ __init__.py
│  └─ __init__.py
├─ templates
│  └─ login.html
├─ usuario
│  ├─ registro.py
│  └─ __init__.py
└─ uv.lock

```