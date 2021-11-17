
class Node:
    def __init__(self):
        self.nextNode = None


# SortedList class
class SortedList:
    def __init__(self):
        # Pointer towards the first Node (currently nothing)
        self.headNode = None
        self.currentNode = None
        self.length = 0  # Variable we manually keep track of number of Nodes in the list

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        self.length += 1
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        # Check it is going to be inserted
        # between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
        # Once we reach here it must be added at the tail
        # Beacuse newNode is largest than all the other nodes.
        leftNode.nextNode = newNode

    def __str__(self):
        # We start at the head
        output = ""
        node = self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = f"'{node.__str__()}'"
                firstNode = False
            else:
                output += (', ' + f"'{node.__str__()}'")
            node = node.nextNode
        return output
