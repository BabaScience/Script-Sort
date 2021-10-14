


class Stack:
    def __init__(self):
        self.elements_in_stack = []

    def push(self, element):
        self.elements_in_stack.append(element)

    def pop(self):
        if self.elements_in_stack:
            v = self.elements_in_stack.pop()
        return v

    def is_empty(self):
        if self.elements_in_stack:
            return False 
        return True

    def is_in(self, element):
        if element in self.elements_in_stack:
            return True 
        return False
    def last_on_stack(self):
        return self.elements_in_stack[-1]

    def first_on_stack(self):
        return self.elements_in_stack[0]
    
