import argparse
import os
from pytube import YouTube
from progress.bar import Bar

parser = argparse.ArgumentParser()
parser.add_argument("link", help="enter link to video")
args = parser.parse_args()

def progress_bar(stream ,chunk, remaining):
    downloaded = stream.filesize - remaining
    downloaded = (downloaded / stream.filesize) * 100
    downloaded = int(downloaded)

    bar.goto(downloaded)

yt = YouTube(args.link, on_progress_callback=progress_bar)

yt = yt.streams\
    .filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()

print(f"\n\t{yt.title}")
print(f"\n\tResolution: {yt.resolution}")
size = round(yt.filesize / 1024 / 1024, 1)
print(f"\n\tSize: {size} MB\n")

bar = Bar("\tDownloading:", max=100, suffix='%(percent)d%%')

try:
    yt.download()
    bar.finish()
    print("\n\tDownloaded successfully!\n")
except Exception as e:
    bar.finish()
    print("\n\tError: " + str(e))
    os.remove(yt.filename + '.mp4')
