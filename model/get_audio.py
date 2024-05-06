'''
    freund - Gyuyeon Lim (lky473736)
    get_audio 
'''

import os
import pyaudio
import wave

def check_device() :
    audio = pyaudio.PyAudio()

    for index in range(audio.get_device_count()) :
        desc = audio.get_device_info_by_index(index)
        
        print ("DEVICE: {device}, INDEX: {index}, RATE: {rate} ".format(device=desc["name"], index=index, rate=int(desc["defaultSampleRate"])))

def record(chunk, format, channels, rate, record_seconds, output_folder, output_file) :
    # current directory
    current_dir = os.getcwd()

    # i'll store the voice instructions by user at this
    output_path = os.path.join(current_dir, output_folder)

    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)

    # whold path that output
    output_file_path = os.path.join(output_path, output_file)

    p = pyaudio.PyAudio()

    # open audio stream
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print ("RECORD START")

    frames = []

    # recored start
    for i in range(0, int(rate / chunk * record_seconds)) :
        data = stream.read(chunk)
        frames.append(data)

    print ("RECORD END")

    # stream down
    stream.stop_stream()
    stream.close()
    p.terminate()

    # write the wav file
    wf = wave.open(output_file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"The file was stored at {output_file_path}.")
