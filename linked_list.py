class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, element):
        new_node = self.Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, element, index):
        if index < 0 or index > self.length():
            raise IndexError("Index out of bounds")
        new_node = self.Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
        if new_node.next is None:
            self.tail = new_node

    def delete(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        return current.data

    def deleteAll(self, element):
        current = self.head
        while current:
            next_node = current.next
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
            current = next_node

    def get(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def findFirst(self, element):
        index = 0
        current = self.head
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element):
        index = self.length() - 1
        current = self.tail
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self):
        self.head = None
        self.tail = None

    def extend(self, elements):
        current = elements.head
        while current:
            self.append(current.data)
            current = current.next