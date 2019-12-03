# Define Node Class
class Node:
    # Initializer
    def __init__(self, value):
        self.value = value
        self.next = None

    # Print Node Values
    def PrintNode(self):
        print(self.value)

class LinkedList:
    # Initializer
    def __init__(self):
        self.head = None

    # Get Last Node in List
    def GetTail(self):
        if(self.head is None):
            return None
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            return currentNode

    # Add Node to the end of the list
    def AddNode(self, node):
        tailNode = self.GetTail()
        if(tailNode == None):
            self.head = node
        else:
            tailNode.next = node

    # Print all node value in list
    def PrintList(self):
        if(self.head is None):
            print("The List is Empty")
        else:
            currentNode = self.head
            while currentNode is not None:
                currentNode.PrintNode()
                currentNode = currentNode.next                
            print("List End")
            
def main():
    mylist = LinkedList()
    mylist.AddNode(Node(1))
    mylist.AddNode(Node(2))
    mylist.AddNode(Node(3))
    mylist.PrintList()

if __name__ == "__main__":
    main()
