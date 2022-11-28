import os

from yt_dlp import YoutubeDL


ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
}
ydl = YoutubeDL(ydl_opts)

def download(url: str) -> str:
    info = ydl.extract_info(url, False)

    xyz = os.path.join("downloads", f"{info['id']}.{info['ext']}")
    if os.path.exists(xyz):
        return xyz
    ydl.download([url])
    return xyz


# The lines below were used for testing
"""
ydl_optssx = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}
yodl = YoutubeDL(ydl_optssx)

def audio_dl(url: str) -> str:
    sin = yodl.extract_info(url, False)

    x_file = os.path.join("downloads", f"{sin['id']}.mp3")
    if os.path.exists(x_file):
        return x_file
    yodl.download([url])
    return x_file
"""
