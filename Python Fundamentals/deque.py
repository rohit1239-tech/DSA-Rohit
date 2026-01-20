from collections import deque

dq = deque([2,3,1])

#add element in list at the end
dq.append(5)
print(dq)

#to append left
dq.appendleft(7)
print(dq)

#to remove right most element in list
dq.pop()
print(dq)


dq.popleft()
print(dq)

#extend 
dq.extend([10,19])
print(dq)


#extendleft for add element in start

#rotate
dq.rotate(2)
print(dq)