'''
    freund - Gyuyeon Lim (lky473736)
    recognize (whisper.cpp)
'''

import pkgutil
import re
from pathlib import Path

# patch whisper on file not find error
# https://github.com/carloscdias/whisper-cpp-python/pull/12
try :
    from whisper_cpp_python import Whisper
    
except FileNotFoundError :
    regex = r"(\"darwin\":\n\s*lib_ext = \")\.so(\")"
    subst = "\\1.dylib\\2"

    print("fixing and re-importing whisper_cpp_python...")
    # load whisper_cpp_python and substitute .so with .dylib for darwin
    package = pkgutil.get_loader("whisper_cpp_python")
    whisper_path = Path(package.path)
    whisper_cpp_py = whisper_path.parent.joinpath("whisper_cpp.py")
    content = whisper_cpp_py.read_text()
    result = re.sub(regex, subst, content, 0, re.MULTILINE)
    whisper_cpp_py.write_text(result)

    from whisper_cpp_python import Whisper


def recognize() :
    whisper = Whisper(model_path="./ggml-medium.bin")
    result = whisper.transcribe(open("data/user_audio/output.wav"))
    return result["text"]