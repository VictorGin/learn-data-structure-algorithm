from traceback import print_list


class NewNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = NewNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        appended_node = NewNode(value)
        if self.head is None:
            self.head = appended_node
            self.tail = appended_node
        else:
            self.tail.next = appended_node
            self.tail = appended_node
            self.length += 1
        # return True

# original_list = LinkedList(4)
# original_list.printList()
# append_list = original_list.append(5)
# append_list.printList()
    def pop(self):
        if self.length > 1:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            print('Empty linked_list cannot pop!!!')
            return None

    def prepend(self,value):
        prepend_node = NewNode(value)
        last_head = self.head
        self.head = prepend_node
        self.head.next = last_head
        self.length += 1

    def pop_first(self):
        if self.length > 1:
            self.head = self.head.next
            self.length -= 1
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            return None

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
    
    def insert(self,index,value):
        if self.length != 0:
            NN = NewNode(self.tail.value)
            self.append(NN.value)
            for _ in range(index,self.length):
                temp = self.get(index)
                if index+1 < self.length:
                    self.set_value(index+1,temp.value)
                else:
                    pass
            self.set_value(index,value)
        else:
            return None

OL = LinkedList(4)
# OL.pop()

# OL.append(5)
# OL.append(5)
OL.insert(1,2)
# OL.set_value(1,2)
OL.printList()
# print(OL.tail.next)
# print(OL.length)






