# Sources --> https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1287/

# Python code sources --> https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

# Each node in a singly-linked list contains not only the value but also a -> reference field <- to link to the next node. By this way, the singly-linked list organizes all the nodes in a sequence.

# --> Opearation
# Unlike the array, we are not able to access a random element in a singly-linked list in constant time. If we want to get the ith element, we have to traverse from the head node one by one. It takes us O(N) time on average to --> visit an element by index <--, where N is the length of the linked list.

# [23,  ---]--->  [6,  ---]---> [15,  ---] ---> ...

# For instance, in the example above, the head is the node 23. The only way to visit the 3rd node is to use the "next" field of the head node to get to the 2nd node (node 6); Then with the "next" field of node 6, we are able to visit the 3rd node.

# Create node


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# Create singly linked list


class SLinkedList:
    def __init__(self):
        self.headval = None
