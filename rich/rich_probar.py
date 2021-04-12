import time
from rich.progress import track

def do_step(step): 
    time.sleep(0.01)

for step in track(range(100)):
    do_step(step)