import threading 
import time 
from queue import Queue 

def thread_job(l, q): 
    for i in range(len(l)):
        l[i] = l[i] ** 2 
    q.put(l)
    
def mutithreading(data): 
    q = Queue() 
    threads = []
    
    for i in range(4): 
        t = threading.Thread(target=thread_job, args=(data[i], q))
        t.start() 
        threads.append(t)

    for t in threads: 
        t.join()

    results = [] 
    for _ in range(4): 
        results.append(q.get())

    print(results)

data = [[1,2,3], [4,5,6], [7,7,7], [8,9,9]]
mutithreading(data) 