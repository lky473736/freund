import struct
import numpy as np

# load the file of bin as ggml 
def load_ggml_model(bin_file_path) :
    with open(bin_file_path, 'rb') as f :
        data = f.read()

    return data

# convert bin to gguf
def save_as_gguf(model_data, output_file_path):
    with open(output_file_path, 'wb') as f:
        f.write(model_data)

bin_file_path = '/Users/alphastation/repository/freund/model/LLM/koalpaca/KoAlpaca-Polyglot-12.8b-ggml-model-q5_0.bin'
output_file_path = '/Users/alphastation/repository/freund/model/LLM/koalpaca/KoAlpaca-convert-to-gguf.gguf'

# load and convert
model_data = load_ggml_model(bin_file_path)
save_as_gguf(model_data, output_file_path)
