arr = [1,6,2,4,8]

#sorted in acending order 
print(sorted(arr))

#sorted in decending order
print(sorted(arr, reverse =True))

#shortcut to sort list in acending order
arr.sort()
print(arr)

#shortcut to sort list in decending order
arr.sort(reverse=True)
print(arr)

#how to sort according to absulute value
arr =[-1,5,-6,7,4]
print(sorted(arr, key =lambda x:abs(x)))
print(arr)

#sorting string 
fruits_list = ["apple ", "pineapple" , "kiwi"]
print(sorted(fruits_list, key = len))