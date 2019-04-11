'''  Function: convert audio to spectogram images
'''
import os
from shutil import copyfile


for dirpath, dirnames, filenames in os.walk("./output/"):
    for filename in [f for f in filenames if f.endswith(".wav")]:
        print(os.path.join(dirpath, filename))
        file_list = filename.split("-")
        emotional_class = int(file_list[2])
        copyfile(os.path.join(dirpath, filename), './audio-class-partition/' + str(emotional_class) + '/' + filename)
        print('Copied', filename)
