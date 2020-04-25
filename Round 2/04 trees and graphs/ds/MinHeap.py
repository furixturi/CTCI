class MinHeap:
    def __init__(self):
        self.items = []

    # insert to next available slot
    # bubble up until its parent is smaller than it
    # or it reaches the root
    def insert(self, val):
        self.items.append(val)
        i = len(self.items) - 1
        parent = (i + 1) // 2 - 1
        while parent >= 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = (i + 1) // 2 - 1

    # take out the first (the smallest), put the last at its place
    # bubble down the new head until it is smaller than both of its children, 
    # or it becomes a leaf
    def extractMin(self):
        if not self.items:
            return None
        if len(self.items) == 1:
            return self.items.pop()
        result = self.items[0]
        self.items[0] = self.items.pop()
        i = 0
        left = i * 2 + 1
        right = i * 2 + 2
        while left < len(self.items) and (
            self.items[i] > self.items[left] or (
                right < len(self.items) and self.items[i] > self.items[right]
            )
        ):
            smallerChildIdx = right if (right < len(self.items) and
                                        self.items[left] > self.items[right]) else left
            self.items[i], self.items[smallerChildIdx] = self.items[smallerChildIdx], self.items[i]
            i = smallerChildIdx
            left = 2 * i + 1
            right = 2 * i + 2
        return result


if __name__ == '__main__':
    h = MinHeap()
    nums = [3, 99, 20, 45, 0, 17]
    for n in nums:
        h.insert(n)
    print(h.items)
    print(h.extractMin())
    print(h.items)
