class Node:
    def __init__ (self, data):
        self.item = data
        self.ref  = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self. start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print( "List tidak memiliki item")
            return
        else:
            n = self.start_node
            items = []
            while n is not None:
                items.append(str(n.item))
                n = n.ref
            print(" ; ".join(items))

    def delete_at_start(self):
        if self.start_node is None:
            print("List tidak memiliki item untuk dihapus")
            return
        data = self.start_node.item
        self.start_node = self.start_node.ref
        return data

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, queue):
        self.queue.insert_at_end(queue)

    def dequeue(self):
        removed = self.queue.delete_at_start()
        return removed

    def traverseQueue(self):
        self.queue.traverse_list()

    def check_order(self, item):
        if self.queue.start_node is None:
            print("Antrian kosong")
            return
        else:
            n = self.queue.start_node
            index = 1
            while n is not None:
                if n.item[0] == item:
                    print(f"Urutan {index} dari {self.size()} antrian")
                    return
                index += 1
                n = n.ref
            print("Item tidak ditemukan dalam antrian")

    def size(self):
        if self.queue.start_node is None:
            return 0
        else:
            n = self.queue.start_node
            count = 0
            while n is not None:
                count += 1
                n = n.ref
            return count

    def getAll(self):
        if self.queue.start_node is None:
            return []
        else:
            n = self.queue.start_node
            items = []
            while n is not None:
                items.append(n.item)
                n = n.ref
            return items

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def exists(self, val):
        if val == self.val[0]:
            return self.val
        if val < self.val[0]:
            if self.left == None:
                return []
            return self.left.exists(val)
        if self.right == None:
            return []
        return self.right.exists(val)

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
                return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    # def preorder(self, vals):
    #     if self.val is not None:
    #         vals.append(self.val)
    #     if self.left is not None:
    #         self.left.preorder(vals)
    #     if self.right is not None:
    #         self.right.preorder(vals)
    #     return vals

    # def inorder(self, vals):
    #     if self.left is not None:
    #         self.left.inorder(vals)
    #     if self.val is not None:
    #         vals.append(self.val)
    #     if self.right is not None:
    #         self.right.inorder(vals)
    #     return vals

    # def postorder(self, vals):
    #     if self.left is not None:
    #         self.left.postorder(vals)
    #     if self.right is not None:
    #         self.right.postorder(vals)
    #     if self.val is not None:
    #         vals.append(self.val)
    #     return vals
