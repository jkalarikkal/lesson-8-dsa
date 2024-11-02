class Queue():

    def __init__ (self):
        self.queue = []

    def enqueue (self, h):
        self.queue.append(h)

    def dequeue (self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        print(len(self.queue))


q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(334)
q.enqueue(74)
q.enqueue(29)
q.enqueue(84)

q.display()
q.size()



q.dequeue()
q.dequeue()
q.dequeue()


q.display()
q.size()

