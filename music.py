import os
import shutil
from posixpath import split

sourceDirectory = r'/Users/nwatts/Desktop/Homestuck WAV'
destinationDirectory = r'/Users/nwatts/Desktop/Plex Ready'
for entry in os.scandir(sourceDirectory):
    # if (entry.path.endswith("
    # .jpg") or entry.path.endswith(".png")) and entry.is_file():
    # print(entry.name.split(' - '))
    artist = entry.name.split(' - ')[0]
    album = entry.name.split(' - ')[1]
    artistPath = destinationDirectory + '/' + artist
    albumPath = artistPath + '/' + album
    artistFolderExists = os.path.exists(artistPath)
    if not artistFolderExists:
        os.makedirs(artistPath)

    albumFolderExists = os.path.exists(albumPath)
    if not albumFolderExists:
        os.makedirs(albumPath)

    for file in os.scandir(entry.path):
        if file.path.endswith(".wav"):
            splitFileName = file.name.split(" - ")

            songName = file.name.split(" - ")[2]
            if len(splitFileName) != 3:
                songName = file.name.split(" - ")[2] + " - " + file.name.split(" - ")[3]

            songName = songName.replace(" ", " - ", 1)

            print(songName)

            destination = albumPath + "/" + songName

            shutil.copyfile(file.path, destination)
