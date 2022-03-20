from pytube import Playlist

link = "https://www.youtube.com/playlist?list=PLxCzCOWd7aiFjkQbGj_yHeTEVPn422_z5"
link_info = Playlist(link)

# print(link_info.title)

print(f"Downloading : {link_info.title}")

for video in link_info.videos:
    video.streams.first().download()

print("Successful")