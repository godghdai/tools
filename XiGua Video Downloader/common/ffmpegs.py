import subprocess
import os


class FFmpegFileNotExistException(Exception):
    def __init__(self, *args):
        self.args = args


class FFmpeg:
    def __init__(self, ffmpeg_path):
        if not os.path.exists(ffmpeg_path):
            raise FFmpegFileNotExistException("未找到ffmpeg.exe文件!!")

        self.ffmpeg_path=ffmpeg_path

    def merge(self, video_path, audio_path, output_path):
        cmd = [self.ffmpeg_path, "-i", video_path, "-i", audio_path, "-c:v", "copy", "-c:a", "copy", output_path]
        subprocess.call(cmd, stdout=subprocess.PIPE)
        os.remove(video_path)
        os.remove(audio_path)
