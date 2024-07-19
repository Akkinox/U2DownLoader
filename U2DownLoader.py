import yt_dlp
import moviepy.editor as mp
import subprocess
import os
import json

def load_config():
    """Carga la configuración desde el archivo config.json."""
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

def download_audio(url, audio_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': audio_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video(url, video_path):
    ydl_opts_video = {
        'format': 'bestvideo',
        'outtmpl': video_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl_video:
        ydl_video.download([url])

def merge_audio_video(video_path, audio_path, output_path):
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)
    
    # Ajustar la duración del video al de la pista de audio si es necesario
    video = video.set_audio(audio)
    
    # Escribir el archivo final
    video.write_videofile(output_path, codec='libx264', audio_codec='aac', audio_bitrate='192k')

def convert_to_mp3(video_path, mp3_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-q:a', '0',
        '-map', 'a',
        mp3_path
    ]
    subprocess.run(command, check=True)

def get_video_info(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', 'Video')

def main():
    config = load_config()  # Cargar la configuración

    url = input("Introduce la URL del video de YouTube: ")
    option = input("Elige una opción (1: Descargar video y audio, 2: Descargar MP3): ")

    # Obtener el nombre del video
    video_title = get_video_info(url)
    # Limpiar el título para usarlo en nombres de archivos
    video_title = "".join([c if c.isalnum() else "_" for c in video_title])  # Reemplazar caracteres no válidos por "_"
    
    # Usar las rutas definidas en el archivo de configuración
    video_base_path = config['video_base_path']
    audio_base_path = config['audio_base_path']
    
    if option == '1':
        # Descargar video y audio por separado
        video_filename = f'{video_title}.mp4'
        video_path = os.path.join(video_base_path, video_filename)
        audio_filename = f'{video_title}.webm'
        audio_path = os.path.join(audio_base_path, audio_filename)
        output_filename = f'{video_title}_final.mp4'
        output_path = os.path.join(video_base_path, output_filename)
        
        print(f"Descargando video a {video_path}...")
        print(f"Descargando audio a {audio_path}...")
        download_video(url, video_path)
        download_audio(url, audio_path)
        
        print(f"Fusionando video y audio en {output_path}...")
        merge_audio_video(video_path, audio_path, output_path)
        
        # Limpiar archivos temporales
        os.remove(video_path)
        os.remove(audio_path)
        
        print(f"¡Video descargado y fusionado! Encuentra el archivo en {output_path}.")
    
    elif option == '2':
        # Descargar solo audio y convertir a MP3
        audio_filename = f'{video_title}.webm'
        audio_path = os.path.join(audio_base_path, audio_filename)
        mp3_filename = f'{video_title}.mp3'
        mp3_path = os.path.join(audio_base_path, mp3_filename)
        
        print(f"Descargando audio a {audio_path}...")
        download_audio(url, audio_path)
        
        print(f"Convirtiendo audio a MP3 y guardando en {mp3_path}...")
        convert_to_mp3(audio_path, mp3_path)
        
        # Eliminar archivo de audio después de la conversión
        os.remove(audio_path)
        
        print(f"¡MP3 convertido! Encuentra el archivo en {mp3_path}.")
    
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
