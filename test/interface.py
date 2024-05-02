import gradio as gr 
import time
import translate as tr
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

gr.Interface(
    title = 'test Whisper model (lky473736)', 
    fn = tr.transcribe, 
    inputs=[
        gr.inputs.Audio(source="microphone", type="filepath")
    ],
    outputs=[
        "textbox"
    ],
    live=True,
    ssl_verify=False).launch()