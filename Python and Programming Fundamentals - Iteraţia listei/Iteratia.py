string = "3,9,13,4,42"

print("Actual String containing integers: ", string)
print("Type of string: ", type(string))

list1 = list(string.split(','))
print("Converted string to list : ", list1)

list2 = list(map(int, list1))
print("List of integers : ", list2)

b = []
for i in range(len(list2)):
    a = pow(list2[i], 2)
    b.append(a)
print("Power lifting list 2 : ", b)



string = ', '.join(str(i) for i in b)
print("Final string : " + string)