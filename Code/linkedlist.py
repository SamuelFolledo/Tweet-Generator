#!python


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
        length = 1
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
            length+=1
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        newNode = Node(item)
        if self.is_empty(): #if head is empty, node's pointer wil be nil
            self.head = newNode
        else:
            currentNode = self.head #make currentNode the head, and loop through til we find the tail
            while currentNode.next != None: #while not at tail
                currentNode = currentNode.next #traverse to next node
            # TODO: Append node after tail, if it exists
            currentNode.next = newNode #now that we are at tail, point tail to newNode
        self.tail = newNode #assign newNode as the tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        newNode = Node(item) #create a node with that item
        # TODO: Prepend node before head, if it exists
        if self.is_empty: #if list is empty...
            self.head = newNode
            self.tail = newNode


        if self.is_empty == False: #if head has data... point newNode to the current head
            newNode.next = self.head
            self.head = newNode #assign newNode as the head
            return

    def find(self, quality): #do we return anything?
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        if self.is_empty():
            ValueError('Item not found: {}'.format(item))
            return
        currentNode = self.head
        if currentNode.data == item: #if head has the item
            self.head = currentNode.next #if head has next... assign next as new head
            if currentNode.next == None: #head is the last item... set self.tail to none
                self.tail = None
            return
        if currentNode == None: #if currentNode reached the tail... item is not found
            self.tail = currentNode.next
            # TODO: Otherwise raise error to tell user that delete has failed
            raise ValueError('Item not found: {}'.format(item))
            return
        prev = None
        while currentNode != None: #loop until we reach tail
            if currentNode.data == item: #if node's data is the item... found!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                if currentNode.next == None: #if currentNode was the tail
                    self.tail = prev #prev node will now be the new tail
                prev.next = currentNode.next #DELETE currentNode by removing prev's next (reference) to currentNode's next
                return
            # TODO: Update previous node to skip around node with matching data
            prev = currentNode #if currentNode's data is not item, 
            currentNode = currentNode.next #keep going til it reach the tail
        ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C', 'D', 'E']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))
    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['E', 'A', 'D', 'B', 'C']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
            print('HEADDDD: {}'.format(ll.head))
            print('TAILLLL: {}'.format(ll.tail))

        # print('head: {}'.format(ll.head))
        # print('tail: {}'.format(ll.tail))
        # print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

### WHY IS MY LAST TAIL NOT GETTING DELETED IN??