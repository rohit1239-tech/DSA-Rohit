from collections import OrderedDict

od = OrderedDict([(1,"rohit"),(3,"sharma"),(7,"ronaldo")])

print(od[1])
print(od[4])

if 10 in od:
    print(od[10])
else:
    print("not in the od")