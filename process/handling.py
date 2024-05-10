from rich.console import Console
from rich.panel import Panel

'''
- 0 : undefined input value
- 1 : undefined error
- 2 : system error of recording voice
- 3 : device error
- 4 : GPT error
'''

console = Console()

def handling_error(errnum) :
    print ()
    console.print ("============", justify="center")
    match (errnum) :
        case 0 :
            console.print ("ERROR 00. undefined input value.", justify="center")
            console.print ("Please try again to input the key.", justify="center")
            
        case 1 : 
            console.print ("ERROR 01. undefined error.", justify="center")
            console.print ("Please refresh this program and run again.", justify="center")
            
        case 2 : 
            console.print ("ERROR 02. system error of recording voice.", justify="center")
            console.print ("Please try again to record", justify="center")
            
        case 3 : 
            console.print ("ERROR 03. device error.", justify="center")
            console.print ("Please refresh this program and re-check your record device", justify="center")
            
        case 4 : 
            console.print ("ERROR 04. GPT error.", justify="center")
            
    console.print ("============", justify="center")
    print ()