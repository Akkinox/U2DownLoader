# U2DownLoader

Este proyecto te permite descargar videos y audios de YouTube, fusionar video y audio, o convertir solo el audio a MP3. A continuación se presentan las instrucciones para instalar y utilizar el script.

## Requisitos

- Python 3.6 o superior
- FFmpeg
- `yt-dlp` (una alternativa a `youtube-dl`)
- `moviepy` (para manipulación de video)

### Instalación

# 1. Instalar las Dependencias

instala las dependencias necesarias usando pip:

```bash
pip install yt-dlp moviepy
``` 

# 2. Instalar FFmpeg


### En Windows

- Descarga el ejecutable de FFmpeg desde [Descargar FFmpeg](https://ffmpeg.org/download.html)
- Extrae el contenido del archivo ZIP descargado.
- Agrega el directorio bin de FFmpeg a la variable de entorno PATH.

### En MacOS

```bash
brew install ffmpeg
``` 

### En Linux

```bash
sudo apt-get install ffmpeg
``` 

# 3. Configurar el Archivo de Configuración
Crea un archivo de configuración llamado config.json en la misma carpeta que el script y define las rutas de destino para los archivos. El archivo debe tener el siguiente formato:

```bash
{
    "video_base_path": "C:/Mis Videos/Videos/",
    "audio_base_path": "C:/Mis Videos/MP3/"
}
``` 

Asegúrate de reemplazar las rutas con las ubicaciones deseadas en tu sistema.

# 4. Ejecución

Para la ejecución en el directorio donde clonaste el proyecto con cmd debes lanzar el siguiente comando:

```bash
python U2DownLoader.py
``` 

Donde U2DownLoader.py es el nombre del archivo Python que contiene el código.

### Opciones

1. Descargar video y audio: Elige la opción 1 para descargar tanto el video como el audio, fusionarlos y guardar el archivo final en la carpeta de videos.

2. Descargar MP3: Elige la opción 2 para descargar solo el audio y convertirlo a MP3, guardándolo en la carpeta de audios.


# Ejemplo de ejecución
```bash
Introduce la URL del video de YouTube: https://www.youtube.com/watch?v=oD5f55ohsc4
Elige una opción (1: Descargar video y audio, 2: Descargar MP3): 1
``` 

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE). Consulta el archivo `LICENSE` para más detalles.