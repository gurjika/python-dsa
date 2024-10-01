class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1


    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp.value

stack = Stack(5)
stack.push(2)
stack.push(3)
stack.print_stack()
print(stack.pop(), '\n')
stack.print_stack()
print()

class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None 

        else:
            self.first = temp.next
            temp.next = None
        
        self.length -= 1
        return temp.value

    def print_queue(self):

        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next

queue = Queue(3)
queue.enqueue(2)
queue.enqueue(5)
queue.print_queue()
queue.dequeue()
queue.print_queue()