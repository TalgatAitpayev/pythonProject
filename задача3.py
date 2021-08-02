numbers=[1,2,3,4,5,6,8,10,12,14]#как сделать input массива?
a=[]
for x in range(0,len(numbers)+1):
    if x%2==0:
        a.append(x)
print(len(a))