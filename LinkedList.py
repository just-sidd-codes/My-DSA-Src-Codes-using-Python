#LinkedList Implementation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def count_Elements(self):
        if(self.start==None):
            return 0
        else:
            self.temp = self.start
            self.count=0
            while self.temp.next!=None:
                self.temp = self.temp.next
                self.count+=1
            return self.count+1
    
    def insert_at_beginning(self,data):
        self.data = data
        if(self.start==None):
            self.start = Node(self.data)
        else:
            newNode = Node(self.data)
            newNode.next = self.start
            self.start = newNode
    
    def insert_at_random(self,data,position):
        self.data = data
        self.position = position
        self.count = self.count_Elements()
        if(self.count==0):
            if(self.position==1):
                self.insert_at_beginning(self.data)
            else:
                print("Cannot insert at ",self.position," position because Linked list is empty")
        if(self.count>0):
            if(self.position<self.count+2):
                if(self.position==1):
                    self.insert_at_beginning(self.data)
                elif(self.position==self.count+1):
                    self.insert_at_end(self.data)
                else:
                    newNode = Node(self.data)
                    self.temp = self.start
                    for i in range(1,self.position):
                        self.temp = self.temp.next
                    newNode.next = self.temp
                    self.temp = self.start
                    for i in range(1,self.position-1):
                        self.temp = self.temp.next
                    self.temp.next = newNode
            else:
                print("Invalid Position")
                return 0
    
    def insert_at_end(self,data):
        self.data = data
        if(self.start==None):
            self.start = Node(self.data)
        else :
            self.temp = self.start
            while self.temp.next!=None:
                self.temp = self.temp.next
            self.temp.next = Node(self.data)
    
    def delete_First(self):
        if(self.start==None):
            print("List is Empty")
            return 0
        else:
            self.temp=self.start
            self.start = self.start.next
            self.temp1 = self.start
            while self.temp1.next!=None:
                self.temp1 = self.temp1.next
            return self.temp
    
    def delete_Random(self,position):
        self.position = position
        self.count = self.count_Elements()
        if(self.count==0):
            print("List is Empty...Cannot delete element")
        elif(self.count>0):
            if(self.position<=self.count):
                if(self.position==1):
                    self.delete_First()
                elif(self.position==self.count):
                    self.delete_Last()
                else:
                    self.temp1 = self.start
                    self.temp2 = self.start
                    for i in range(1,self.position-1):
                        self.temp1 = self.temp1.next
                    for i in range(1,self.position+1):
                        self.temp2 = self.temp2.next
                    self.temp1.next = self.temp2
            else:
                print("Position does not exist")
                return 0
    
    def delete_Last(self):
        if(self.start==None):
            print("List is Empty")
            return 0
        else:
            self.temp=self.start
            while (self.temp.next).next!=None:
                self.temp = self.temp.next
            self.temp.next = None
                
            
    def printList(self):
        if(self.start==None):
            print("List is Empty")
        else:
            self.temp = self.start
            while self.temp.next!=None:
                print(self.temp.data)
                self.temp = self.temp.next
            print(self.temp.data)
            
option = None

myList =LinkedList()

while(option!=9):
    print("")
    print("1. Insert at Beginning in LinkedList")
    print("2. Insert at any random position in LinkedList")
    print("3. Insert at End in LinkedList")
    print("4. Delete First Element of LinkedList")
    print("5. Delete any random Element of LinkedList")
    print("6. Delete Last Element of LinkedList")
    print("7. Get count of LinkedList")
    print("8. Print LinkedList")
    print("9. Exit")
    print("")
    
    option=int(input("What do You Want to do : "))
    
    if option==1:
        data = input("Enter the Element You want to insert at beginning : ")
        myList.insert_at_beginning(data)
        print("Element ",data," is inserted in beginning of LinkedList")
        print("")
    elif option==2:
        data = input("Enter the Element You want to insert at random position : ")
        position = int(input("Enter the position : "))
        if(position<0):
            print("Invalid position")
            continue
        else:
            if myList.insert_at_random(data,position)!=0:
                print("Element ",data," is inserted at position ",position," in linkedlist")
            print("")
    elif option==3:
        data = input("Enter the Element You want to insert at end : ")
        myList.insert_at_end(data)
        print("Element ",data," is inserted at the end of LinkedList")
    elif option==4:
        if(myList.count_Elements()==0):
            print("LinkedList is Empty...Cannot delete Elements")
        else:
            myList.delete_First()
            print("First Element is deleted")
            print("")
    elif option==5:
        position = int(input("Enter the position : "))
        if(position<0):
            print("Invalid position")
            continue
        else:
            if myList.delete_Random(position)!=0:
                print("Item at ",position," position is deleted from linkedlist")
            print("")
    elif option==6:
        if(myList.count_Elements()==0):
            print("LinkedList is Empty...Cannot delete Elements")
        else:
            myList.delete_Last()
            print("Last Element is deleted")
            print("")
    elif option==7:
        print("Count of the linkedlist is : ",myList.count_Elements())
        print("")
    elif option==8:
        print("LinkedList : ")
        myList.printList()
        print("")
    elif option==9:
        print("Thank You Bye Bye")
        break
    else:
        print("Invalid Choice")
        print("")
    






