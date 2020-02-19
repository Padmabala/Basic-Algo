class queuee:
    def __init__(self,size):
        self.q=[]
        self.size=size
        self.front=-1
        self.rear=-1
    def enqueue(self,ele):
        if(self.front==self.size):
            print("Q is full")
        else:
            self.front+=1
            self.q.append(ele)
    def dequeue(self):
        if(self.front==self.rear):
            print("Q is empty")
        else:
            self.rear+=1
            print(self.q[self.rear])
            self.q[self.rear]=None

    def display(self):
        print(self.q, end=' ')
qu=queuee(5)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
qu.enqueue(9)
qu.enqueue(10)
qu.display()
qu.dequeue()
qu.display()