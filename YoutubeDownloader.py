# Program to download youtube videos
# Sarveshwar Shukla (19 March 2022)
# needs modifications (not very effective)

from pytube import YouTube

link = "https://www.youtube.com/watch?v=tdY_xa5OMr8"
youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videoResolution = youtube_1.streams.all()
videoResolutionList = list(enumerate(videoResolution))
for i in videoResolutionList:
    print(i)
    
videoToDownload = int(input("Enter : "))
    
videoResolution[videoToDownload].download()
print("Successful")
