# Program to download youtube videos
# Sarveshwar Shukla (19 March 2022)
# needs modifications (not very effective)

from pytube import YouTube

link = "https://www.youtube.com/watch?v=ULcOQ2w4sPk"
link_info = YouTube(link)

# print(link_info.title)
# print(link_info.thumbnail_url)

videoResolution = link_info.streams.all()
videoResolutionList = list(enumerate(videoResolution))
for i in videoResolutionList:
    print(i)
    
videoToDownload = int(input("Enter : "))
    
videoResolution[videoToDownload].download()
print("Successful")
