
class Circularqueue:

    def __init__(self, size: int)-> None:
        
        self.elements = [None] * size
        self.max = size
        self.front = -1
        self.rear = -1


    def __repr__(self):
        return 'Queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear)


    def enqueue(self, value: str) -> None:
        
        if self.front == 0 and self.rear == self.max -1 or self.front -1 == self.rear:
            print('Queue Overflow...')
            return None

        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        
        elif self.rear == self.max -1 and self.front != 0:
            self.rear = 0

        else:
            self.rear += 1

        self.elements[self.rear] = value


    def dequeue(self) -> str:

        if self.front == -1:
            print("Queue Underflow")
            return None
        
        value = self.elements[self.front]
        self.elements[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        elif self.front  == self.max -1:
            self.front = 0
        
        else:
            self.front += 1

        return value


    def search(self, key: str) -> int:
        
        if self.front < self.rear:
            for i in range(self.front, self.rear + 1):
                if self.elements[i] == key:
                    return i
        
        else:
            for i in range(0, self.rear + 1):
                if self.elements[i] == key:
                    return i
            
            for i in range(self.rear, self.front + 1):
                if self.elements[i] == key:
                    return i
            
            for i in range(self.front, self.max):
                if self.elements[i] == key:
                    return i        
        
        return -1


    def peek(self) -> str:
        
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return None
            
        return self.elements[self.front]