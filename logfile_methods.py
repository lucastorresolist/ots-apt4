from datetime import datetime

path = 'logfile.txt'

def save_log(method_name: str) -> None:
    now = datetime.now()
    archive = open('logfile.txt', 'a')
    archive.write(f'{str(now)} {method_name} \n')

