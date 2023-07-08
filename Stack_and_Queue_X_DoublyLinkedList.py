#DoublyLinkedList__X__Stack&Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Stack_and_Queue_X_DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.top = None
        self.rear = None
    
    def enqueue(self,data):
        self.data = data
        if self.start==None:
            newNode = Node(self.data)
            self.start = newNode
        else:
            newNode = Node(self.data)
            newNode.next = self.start
            self.start.prev = newNode
            self.start = newNode
            self.temp = self.start
            while self.temp.next!=None:
                self.temp = self.temp.next
            self.rear = self.temp
            self.top = self.rear
    
    def push(self,data):
        self.data = data
        if self.start==None:
            newNode = Node(self.data)
            self.start = newNode
            self.top = self.start
        else:
            newNode = Node(self.data)
            self.top.next = newNode
            newNode.prev = self.top
            self.top = newNode
            self.rear = self.top
    
    def dequeue(self):
        if self.start==None:
            print("Can't Dequeue as List is Empty")
        elif(self.start==self.rear):
            self.start=None
            self.rear=None
            self.front=None
            self.top=None
        else:
            self.rear = self.rear.prev
            self.rear.next=None
            self.top = self.rear
        
    def pop(self):
        if self.top==None:
            print("Item cannot be popped as List is Empty")
        elif(self.top==self.start):
            self.start=None
            self.top=None
            self.rear=None
        else:
            self.top = self.top.prev
            if self.top!=None:
                self.top.next=None
            self.rear = self.top
    
    def getTop(self):
        if self.start==None and self.top==None:
            print("Cannot get Top Element as List is Empty")
            return None
        else:
            return self.top.data
    
    def getFront(self):
        if self.start==None:
            print("Cannot get Front Elment as List is Empty")
            return None
        else:
            return self.start.data
            
    def getRear(self):
        if self.start==None:
            print("Cannot get Rear Element as List is Empty")
        else:
            return self.rear.data
            
    def print_Elements(self):
        if self.start==None:
            print("Cannot print Elements as List is Empty")
            return None
        else:
            self.temp = self.start
            print("Elements inside list are : ",end=' ')
            while(self.temp.next!=None):
                print(self.temp.data,end=' ,')
                self.temp = self.temp.next
            print(self.temp.data)


choice = 0

while choice!=4 :
    print("-------------------------")
    print("1.Stack")
    print("2.Queue")
    print("3.Doubly LinkedList")
    print("4.Exit")
    print("-------------------------")
    
    choice = int(input("Which Data  structure you want to use : "))
    print("")
    
    if(choice==1):
        myDs = Stack_and_Queue_X_DoublyLinkedList()
        in_choice = 0
        while(in_choice!=5):
            print("-------------------------")
            print("1. Push")
            print("2. Pop")
            print("3. Get Top")
            print("4. Print Stack")
            print("5. Exit")
            print("-------------------------")
            in_choice=int(input("Enter Your Choice : "))
            if(in_choice==1):
                print("")
                data = input("Enter data You want to insert : ")
                myDs.push(data)
                print("")
            elif(in_choice==2):
                print("")
                print("Element ",myDs.getTop()," is popped from stack")
                myDs.pop()
                print("")
            elif(in_choice==3):
                print("")
                print("Top element is ",myDs.getTop())
                print("")
            elif(in_choice==4):
                print("")
                myDs.print_Elements()
                print("")
            elif(in_choice==5):
                print("")
                print("Exited From Stack")
                print("")
                break
            else:
                print("Invalid Choice")
            
    elif(choice==2):
        myDs = Stack_and_Queue_X_DoublyLinkedList()
        in_choice = 0
        while(in_choice!=6):
            print("-------------------------")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Get Front")
            print("4. Get Rear")
            print("5. Print Queue")
            print("6. Exit")
            print("-------------------------")
            in_choice=int(input("Enter Your Choice : "))
            if(in_choice==1):
                print("")
                data = input("Enter data You want to insert : ")
                myDs.enqueue(data)
                print("")
            elif(in_choice==2):
                print("")
                print("Element ",myDs.getRear()," is dequeued from Queue")
                myDs.dequeue()
                print("")
            elif(in_choice==3):
                print("")
                print("Front Element is ",myDs.getFront())
                print("")
            elif(in_choice==4):
                print("")
                print("Rear Element is ",myDs.getRear())
                print("")
            elif(in_choice==5):
                print("")
                myDs.print_Elements()
                print("")
            elif(in_choice==6):
                print("")
                print("Exited From Queue")
                print("")
                break
            else:
                print("")
                print("Invalid Choice")
                print("")
    elif(choice==3):
        myDs = Stack_and_Queue_X_DoublyLinkedList()
        in_choice = 0
        while(in_choice!=8):
            print("-------------------------")
            print("1. Insert at Beginning")
            print("2. Insert at Random")
            print("3. Insert at End")
            print("4. Delete First")
            print("5. Delete Random")
            print("6. Delete Last")
            print("7. Print List")
            print("8. Exit")
            print("-------------------------")
            in_choice=int(input("Enter Your Choice : "))
            if(in_choice==1):
                print("")
                data = input("Enter data You want to insert : ")
                myDs.enqueue(data)
                print("")
            elif(in_choice==2):
                pass
            elif(in_choice==3):
                print("")
                data = input("Enter data You want to insert : ")
                myDs.push(data)
                print("")
            elif(in_choice==4):
                pass
            elif(in_choice==5):
                pass
            elif(in_choice==6):
                print("")
                print("Element ",myDs.getTop()," is Deleted from List")
                myDs.pop()
                print("")
            elif(in_choice==7):
                print("")
                myDs.print_Elements()
                print("")
            elif(in_choice==8):
                print("")
                print("Exited From DoublyLinkedList")
                print("")
                break
            else:
                print("")
                print("Invalid Choice")
                print("")    
                
    elif(choice==4):
        print("")
        print("Thank You Bye Bye")
        break
    else:
        print("")
        print("Invalid Choice")
        print("")
    










