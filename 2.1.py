class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

def printLL(head):
    itr = head
    while itr != None:
        print(itr.data)
        itr = itr.next

def removeDups(head):
    prev_ptr = head
    buffer = {}
    buffer[prev_ptr] = True

    while (prev_ptr != None):
        print(prev_ptr.data)
        if prev_ptr.next.data in buffer:
            #delete curr_ptr node
            prev_ptr.next = prev_ptr.next.next
        else:
            buffer[prev_ptr.next.data] = True
        prev_ptr = prev_ptr.next

#TEST

list1 = SLinkedList()
list1.head = Node("Mon")
list1.head.next = Node("Tue")
list1.head.next.next = Node("Tue")#Repeat for test
list1.head.next.next.next = Node("Wed") 
list1.head.next.next.next.next = Node("Thurs") 
list1.head.next.next.next.next.next = Node("Fri") 
list1.head.next.next.next.next.next.next = Node("Fri") 

removeDups(list1.head)