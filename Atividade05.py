class BinaryTreeHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) > 1:
            self.swap(0, len(self.heap) - 1)
            max_val = self.heap.pop()
            self.heapify_down(0)
        elif len(self.heap) == 1:
            max_val = self.heap.pop()
        else:
            raise IndexError("Heap is empty")
        return max_val

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if (left < len(self.heap) and self.heap[left] > self.heap[largest]):
            largest = left
        if (right < len(self.heap) and self.heap[right] > self.heap[largest]):
            largest = right
        if (largest != index):
            self.swap(index, largest)
            self.heapify_down(largest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
