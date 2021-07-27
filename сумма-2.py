n=int(input())
c=0
for x in range(1,n+1):
    c+=4*(1+((-1*x)/((2*x)+1)))
    print(c)