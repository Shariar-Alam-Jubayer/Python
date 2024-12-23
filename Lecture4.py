# dict={
#     "name":"jubayer",
#     "scores":{
#         "math":90,
#         "dsa":85,
#         "oop":95,
#     }
# }
# print(type(dict))
# print(dict["scores"]["math"])
# print(dict.items())
# print(dict.keys())
# print(dict.get('name'))
# print(dict.values())
# print(dict.update({"name":"shariar"}))
# print(dict)
# sets=set()
# sets.add(9)
# sets.add(6)
# sets.add(5)
# # sets.discard(1)
# print(sets)
# # sets.clear( )
# sets.pop()
# sets.pop()
# print(sets)
# print(type(sets))
# set={1,2,3,4}
# set2={1,2,2,5}
# print(set.union(set2))
# print(set.intersection(set2))

#lets practices
# dict={
#     "cat ": "a small animal",
#     "table" : {
#         "a piece of furniture",
#         "list of facts & figures"
# }
# }
# print(dict)

# set={"python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"}
# print(set)
# print(len(set))

marks={}
x=int(input("enter phy marks :"))
marks.update({"phy":x})

x=int(input("enter che marks :"))
marks.update({"che":x})

x=int(input("enter math marks :"))
marks.update({"math":x})
print(marks)
print(type(marks))

values={
    ("float",9.0),
    ("int",9)
}
print(type(values))
print(values)