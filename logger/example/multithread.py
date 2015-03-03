import threading
import time
import random
from logger.logger import Logger

def worker(name):
    myLog = Logger(caller=name)
    for i in range(10):
        myLog.info('Hey I am '+ name)
        time.sleep(random.randint(1, 5)) # Integer from 1 to 5, endpoints included
    return

logConfig = Logger(path='/tmp/multithread.log')
threads = list()

for i in range(3):
    t = threading.Thread(target=worker,args=('Thread'+str(i),))
    threads.append(t)
    t.start()