class Queue:
    # Initializer
    def __init__(self):
        self.queue = []

    def Enqueue(self, value):
        self.queue.append(value)
    
    def Dequeue(self):
        self.queue.pop(0)

    def ShowQueue(self):
        print(self.queue)

def main():
    myqueue = Queue()
    myqueue.Enqueue(10)
    myqueue.Enqueue(1)
    myqueue.Enqueue(6)
    myqueue.ShowQueue()
    myqueue.Dequeue()
    myqueue.ShowQueue()
    myqueue.Dequeue()
    myqueue.ShowQueue()
    

if __name__ == "__main__":
    main()
