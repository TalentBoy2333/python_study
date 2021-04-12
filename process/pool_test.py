import multiprocessing as mp 

def job(x): 
    return x**2

def multi_core(): 
    pool = mp.Pool(processes=4) # processes=4 设置使用的核数
    res = pool.map(job, range(10))
    print(res)

    res = pool.apply_async(job, (2, ))
    print(res.get())

multi_core()