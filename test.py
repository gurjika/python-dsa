class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        pass

        # current = self.head
        # to_find_node_for_less = None
        # to_find_node_for_more = None
        # first_more = None
        # prev_head = self.head

        # while current != None:
        #     if current.value >= x:
        #         temp = current
        #         current = current.next
        #         if to_find_node_for_more:
        #             to_find_node_for_more.next = temp
        #         to_find_node_for_more = temp

        #         if not first_more:
        #             first_more = to_find_node_for_more


 

        #     elif current.value < x:
        #         temp = current
        #         current = current.next
        #         if to_find_node_for_less:
        #             to_find_node_for_less.next = temp
        #         to_find_node_for_less = temp


        # if self.head >= x:
        #     if first_more:
        #         to_find_node_for_less.next = prev_head
        #         prev_head.next = first_more
        #         self.head = 
        #         return
        #     self.tail = 




#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
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
    



# Run the test function
test_partition_list()
      