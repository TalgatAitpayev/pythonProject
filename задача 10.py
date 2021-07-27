n=int(input())
a=0
c=1
for x in range(1,n+1):
    c*=x
a+=1+(1/c)

print(a) #ne pomnyu kak ukazat tochnost znacheniya