class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):

        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            

            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        if self.root == None:
            return False
        
        temp = self.root
                
        while temp is not None:

            if temp.value == value:
                return True
            

            if temp.value < value:
                temp = temp.right
            
            else:
                temp = temp.left


        return False
    

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True
        
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

bst = BinarySearchTree()

bst.insert(40)
bst.insert(24)
bst.insert(23)
bst.insert(5)
bst.insert(3)
bst.insert(6)


print(bst.contains(4))

print(bst.r_contains(6))