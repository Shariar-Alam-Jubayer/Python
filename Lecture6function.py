# movies =["zero","goster","martex","avasem","hostad hotel","chup"]
cities=["dhaka","barishal","comilla","sylate"]

# def list_len(list):
#     return len(list)

# print(list_len(movies))
# print(list_len(cities))

# def print_list(list):
#     for var in list :
#         print(var,end=" ")

# print_list(cities)

# def facto(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
    
# print(facto(5))

# def converter (usd):
#     bd=119.54*usd
#     print(usd,"usd to",bd,"bd")

# converter(100)

# def sums(n):
#     if(n==0):
#         return 0
    
#     return sums(n-1)+n
    
# print(sums(5))


def print_list(list,index):
    if(index==len(list)):
        return
    print(list[index])
    return print_list(list,index+1)


movies =["zero","goster","martex","avasem","hostad hotel","chup"]
print_list(movies,0)