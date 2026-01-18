#how to write function to count length of string 

def leng_of_string(s):
    cnt = 0
    for element in s:
        cnt =cnt+1
    return cnt 

s= "rohit"
result = leng_of_string(s)
print(result)

#direct method

print(len(s))