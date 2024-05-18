import subprocess as sp

file_name = sub

# AppleScript 코드
applescript = f'''
tell application "Terminal"
    do script "python3 {file_name}"
end tell
'''

# AppleScript를 실행하여 새로운 터미널에서 코드 실행
sp.run(['osascript', '-e', applescript])
