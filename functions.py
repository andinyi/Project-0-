from rich.console import Console

console = Console()

def getInput():
    user = input()
    user = user.lower()
    return user

def printProgressBar(progress, total):
    if(progress > total):
        return 
    percent = 100*(progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print('\033[93m' + f"\r|{bar}| {percent:.2f}%" + '\033[0m', end="\r")
    if(progress == total):
        print('\033[92m' + f"\r|{bar}| {percent:.2f}%" + '\033[0m')
    


    

    
    
        
                    