class Node():

    def __init__(self,value):
        self.next = None
        self.value = value

class linked_list():

    def __init__(self):
        self.head = None
    
    def append(self,value):
        current_node = self.head
        if current_node == None:
            self.head = Node(value)
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
    def list_elements(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def length(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def get_element(self,position):
        if position < 0:
            return 'not in the list.'
        i = 0
        current_node = self.head

        while current_node is not None:
            if i == position:
                return current_node.value
            else:
                i = i + 1
                current_node = current_node.next
        return 'not in the list'

    def reverse_list(self):
        
        previos_node = None
        current_node = self.head

        while current_node is not None:
            
            next_node = current_node.next
            current_node.next = previos_node
            previos_node = current_node
            current_node = next_node
        
        self.head = previos_node

my_list = linked_list()
my_list.append(34)
my_list.append(4567)
my_list.append(3456)
my_list.append(323)
my_list.append(7)

my_list.reverse_list()
my_list.list_elements()
