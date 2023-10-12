def arrayofpowering(x):    ##abbreviation to create condition and for and append to list 
    L = [ x**2 for x in range(10) if x%2 == 0 ]   #x**2 = out put
    return L 
print(arrayofpowering(2))

################################ assigning vars
l=[1,3,4,9]
a,*b,c=l
print(f"mmmmmm{a},mmmmm{b},mmmmm{c}c")

############################################ iteration to find index and value of lists ,tuples ,strings
def index_value ():
    my_list = ['apple', 'banana', 'cherry', 'date']
    for index, value in enumerate(my_list):
        print(f'Index {index}: {value}')
index_value()