"""
Создайте два класса:
- AudioFileMixin — требует наличие поля audio_tracks (список треков).
Метод play_audio() выводит:

Воспроизведение аудио для <НазваниеКласса>:
<название трека>
<название трека>

- VideoFileMixin — требует наличие поля video_files (список видео).
Метод play_video() выводит:

Воспроизведение видео для <НазваниеКласса>:
<название видео>
<название видео>

Если нужное поле отсутствует — выбрасывайте AttributeError.
"""

class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(track)


class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(video)

"""
Создайте два класса:
- MediaPlayer — поддерживает только аудио. Принимает список треков.
- Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.

Данные:

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

Пример вывода:
Воспроизведение аудио для MediaPlayer:
track1.mp3
track2.mp3

Воспроизведение аудио для Laptop:
track1.mp3
track2.mp3

Воспроизведение видео для Laptop:
movie.mp4
trailer.mov
"""

class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

mp = MediaPlayer(tracks)
mp.play_audio()
print()

laptop = Laptop(tracks, movies)
laptop.play_audio()
laptop.play_video()
