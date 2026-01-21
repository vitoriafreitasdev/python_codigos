class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_begging(self, data):
        node = Node(data, self.head)
        self.head = node 

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return 

        itr = self.head 
        listr = ''
        while itr: 
            listr += str(itr.data) + " --> "
            itr = itr.next 
        
        print(listr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head 
        while itr.next:
            itr = itr.next 
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None 
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
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next 
            return 
        
        count = 0 
        itr = self.head 

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next 
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begging(data)
            return
        
        count = 0
        itr = self.head 
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node 
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        
        count = 0
        len = self.get_length()

        if len == 0:
            print("The list is empty")

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head

        while count < len:

            if itr.data == data_after:
                new_node = Node(data_to_insert, itr.next)
                itr.next = new_node
                break

            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        # Remove first node that contains data
        count = 0
        len = self.get_length()

        if len == 0:
            print("The list is empty")

        itr = self.head 

        if itr.data == data:
            self.head = itr.next
            return

        while count < len:
        
            if itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break

            itr = itr.next 
            count += 1

if __name__ == '__main__':
    # li = LinkedList()
    # li.insert_at_begging(5)
    # li.insert_at_begging(8)
    # li.insert_at_end(10)
    # li.print()

    # li2 = LinkedList()

    # li2.insert_values(["banana", "mango", "grapes", "orange"])

    # li2.print()

    # print(li2.get_length())

    # li2.remove_at(2)

    # li2.print()

    # li2.insert_at(0, "figs")
    # li2.insert_at(2, "jackfruit")

    # li2.print()

    #Exerc
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange", "figs"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.insert_values(['calça', 'blusa de frio', 'luvas', 'camiseta', 'touca', 'meias'])
    ll.print()

    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()

#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md


