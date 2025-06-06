class Queue :
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) # Add item to the end of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) #remove element from the front of the queue
        else:
            return "Queue is empty"
    def is_empty(self):
        return len(self.queue) == 0
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
    def display(self):
        print(self.queue)
    