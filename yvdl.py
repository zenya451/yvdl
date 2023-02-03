import argparse
from pytube import YouTube
from progress.bar import Bar

last_persent = 0

parser = argparse.ArgumentParser()
parser.add_argument("link", help="enter link to video")
args = parser.parse_args()

bar = Bar("Downloading:", max=100)

def progress_bar(stream ,chunk, remaining):
    downloaded = stream.filesize - remaining
    downloaded = (downloaded / stream.filesize) * 100
    downloaded = round(downloaded)

    global last_persent

    for i in range(last_persent, downloaded):
        bar.next()

    last_persent = downloaded


yt = YouTube(args.link, on_progress_callback=progress_bar)
yt = yt.streams\
    .filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()

print("\n")

yt.download()

bar.finish()

print("\nDownloaded successfully !\n")
