"""
1-Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction. Your node class will look this this
2-Implement all other methods in regular linked list class and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

3-Add following new methods
def print_forward(self):
    #This method prints list in forward direction. Use node.next
def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
"""

class Node: 
    def __init__(self, data=None, prev=None, next=None):
        self.data = data 
        self.prev = prev 
        self.next = next

    
class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.last = None
    
    def __str__(self):
        if self.head is None:
            return "The list is empty"
        
        itr = self.head 
        list = ''

        while itr:
            list += str(itr.data) + ' => '
            itr = itr.next
        
        return list 
    
    def insert_at_start(self, data):
        head = self.head
        node = Node(data, None, head)
        head.prev = node
        self.head = node
        if self.head.next is None:
            self.last = self.head

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.last = node
            return
        
        ultimo = self.last

        node = Node(data, ultimo, None)
        ultimo.next = node
        self.last = node 

    def insert_values(self, data_list):
        self.head = None 
        self.last = None 
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head 

        while itr:
            count += 1
            itr = itr.next 

        return count

    def remove_at(self, index):
        if index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            next = self.head.next 
            next.prev = None
            self.head = next 
            return
            
        if index == self.get_length() - 1:
            last_before = self.last.prev
            last_before.next = None
            self.last = last_before
            return

        count = 0 
        itr = self.head
        while count <= index:
            if count == index - 1:
                next_next = itr.next.next 
                itr.next = next_next
                next_next.prev = itr
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_start(data)
            return
        
        if index == self.get_length() - 1:
            self.insert_at_end(data)
            return
        
        count = 0
        itr = self.head 
        while count <= index:
            if count == index - 1:
                bef = itr
                aft = itr.next
                node = Node(data, bef, aft)
                aft.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, value_after, value_to_insert):
        
        len = self.get_length()

        if len == 0:
            return "List is empty"
        
        if value_after == self.head.data:
            node = Node(value_to_insert, self.head, self.head.next)
            self.head.next = node
            return 
        
        if value_after == self.last.data:
            node = Node(value_to_insert, self.last, None)
            self.last.next = node
            self.last = node 
            return
        
        count = 0 
        itr = self.head 

        while count < len:
            if itr.data == value_after:
                itr_next = itr.next
                node = Node(value_to_insert, itr, itr_next)
                itr_next.prev = node
                itr.next = node 
                break
            itr = itr.next 
            count += 1

    def remove_by_value(self, value_to_remove):
        len = self.get_length()

        if len == 0:
            return "List is empty"
        
        if value_to_remove == self.head.data:
            next = self.head.next 
            next.prev = None
            self.head = next 
            return
            
        if value_to_remove == self.last.data:
            last_before = self.last.prev
            last_before.next = None
            self.last = last_before
            return
        count = 0
        itr = self.head
        while count < len:
            if itr.next.data == value_to_remove:
                next_value_next = itr.next.next
                next_value_next.prev = itr
                itr.next = next_value_next
                break

            itr = itr.next 
            count += 1
    
    def print_forward(self):
        len = self.get_length()

        if len == 0: 
            print("List is empty")
            return 
        
        itr = self.head 
        items = ''
        while itr:
            items += str(itr.data) + " - "
            itr = itr.next
        print(items)
        
    def print_backward(self):
        len = self.get_length()

        if len == 0: 
            print("List is empty")
            return 
        
        itr = self.last 
        items = ''
   
        while itr:
            items += str(itr.data) + ' - '
            itr = itr.prev
           
        print(items)
        
#fazer o numero 3 agora

dll = DoubleLinkedList()

dll.insert_values(['calça', 'blusa de frio', 'luvas', 'camiseta', 'touca', 'meias'])
print(dll)
dll.remove_at(4)
dll.print_backward()
dll.print_forward()
dll.insert_at_start('botas')
dll.print_backward()
dll.print_forward()