import threading
import time

def thread_job():
    print('this is an added thread, number is %s' % threading.current_thread())
    for i in range(10):
        time.sleep(0.2)
    print('finishied')

def main():
    added_thread = threading.Thread(target= thread_job)
    added_thread.start()
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    added_thread.join()
    print('all done')
if __name__ == '__main__':
    main()