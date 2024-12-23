# movies=[] 
# movies.append(input("enter 1st movie :"))
# movies.append(input("enter 2nd movie :"))
# movies.append(input("enter 3rd movie :"))

# movies.insert( 1, 'adbhud' )

# print(movies)

#cheek palindrome
# list1 = [1,3,1]
# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")
# grade=("C","D",'A',"A","B","B","A")
# print(grade.count('A'))
list = ["C","D",'A',"A","B","B","A"] 
list.sort(reverse=True)
print("sorted :",list)
tup=(1,3,1,3,5,8)
print(tup.index(8))
print(type(tup))