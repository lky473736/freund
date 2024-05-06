'''
    freund - Gyuyeon Lim (lky473736)
    interface (main) 
'''


import pyaudio
import model.get_audio as get
import model.recognize as rec

chunk = 1024  # the frame that read one time
format = pyaudio.paInt16  # audio format
channels = 1  # channel : single
rate = 44100  # velocity of sampling
record_seconds = 5  # 5~10
output_folder = "data/user_audio" 
output_file = "output.wav"  

get.check_device()
get.record(chunk, format, channels, rate, record_seconds, output_folder, output_file)

rec.recognize()