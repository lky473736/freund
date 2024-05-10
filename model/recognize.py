'''
    freund - Gyuyeon Lim (lky473736)
    recognize
'''

import whisper

def recognize() :
    model = whisper.load_model("base")
    result = model.transcribe("data/user_audio/output.wav")
    return result["text"]