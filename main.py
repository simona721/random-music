import random, os


music_dir = "/home/user/Music"
songs = os.listdir(music_dir)


song = random.randint(0, len(songs))

print(songs[song])


#This plays the songs
os.system(os.path.join(music_dir, songs[0]))