import os
import time
import sys
import dotenv

counting = 0
dotenv_file = dotenv.find_dotenv()

while True : 
    token = dotenv.dotenv_values(dotenv_file)['TOKEN']
    word = dotenv.dotenv_values(dotenv_file)['WORD']
    # print (token, word)
        
    if token == '0' : 
        pass
    
    else : 
        if token == 'recorded' : 
            print ("recording")
            
        elif token == 'recognized' :
            counting += 1
            instruction = word
            print (f'[Q{counting}]', instruction)
            
        elif token == 'answered' : 
            answer = word
            print (f'[A{counting}]', answer)
            
        else :
            if token == 'error' :
                print ("error occured")
                
        dotenv.set_key(dotenv_file, 'WORD', '0')
        dotenv.set_key(dotenv_file, 'TOKEN', '0')
            
    time.sleep (1)