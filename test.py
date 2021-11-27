n=int(input("Enter the number of tweets"))
a=[]
b=[]
counter=0
count_arr=[]

for i in range(0,n):
    username=input("Enter user name-->")
    #tweet_id=input("Enter user Tweet Id--->")

    
    a.append(f'{username} ')
    print(a[i])
    c=(a[i].split())
    b.append(c[0])
print(len(b))
print(a,'\n')
print(b,'\n')
for i in range(0,len(b)):
    for j in range(0,i):
        if (b[i]==b[j]):
            counter=counter+1
            
print(counter)




    



