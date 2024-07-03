class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.tail is not None:
            last_item = self.tail
            last_item.next = new_node
            self.tail = new_node
        
        else:
            self.tail = new_node
            self.head = new_node

        self.length += 1
        return True

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        
        temp = self.head

        if self.head is None:
            return None
        
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp

        while temp is not None:

            if temp.next == self.tail:
                popped = temp.next
                last_node = temp
                self.tail = last_node
                last_node.next = None
                self.length -= 1
                return popped.value
            
            temp = temp.next
            

linked_list = LinkedList(4)
linked_list.pop()

linked_list.print_list()
print()
print(f'popped item {linked_list.pop()}')

print()
linked_list.print_list()
print()

print(f'tail: {linked_list.tail}')
print(f'head: {linked_list.head}')