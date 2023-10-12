import json 
class Queue :
    def __init__(self,name,front,rear,length):
        self.queue=[""]*length
        front=0
        rear=0
        self.name=name
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
        print(self.rear - self.front)
        if self.rear - self.front >= self.length  : 
            raise IndexError("Index is out of range")
        
    def is_empty(self):
        if self.rear - self.front == 0:
            return "empt"
    def save_data(self,name):
        pass
    def load_data(self,name):
        with open('file.txt', 'a') as file:
            data_to_append = self.queue
            file.write(f"added data{data_to_append}")
            file.writelines("\n")


 
my_queue = Queue("mo",0,0,6)
my_queue.insert(3)
my_queue.insert(2)
my_queue.insert(1)
my_queue.insert(3)
my_queue.insert(2)
my_queue.load_data("mo")

print(my_queue.queue)
my_queue2 = Queue("lo",0,0,6)
my_queue2.insert(3)
my_queue2.insert(2)
my_queue2.insert(8)
my_queue2.insert(5)
my_queue2.insert(4)
my_queue2.load_data("mo")
print(my_queue2.queue)


# print(my_queue.queue)
# print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
# print(my_queue.pop())
# print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
# print(my_queue.pop())
# print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
# print(my_queue.queue)
# print(f"rear :{my_queue.rear} ,front :{my_queue.front}")
##################################################################################

