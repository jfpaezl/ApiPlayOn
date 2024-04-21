# API de Películas y Series

Este proyecto es una API que permite a los usuarios explorar, buscar y listar películas y series, similar a la funcionalidad ofrecida por plataformas como Netflix. Los usuarios pueden buscar contenido por título, género, año de lanzamiento, entre otros criterios. Además, la API proporciona detalles detallados de cada película o serie, incluyendo elenco, duración, calificaciones y más.

## Instalación

Sigue estos pasos para instalar y ejecutar este proyecto localmente:

1. Descarga el proyecto.
2. Crea un entorno virtual. Puedes hacerlo con el siguiente comando:

```bash
python -m venv env
```

3. Activa el entorno virtual. En Windows, puedes hacerlo con el siguiente comando:

```bash
.\env\Scripts\activate
```
En Unix o MacOS, usa este comando:

```bash
source env/bin/activate
```
4. Crea un archivo .env copiando las variables de env.example y pegándolas en el .env.
5. Instala las dependencias del proyecto con el siguiente comando:
```bash
pip install -r requirements.txt
```

## Inicialización

Para iniciar la API, asegúrate de que tu entorno virtual esté activo y luego ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en el puerto 8000 de tu máquina local. Puedes acceder a la API en http://localhost:8000.

Si quieres cambiar el puerto, puedes hacerlo con el argumento --port, por ejemplo:

```bash
uvicorn main:app --reload --port 8080
```

ten en cuenta que si cambias el puerto.  en el archivo .env deves cambiar el puerto en API_ROUTE