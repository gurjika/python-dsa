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
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            popped = self.pop_first()            
            return popped
        
        if index == self.length - 1:
            popped = self.pop()
            return popped
        
        previous_node = self.get(index - 1)
        next_node = previous_node.next
        previous_node.next = next_node.next
        next_node.next = None
        self.length -= 1
        return next_node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        previous = None
        current = temp
        next = temp.next

        while current is not None:
            current.next = previous
            previous = current
            current = next
            if next:
                next = next.next

        return True
    
    def middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head


        while fast_pointer != self.tail and fast_pointer is not None:

            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer 
    
    def has_loop(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer != self.tail and fast_pointer is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer == fast_pointer:
                return True
            
        return False
    
    def partition_list(self, x):

        if self.length == 0:
            return False

        current = self.head.next
        to_find_node_for_less = self.head
        to_find_node_for_more = self.head
        prev_head = self.head
        new_head = None

        first_more = None

        while current != None:
            if current.value >= x:
                temp = current
                current = current.next
                to_find_node_for_more.next = temp
                to_find_node_for_more = temp

                if not first_more:
                    first_more = to_find_node_for_more



            elif current.value < x:
                
                temp = current
                current = current.next
                to_find_node_for_less.next = temp
                to_find_node_for_less = temp

                if not new_head:
                    new_head = temp


        if prev_head.value < x:
            self.head = prev_head

        else:
            to_find_node_for_less.next = prev_head
            prev_head.next = first_more
            self.head = new_head

      
        to_find_node_for_more.next = None
        self.tail = to_find_node_for_more

        return True
        

def find_kth_from_end(linked_list: LinkedList, k):


    if k < 0:
        return None
    
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head


    for _ in range(1, k):
        if fast_pointer is None:
            return None
        fast_pointer = fast_pointer.next
    
    while fast_pointer != linked_list.tail:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next

    return slow_pointer

linked_list = LinkedList(3)
linked_list.append(2)
linked_list.append(1)

# linked_list.append(10)
# linked_list.append(7)
# linked_list.append(8)
# linked_list.append(9)
# linked_list.append(10)
# linked_list.append(11)


print()
print()




# print(linked_list.middle_node().value)
# linked_list.pop_first()
# print()
# linked_list.reverse()
# linked_list.print_list()



print(f'tail: {linked_list.tail.value}')
print(f'head: {linked_list.head.value}')
# print(linked_list.get(0))


def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0

    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)

    print("Before:", linkedlist_to_list(ll.head))

    ll.partition_list(x)

    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
      