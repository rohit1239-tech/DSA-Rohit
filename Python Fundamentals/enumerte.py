#(index , value )
arr = [5,6,1,3]
print(list(enumerate(arr)))

#if you want in colunm 
for i,val in list(enumerate(arr)):
    print(i,val)

#another method 
for i in range(len(arr)):
    val = arr[i]
    print(i, val)
