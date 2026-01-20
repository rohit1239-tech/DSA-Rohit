from collections import Counter


arr = Counter([1,2,2,3,2,3,3,4])

print(arr[2])

print(arr.most_common(1))
print(list(arr.elements()))


c1= Counter([1,2,2,3,4,2,3,1])
c2= Counter([1,2,3,4])
c3= c1 - c2
print(list(c3.elements()))