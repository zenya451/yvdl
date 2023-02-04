import argparse
from pytube import YouTube
from progress.bar import Bar

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
        bar.next()

    last_persent = downloaded


yt = YouTube(args.link, on_progress_callback=progress_bar)

yt = yt.streams\
    .filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()

print(f"\n\t{yt.title}")
print(f"\n\tResosution: {yt.resolution}")
size = round(yt.filesize / 1024 / 1024, 1)
print(f"\n\tSize: {size}\n")

bar = Bar("\tDownloading:", max=100)

yt.download()

bar.finish()

print("\n\tDownloaded successfully !\n")
