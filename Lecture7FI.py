# with open("practice.txt","w+") as f:
#     data =f.write("Hi everyone we are learning File I/O using Java. I like programming in Java.")
# with open("practice.txt","r") as f:
      # data =f.read()
# new_data=data.replace("Java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#       data =f.write(new_data)
# def cheaks_word():
#     word="xlearning"
#     with open("practice.txt","r") as f:
#       data =f.read()
#       if(data.find(word)!=-1):
#          print("found")
#       else:
#          print("not found")
# cheaks_word()


# def cheaks_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#       while data:
#          data =f.readline()
#          if(word in data):
#             print(line_no)
#             return
#          line_no+=1
#     return -1
# print(cheaks_line())

count=0
with open("practice.txt","r") as f:
      data =f.read()
      print(data)
      nums=data.split(",")
      for var in nums:
            if(int(var) % 2 ==0):
                  count+=1

print(count)