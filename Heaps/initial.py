class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    

    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current != 0 and self.heap[current] > self._parent(current):
            new_index = self._parent(current)
            self._swap(current, new_index)
            current = new_index
            

            
