#!python

import time

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        if self.is_empty():
            return 0
        length = 0
        currentNode = self.head
        while currentNode != None:
            length+=1
            currentNode = currentNode.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        newNode = Node(item)
        # TODO: Append node after tail, if it exists
        if self.is_empty(): #if head is empty, then append to head
            self.head = newNode
            self.tail = newNode
            return
        else: #point tail's next to newNode and assign newNode as the new tail
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        newNode = Node(item) #create a node with that item
        # TODO: Prepend node before head, if it exists
        if self.is_empty(): #if list is empty...
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head #point newNode's next to current head
        self.head = newNode #assign newNode as the head

    def find(self, quality): #do we return anything?
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        if self.is_empty():
            return None
        # TODO: Loop through all nodes to find item where quality(item) is True
        current = self.head
        while current != None:
            # TODO: Check if node's data satisfies given quality function
            if quality(current.data):
                return current.data
            current = current.next
        return None        

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
        currentNode = self.head
        if currentNode.data == item: #if head has the item
            self.head = currentNode.next #if head has next... assign next as new head
            if currentNode.next == None: #head is the last item... set self.tail to none
                self.tail = None
            return
        prev = None
        while currentNode != None: #loop until we reach tail
            print("Current node =", currentNode)
            if currentNode.data == item: #if node's data is the item... found!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                if currentNode.next == None: #if currentNode is the tail because it has no next...
                    self.tail = prev #prev node will now be the new tail
                prev.next = currentNode.next #DELETE currentNode by removing prev's next (reference) to currentNode's next
                return
            # TODO: Update previous node to skip around node with matching data
            prev = currentNode #if currentNode's data is not item, 
            currentNode = currentNode.next #keep going til it reach the tail
            print("Current.next = ", currentNode)
        # TODO: Otherwise raise error to tell user that delete has failed
        raise ValueError('Item not found: {}'.format(item))

    def update_list(self, data):
        '''Updates list by checking if data passed exist,
        if data exist in the list, delete then append
        if not just append'''
        for item in self.items():
            if item[0] == data[0]: #if key exist in a tuple, array, dictionary or hash table look until data exist and delete it
                print(f"Updating {item} to {data}")
                # self.delete(item) #delete and append
                # self.append(data)
                #For future, create a update function instead of deleting and appending
                item[1] = data[1]

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5]]:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    ll.update_list(['C', 1])
    print('list: {}'.format(ll))

    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('length: {}'.format(ll.length()))
    # # Enable this after implementing delete method
    # delete_implemented = True
    # if delete_implemented:
    #     print('\nTesting delete:')
    #     for item in ['E', 'A', 'D', 'B', 'C']:
    #         print('delete({!r})'.format(item))
    #         ll.delete(item)
    #         print('list: {}'.format(ll))
    #         print('HEADDDD: {}'.format(ll.head))
    #         print('TAILLLL: {}'.format(ll.tail))

    #     print('head: {}'.format(ll.head))
    #     print('tail: {}'.format(ll.tail))
    #     print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
    

        # if nodeData[0] == item:
        #     print("deletinggggg")
        #     ll.delete(data)
        # else:
        #     ll.append(nodeData)
        # print('list: {}'.format(ll))
    # print('list: {}'.format(ll))
