class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def add(self, root, data):
        if root is None:
            return Node(data)
        
        if root.data == data:
            print("Cannot be added as element already exists in the tree")
            return root
        
        elif root.data < data:
            root.right = self.add(root.right, data)
        
        else:
            root.left = self.add(root.left, data)

        return root
    
    def insert(self, data):
        self.root = self.add(self.root, data)


    def search(self, root, element):
        if root is None:
            print("Element not found")
            return
        if root.data == element:
            print("Element found")
            return
        elif root.data > element:
            self.search(root.left, element)
        else:
            self.search(root.right, element)

    def delete(self, element):
        pass

    def pre_order(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=" ")
        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data, end=" ")
    
    def level_order(self, root):
        if root is None:
            return
        lst = []
        lst.append(root)
        while lst:
            temp = lst.pop(0)
            if temp.left:
                lst.append(temp.left)
            if temp.right:
                lst.append(temp.right)
            print(temp.data, end=" ")


obj = BST()
for ele in (6,4,7,2,8,1,9,5,3):
    obj.insert(ele)

obj.search(obj.root, 8)
obj.search(obj.root, 11)