class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class boo:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert(self, index: int, value):
        new_node = Node(value)
        if index < 0 or index > self.size:
            raise IndexError()
        if self.size == 0:
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        self.size += 1
    def get(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError()
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    def delete(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError()
        if index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
    def __len__(self):
        return self.size
# используем вводя пример внизу
if __name__ == "__main__":
    my_list = boo()
    my_list.insert(0, 10)
    my_list.insert(1, 20)
    my_list.insert(1, 15)
    print("значение ", my_list.get(1))
    print("длина списка", len(my_list))
    my_list.delete(1)
    print("значение после удаления", my_list.get(1))
    print("длинна после удаления", len(my_list))