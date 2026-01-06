lst = []

str = '''abc
de
f'''

str1 = '''abz
de
z
'''
with open('file.txt') as f:
    count = 0
    for i in f:
        print(i,end="")
        count+=1
    print(count)


# print(str.readline())


# for i in str:
#     lst.append(i)

# print(lst)

# for i in str:
#     for j in str1:



# countt =0 
# for i in str:
#     if i is " ":
#         countt = count+1
#         lst.append(i)
# print(countt)
# print(lst)


# for i in str:
#     count = 0
#     if i.endswith(" "):
#         count+=1

# print(count)
# print(str)
# counte = 0 
# for i in str:
#     print(i,end=" ")
#     counte+=1
#     print(counte)
