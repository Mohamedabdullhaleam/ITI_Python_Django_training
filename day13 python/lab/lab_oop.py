class Queue :
    def __init__(self,front,rear,length):
        self.queue=[""]*length
        front=0
        rear=0
        self.rear=rear
        self.front=front
        self.length=length
    def pop(self):
        val = self.queue[self.front]
        self.queue[self.front]=""
        self.front=(self.front+1)%self.length
        return val  
    def insert(self,value):
        self.queue[self.rear]=value
        self.rear=(self.rear +1)%self.length
        
    def is_empty(self):
        if self.rear - self.front == 0:
            return "empt"


class added_features(Queue):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def save_data(self,name):
        pass
    def load_data(self,name):
        with open('file.txt', 'a') as file:
            data_to_append = self.queue
            file.write(f"added data{data_to_append}")
            file.writelines("\n")

        
        
    
my_queue = added_features('mohamed')
my_queue.insert(3)
my_queue.insert(2)
my_queue.insert(1)
my_queue.insert(3)
my_queue.insert(2)



print(my_queue.queue)
print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
print(my_queue.pop())
print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
print(my_queue.pop())
print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
print(my_queue.queue)
print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
##################################################################################




