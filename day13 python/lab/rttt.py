import json

class QueueOutOfRangeException(Exception):
    pass


class queue2:

    queues = {}

    def _init_(self, name , size,):
        self.queue = []
        self.name = name
        self.size = size
        queue2.queues[self.name] = self

    def insert(self, value):
        if len(self.queue) < self.size:
            self.queue.append(value)
        else:
            raise QueueOutOfRangeException("QueueOutOfRange")

    def is_empty(self):
        return len(self.queue) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Warning! queue is empty")
            return 0
        
    @classmethod
    def save(cls, filename):
        queue_data = {name: {'name': queue.name, 'size': queue.size, 'queue': queue.queue} for name, queue in cls.queues.items()}
        data_to_save = {'queues': queue_data}

        with open(filename, 'w') as file:
            json.dump(data_to_save, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            queue_data = json.load(file)
            cls.queues = {name: queue2(name, queue_data[name]['size']) for name in queue_data}
            for name, queue in cls.queues.items():
                queue.queue = queue_data[name]['queue']

queue_test = queue2('Queue_Save', 5)

queue_test.insert(1)
queue_test.insert(2)

queue_test = queue2('Queue_test1', 6)
queue_test.insert(1)
queue_test.insert(2)

queue_test = queue2('Queue222222', 6)
queue_test.insert(111)
queue_test.insert(12)

queue2.save('test1.json')

queue2.load('test.json')
output1= queue2.queues["Queue1"]
print(output1.name)
print(output1.size)
print(output1.queue)