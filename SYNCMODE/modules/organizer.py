import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen import File
from modules.analyzer import analyze_track


def scan_music_folder(source_folder, target_folder=None): # lê os metadados das musicas (gênero, artista) e organiza em pastas.
    logs = []

    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
        return logs

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".mp3", ".wav")):
            file_path = os.path.join(source_folder, filename)
            try:
                audio = File(file_path)
                if audio and audio.tags:
                    title = audio.tags.get('title', ['Sem titulo'])[0]
                    artist = audio.tags.get('artist', ['Desconhecido'])[0]
                else:
                    # Fallback se não houver tags
                    title = os.path.splitext(filename)[0]
                    artist = 'Desconhecido'

                # Análise técnica da faixa (analyze_track retorna dict)
                analysis = analyze_track(file_path) or {}

                # Adiciona a lista com valores consistentes
                logs.append({
                    'title': title,
                    'artist': artist,
                    'file': filename,
                    'bpm': analysis.get('bpm'),
                    'key': analysis.get('key'),
                    'duration': analysis.get('duration')
                })

            except Exception as e:
                print(f"Erro ao ler {filename}: {e}")
                logs.append({
                    'title': os.path.splitext(filename)[0],
                    'artist': 'Desconhecido',
                    'file': filename
                })
    return logs