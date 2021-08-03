numbers=[1,5,3,7,4]#как сделать input массива?
a=[]
for x in range(1,len(numbers)+1):
    if [x-1]<[x]:
        a.append(x)
print(len(a))