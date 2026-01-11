
def file_opener():
    with open('file.txt') as f:
        content=""
        for i in f:
            content+=i
            # print(i,end="")
        return content

f1 = file_opener()


def file_opener_new():
    with open('file1.txt') as f:
        content=""
        for j in f:
            # print(j,end="")
            content+=j
            # return j
        return content

f2 = file_opener_new()
# print(f2)

if f1==f2:
    print(f1)
else:
    print(f2)


# def old_file():
#     with open('file.txt') as x:
#         lst_x=[]
#         count = 0
#         for i in x:
#             #lst_x.append(i)
#             count+=1
#             # print(i,"it is from i",end="")
#             return i
#     return None

# # # print(count)
# # print(lst_x)

# def new_file():
#     with open('file1.txt') as y:
#         lst_y=[]
#         count1 = 0
#         for j in y:
#             # print(j,"it is from j",end="")
# #         lst_y.append(j)
#             count1+=1
#             return j
#     return None


# # print(count1)
# print(lst_y)




# if old_file() == new_file():
#     print(old_file())
# else:
#     print(new_file())









# lst_new=[]

# def update(list:str):
#     for i in lst_x:
#         print(i +" it is from i")
#         return lst_new.append(i)
#         for j in lst_y:
#             print(j,"it is from j")
#             if i==j:
#                 print("i")
#                 return lst_new.append(i)
#             else:
#                 print("j")
#                 return lst_new.append(j)

# update(lst_new)
# print(lst_new)







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
