import multiprocessing as mp 
import time 

def job(v, num, lock):
    lock.acquire()
    for _ in range(10): 
        time.sleep(0.1)
        v.value += num
        print(v.value)
    lock.release()

def multi_core(): 
    v = mp.Value('d', 1) # 多进程，共享内存
    # array = mp.Array('d', [1,2,3])

    lock = mp.Lock()

    p1 = mp.Process(target=job, args=(v, 1, lock))
    p2 = mp.Process(target=job, args=(v, 3, lock))
    p1.start() 
    p2.start() 
    p1.join() 
    p2.join()
 

multi_core()