class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_first(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != self.head and temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
            temp.next.next = self.head
            self.head = temp.next

    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != self.head and temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
            temp.next.next = self.head

    def pop_last(self):
        response = None
        temp = self.head

        if temp is None:
            return "Queue Empty"
        
        if temp.next is None or temp.next == temp:
            response = temp.data
            self.head = None
            return response

        while temp.next.next != self.head:
            temp = temp.next

        next_temp = temp.next.next
        response = temp.next.data
        temp.next.next = None
        temp.next = next_temp

        return response

    def pop_first(self):
        response = None
        temp = self.head

        if temp is None:
            return "Queue Empty"
        
        if temp.next is None or temp.next == temp:
            response = temp.data
            self.head = None
            return response

        while temp.next != self.head:
            temp = temp.next
        
        self.head = self.head.next

        next_temp = temp.next.next
        response = temp.next.data
        temp.next.next = None
        temp.next = next_temp

        return response

    def peek(self):
        temp = self.head
        while temp.next != self.head and temp.next is not None:
            temp = temp.next
        print(temp.data)

    def print(self):
        temp = self.head
        response_list = []

        if temp is None:
            print("Queue Empty")
            return
        while temp.next != self.head and temp.next is not None:
            response_list.append(temp.data)
            temp = temp.next
        response_list.append(temp.data)
        print(response_list)
    

obj = CircularLinkedList()
obj.add_first(1)
obj.add_first(2)
obj.add_first(3)
obj.add_first(4)
obj.add_first(5)
obj.add_first(6)
obj.add_first(7)
obj.add_first(8)
obj.print()
obj.peek()