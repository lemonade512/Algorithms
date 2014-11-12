from binary_heap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()
    heap.insert(5)
    heap.insert(7)
    heap.insert(3)
    heap.insert(2)
    heap.insert(9)
    heap.insert(21)

    print "\nPopped:", heap.pop()
    print heap
    print "\nPopped:", heap.pop()
    print heap
    print "\nPopped:", heap.pop()
    print heap
