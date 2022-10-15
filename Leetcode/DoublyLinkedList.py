class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.prev = None
        self.data = data

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print("Data : ",temp.data)
            temp = temp.next

    def add_front(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = Node(data)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        tail = Node(data)
        temp.next = tail
        tail.prev = temp

    def peek_left(self):
        if self.head is None:
            return None
        return self.head.data

    def peek_right(self):
        if self.head is None:
            return None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.data

    def pop_left(self):
        if self.head is None:
            print("List is Empty!")
            return None
        data = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return data

    def pop_right(self):
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        data = temp.next.data
        temp.next = None
        return data

def doubly_linked_list(data = []):
    linked_list = LinkedList()
    for nums in data:
        linked_list.add_last(nums)
    return linked_list

doubly_linked_list([1,3,2,4,5,8,7,6,9])