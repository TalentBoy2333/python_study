import time
from rich.progress import Progress

def do_step(step): 
    time.sleep(0.1)
    
def multi_proc(): 
    for step in range(100):
        do_step(step)

with Progress(['a', multi_proc]) as progress:

    task1 = progress.add_task("[red]Downloading...", )
    task2 = progress.add_task("[green]Processing...", )
    task3 = progress.add_task("[cyan]Cooking...", )

    while not progress.finished:
        progress.update()
        progress.update()
        progress.update()
        time.sleep(0.02)
