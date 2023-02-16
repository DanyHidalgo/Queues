from lqueue import LinearQueue

q = LinearQueue(5)
print(q)

#Underflow 1
val = q.dequeue()

#inserts
q.enqueue('A')
print(q)
q.enqueue('B')
print(q)
q.enqueue('C')
print(q)

#Search
print("Search A:", q.search('A'))
print("Search F:", q.search('F'))
print("Search C:", q.search('C'))

q.enqueue('D')
print(q)

#overflow
q.enqueue('E')
q.enqueue('F')

#delete
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

#Peek
print('Element peeked:', q.peek())

val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

#Underflow 2 
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))


