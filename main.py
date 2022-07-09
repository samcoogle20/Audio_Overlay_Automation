from pydub import *
import os
from Definitions import *

sound_directory = 'Sound_Options'
voice_directory = 'Voice'


for voice_file in os.listdir(voice_directory):
    new_dir = voice_file[:-4]
    try:
        os.mkdir(new_dir)
    except:
        print(f"Directory for {new_dir} already exists")
        continue
    voice = AudioSegment.from_mp3(f"Voice/{voice_file}")
    for sound_file in os.listdir(sound_directory):
        path = os.path.join(sound_directory, sound_file)
        song = AudioSegment.from_wav(path)
        sound_str = sound_file[:-4]
        final = voice.overlay(song, gain_during_overlay=volume_level[sound_file[:-4]])
        final.export(f"./{new_dir}/{new_dir} {sound_str}.mp3", format="mp3")
