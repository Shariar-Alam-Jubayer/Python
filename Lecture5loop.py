# n=int(input("num :"))
# count=1
# while  count<=10 :
#     print((count*n))
#     count+=1
# n=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# count=0
# while  count<len(n) :
#     print(n[count])
#     count+=1
# n=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# count=0
# while  count<len(n) :
#     if(n[count]==9):
#         print("found indx",count)
#         break;
#     else:
#         print("not found")
    
#     count+=1
# count=1
# while  count<=10 :
    
#     if(count==5):
#         count+=1
#         continue;
#     print(count)
#     count+=1


#for loop

# n=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for var in n :
#     print(var)

# n=[1, 4, 9, 16, 25, 36, 49, 64, 81,100,9]
# index=0
# for var in n :
#     if(var==9):
#         print("found indx",index)
#     index+=1
    
    #range()

# for el in range(100,0,-1):
#     print(el)
# n=int(input("number :"))
# for el in range(1,11):
#     print(el*n)

      #WAP to find the sum of first n numbers. (using while)

# n=int(input("num :"))
# count=1
# sum=0
# while  count<=n :
#     sum+=count
#     count+=1
# print("sum is :",sum)
    #WAP to find the factorial of first n numbers. (using for)
n=int(input("number :"))
factorial=1
for el in range(1,n+1):
    factorial*=el
print("factorial is :",factorial)