class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None): # задаём начальный элемент
        self.head = head

    def empty(self): # проверяем связный список на пустоту
        if self.head:
            return False
        return True

    def printList(self):# печатаем связный список
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next
        print()

    def push(self, data): # добавляем элемент в начало
        node = Node(data, next=self.head)
        self.head = node

    def append(self, data): # добвляем элемент в конец
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def size(self):
        node = self.head
        d = 0
        while node:
            d += 1
            node = node.next
        return d

    def delete(self, value):
        node = self.head
        if node.data == value:
            self.head = self.head.next
        else:
            while node.next:
                if node.next.data == value:
                    node.next = node.next.next
                else:
                    node = node.next

    def insert(self, index, value):
        node = self.head
        s = 0
        while node:
            if s != index:
                node = node.next 
            else:
                node.next = Node(value, next=node.next)
            s += 1

    def value_n_from_end(self, n):
        length = LinkedList.size(self)
        node = self.head
        s = 0
        while node:
            if s == (length - n):
                print(node.data)
            s += 1
            node = node.next
        

n3 = Node(3)
n2 = Node(2, next=n3)
n1 = Node(1, next=n2)


l = LinkedList(head=n1)
for i in [1,2,3,4,5,4,5,6,6,6,6,1,1,54,3]:
    l.append(i)

l.printList()
print('Length =', l.size())
l.delete(6)
print('Length =', l.size())
l.insert(0, 56)
print('Length =', l.size())
l.printList()
l.value_n_from_end(10)
