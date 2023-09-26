buffer = [] #shared buffer
buffer_size = 10

empty = semaphore(buffer_size) #semaphore to track empty slots
full = semaphore(0)
mutex = semaphore(1)


def producer():
    while True:
        item = produce_item()
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        mutex.release()
        full.release()
        consume_item(item)
        
def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        mutex.release()
        empty.release()
        consume_iem(item)
        
        