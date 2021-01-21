
    def insert(self,head,data): 
        newNode = Node(data)
        if head == None:
            head = newNode
            return head
        currentNode = head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode
        return head
        
    #Complete this method
  
