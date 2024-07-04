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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

        

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
    
    def pop_first(self):

        temp = self.head

        if self.head is None:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        self.length -= 1
        self.head = self.head.next
        temp.next = None
        return temp

    def get(self, index):
 
        if self.length <= index or index < 0:
            return None
        
        temp = self.head

        # while temp is not None:
        #     if counter == index:
        #         return temp.value
        #     temp = temp.next
        #     counter += 1

        for _ in range(index):
            temp = temp.next

        return temp
    
    def set(self, index, value):

        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True
        
        if index == self.length:
            return self.append(value)
         
        temp = self.get(index - 1)
        new_node = Node(value)
        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node
        self.length += 1
        return True
    


linked_list = LinkedList(4)
linked_list.append(2)
linked_list.insert(2, 5)

# linked_list.pop_first()
linked_list.print_list()
print()

print()
linked_list.print_list()
print()

print(f'tail: {linked_list.tail.value}')
print(f'head: {linked_list.head.value}')
print(linked_list.get(0))