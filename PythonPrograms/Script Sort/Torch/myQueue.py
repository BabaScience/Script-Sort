

class Queue:
    def __init__(self):
        self.elements_in_queue = []

    def enqueue(self, element):
        self.elements_in_queue.append(element)

    def dequeue(self):
        if self.elements_in_queue:
            v = self.elements_in_queue.pop()
        return v
    def is_empty(self):
        if self.elements_in_queue:
            return False 
        return True

    def is_in(self, element):
        if element in self.elements_in_queue:
            return True 
        return False


