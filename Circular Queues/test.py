from cqueue import Circularqueue

q = Circularqueue(5)
print(q)

#inserts
q.enqueue('A')
print(q)
q.enqueue('B')
print(q)
q.enqueue('C')
print(q)
q.enqueue('D')
print(q)
q.enqueue('E')
print(q)

#overflow case 1
q.enqueue('F')
print(q)

#delets
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

#underflow
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

q.enqueue('A')
print(q)
q.enqueue('B')
print(q)
q.enqueue('C')
print(q)
q.enqueue('D')
print(q)
q.enqueue('E')
print(q)

val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

q.enqueue('F')
print(q)

#overflow case 2
q.enqueue('G')
print(q)
