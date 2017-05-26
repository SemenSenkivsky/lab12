from node import *        

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None



    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.n = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.n 
        if current is not None:
            if previous is None:
                self._head = self._head.n 
            else:
                previous.n = current.n 

    def remove_all(self,_head):
        while self._head:
            old_node = self._head
            self._head = self._head.next
            print(old_node)
            del(old_node)

    def len(self):
        cur = self._head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count
    def split_half(self):
        l = self.len()
        if l > 1:
            ls1 = Multiset()
            ls2 = Multiset()
            cur = self._head
            for i in range(0,l % 2):
                ls1.add(cur)
                cur = cur.next
            while cur:
                ls2.add(cur)
                cur.next
            return ls1,ls2
        else:
            return None

