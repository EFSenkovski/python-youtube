from pytube import YouTube, Playlist
from moviepy.editor import *

url_playlist = input("Digite a URL da playlist: ")
path_output = input("Digite a pasta de saída: ")

playlist = Playlist(url_playlist)

i = 0
for url in playlist:
    i = i + 1
    msg = "--------------------------------------------------\nBaixando {0} de {1} "
    print(msg.format(i,len(playlist)))

    video = YouTube(url)
    stream = video.streams.filter(only_audio=True)[0]
    mp4_file = stream.download(output_path=path_output)
    
    mp3_file = mp4_file.replace(".mp4",".mp3")

    audioclip = AudioFileClip(mp4_file)
    audioclip.write_audiofile(mp3_file)
    audioclip.close()

    #https://www.youtube.com/watch?v=ZIiQ1jMqhVM&list=PLCwAHfhr-Gc_wCv4yrPBiZFFyaRDMraMl&index=5

    #
    
    
