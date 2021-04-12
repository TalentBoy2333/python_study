import threading 
import time

def t1_job(): 
    print('t1 start.')
    time.sleep(1)
    print('t1 finish. ')

def t2_job(): 
    print('t2 start.')
    time.sleep(1)
    print('t2 finish. ')

def main():
    t1 = threading.Thread(target=t1_job, name='T1')
    t2 = threading.Thread(target=t2_job, name='T2')
    t1.start()
    t2.start() 
    t1.join()
    t2.join()
    print('all done')

main()