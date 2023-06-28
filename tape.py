n = int(input("Please enter number of files : "))
length = []
for i in range(0,n):
    element = -int(input("Please enter the length of " + str(i+1) + "th file : "))
    length.append(element)


sort = []

for i in range(len(length)):
    max = length[i]
    pointer = i
    for j in range(len(length)):
        found = False
        for k in range(i): 
            if sort[k] == j+1:
                found = True
                break
        if found:
            continue
        else :
            if length[j] > max:
                max = length[j]
                pointer = j
    length[pointer] = float('-inf')
    pointer = pointer+1
    sort.append(pointer)

print(sort)
  
