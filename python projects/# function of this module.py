# function of this module 
# recieve rates from the producer client then set it as the base currency   
import queue
import threading

# Shared queue between producer and consumer
document_queue = queue.Queue()

# Producer function (uploads a document)
def producer(document):
    document_queue.put(document)

# Consumer function (receives and processes the document)
def consumer():
    while True:
        document = document_queue.get()
        if document is None:
            break  # Exit the loop when no more documents are produced
        print(f"Received document: {document}")
        # Add your processing logic here
        document_queue.task_done()

# Create and start the producer and consumer threads
producer_thread = threading.Thread(target=producer, args=("example_document.pdf",))
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()

print("All tasks are done.")
