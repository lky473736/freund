'''
    freund - Gyuyeon Lim (lky473736)
    interface (main) 
'''

import pyaudio
from rich.console import Console
from rich.panel import Panel
import time
import os

import model.voice.get_audio as get
import model.recognize.whisper.recognize as rec
import process.handler.handling as hand
import model.controller.llamacpp.llamacpp as llamacpp

# import subprocess
import subprocess
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

chunk = 1024  # the frame that read one time
format = pyaudio.paInt16  # audio format
channels = 1  # channel : single
rate = 44100  # velocity of sampling
record_seconds = 5  # 5~10
output_folder = "data/user_audio" 
output_file = "output.wav"  

console = Console()

print()
console.print ("============", justify="center")
console.print ("Welcome to freund", justify="center")
console.print ("Ver. proto1 (2024. 05. 10. Updated)", justify="center")
console.print ("============", justify="center")
print ()

console.print ("Wait for checking device...", justify="center")
time.sleep (3)
get.check_device()
print ()
console.print ("============", justify="center")
print ()

console.print ("Open the display that can confirm your instruction and answer...", justify="center")
time.sleep (3)
print ()
console.print ("============", justify="center")
print ()

file_path = "repository/freund/process/printer/printer.py"
applescript = f'''
tell application "Terminal"
    do script "python3 {file_path}"
end tell
'''
subprocess.run(['osascript', '-e', applescript])

while True :
    input_value = input("If you want to continue to put instruction to freund, press 'p'. : ")
    
    if input_value in ['q', 'Q']:
        break
    
    elif input_value in ['p', 'P'] :
        path = get.record(chunk, format, channels, rate, record_seconds, output_folder, output_file)
        dotenv.set_key(dotenv_file, 'TOKEN', 'recorded')
        
    else : 
        hand.handling_error(0)
        dotenv.set_key(dotenv_file, 'TOKEN', 'error')
        continue
    
    if os.path.isfile(path) == True :
        instruction = rec.recognize()
        dotenv.set_key(dotenv_file, 'WORD', instruction)
        dotenv.set_key(dotenv_file, 'TOKEN', 'recognized')
        
        reaction = llamacpp.predict(instruction)
        answer = reaction["choices"][0]['text'][reaction["choices"][0]['text'].index('A')+4: ]
        dotenv.set_key(dotenv_file, 'WORD', answer)
        dotenv.set_key(dotenv_file, 'TOKEN', 'answered')
        
    else : 
        hand.handling_error(2)
        dotenv.set_key(dotenv_file, 'TOKEN', 'error')
        state = 'error'
    
