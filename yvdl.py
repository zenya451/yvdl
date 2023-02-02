import argparse
from pytube import YouTube
from alive_progress import alive_bar
import alive_progress.styles

last_persent = 0

parser = argparse.ArgumentParser()
parser.add_argument("link", help="enter link to video")
args = parser.parse_args()

def progress_bar(stream ,chunk, remaining):
    downloaded = stream.filesize - remaining
    downloaded = (downloaded / stream.filesize) * 100
    downloaded = round(downloaded)

    global last_persent

    for i in range(last_persent, downloaded):
        bar()

    last_persent = downloaded


yt = YouTube(args.link, on_progress_callback=progress_bar)
yt = yt.streams\
    .filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()

print("\n")

with alive_bar(100, title="Downloading:", bar="classic2") as bar:
    yt.download()

print("\nDownloaded successfully !\n")
