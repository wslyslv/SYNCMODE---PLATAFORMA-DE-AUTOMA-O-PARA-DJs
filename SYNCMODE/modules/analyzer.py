import librosa
import os


def analyze_track(filepath):
    """Analisa uma faixa de áudio e retorna um dict com 'bpm', 'key' e 'duration'.

    Retorna um dicionário com valores numéricos (ou None em caso de falha).
    """
    try:
        # Carrega o áudio (usa sr=None para manter sample rate original)
        y, sr = librosa.load(filepath, sr=None)

        # Duração (em segundos)
        duration = float(librosa.get_duration(y=y, sr=sr))

        # Detecta BPM
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        tempo = float(tempo)

        # Detecta tonalidade (chave musical) usando chroma
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_idx = int(chroma.mean(axis=1).argmax())
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        key = notes[key_idx]

        return {
            'bpm': int(round(tempo)) if tempo and tempo > 0 else None,
            'key': key,
            'duration': round(duration, 2) if duration and duration > 0 else None
        }

    except Exception as e:
        # Log simples e retorno consistente
        try:
            name = os.path.basename(filepath)
        except Exception:
            name = str(filepath)
        print(f"Erro ao analisar {name}: {e}")
        return {
            'bpm': None,
            'key': None,
            'duration': None
        }