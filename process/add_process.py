import multiprocessing as mp 

def job(a, b): 
    print('aaaa')

def add_process():
    p = mp.Process(target=job, args=(1, 2))
    p.start()
    p.join()

add_process()