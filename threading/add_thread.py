import threading 

def thread_job(): 
    print('This is an added thread, number is {}'.format(threading.current_thread()))

def main():
    # print(threading.active_count()) # 查看激活进程数
    # print(threading.enumerate()) # 查看激活进程
    # print(threading.current_thread()) # 查看正在运行的线程

    added_thread = threading.Thread(target=thread_job, )
    added_thread.start()

main()