class Node:
    def __init__(self, data) -> None:
        self.next = None
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
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

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

def singly_linked_list(data = []):
    linked_list = LinkedList()
    for nums in data:
        linked_list.add_last(nums)
    return linked_list

singly_linked_list([1,3,2,4,5,8,7,6,9])