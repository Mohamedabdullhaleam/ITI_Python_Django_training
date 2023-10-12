#p1
# Write a program that counts up the number of vowels [a, e, i, o,
# u] contained in the string.
# v_count=0
# name = input("enter your string ")
# for i in name :
#     if i in(['a', 'e', 'i', 'o', 'u']): 
#         v_count+=1
# print(f"number of vouls ={v_count}")
#############################################
# Fill an array of 5 elements from the user, Sort it in descending
# and ascending orders then display the output.

user_array = []
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    elements = input(f"Enter element {i+1}: ")
    user_array.append(elements)
    sorted_acend = user_array.sort()



#  #or
# userr_array=input('enter array elements :').split()
# print("User array:", userr_array)
#########################################################3
# Write a program that prints the number of times the string 'iti'
# occurs in anystring.
# st="iti insituation iti instituation iti instituation"
# count=st.count("iti")
# print(f"iti mentioned : {count} times")
########################################3
# Write a program that remove all vowels from the input word and
# generate a brief version of it.

# name = input("enter your string ")
# for i in name :
#     if i in(['a', 'e', 'i', 'o', 'u']): 
#         name=name.replace(i,"")
# print(f"name without vouls = {name}")

##########################################3
#Write a program that prints the locations of "i" character in any
#string you added.
# locs=[]
# index_loc=0
# strr = "im mon mmi moo miimmm i"
# for i in strr:
#     index_loc+=1
#     if (i == "i"):
#         locs.append(index_loc)
# print("locations of i are ",*locs)
#################################################3
#  a program that generate a multiplication table from 1 to the
# number passed.

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     print(f"------------------------{i}------------------------------")
#     for j in range(1, 13):
#         result = i * j
#         print(f"{i} x {j} = {result}", end="\n")
#     print() 
######################################################
# height=int(input("enter the height of the pyramid :"))
# for i in range(1, height + 1):
#     spaces = height - i
#     stars = i
#     print(" " * spaces, end="")
#     print("*" * stars)