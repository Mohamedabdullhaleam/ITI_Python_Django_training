import random as rd
# Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# increased by one from start.
array = []
def arrayfilling_gene(length,start):
    global array 
    if isinstance(length, int) and isinstance(start, int):
        for i in range (length):
            array.append(start)
            start+=1
        # print(array)
        return(array)
# arr=arrayfilling_gene(5,0)
# print(arr)

#############################################
# p2--write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if is is divisible by both return "FizzBuzz"
def Fizz_Buzz(num):
    if isinstance(num, int):
        if num%3 ==0 and num%5==0 :
            return "Fizz_Buzz"
        elif num%3 == 0:
            return "Fizz"
        elif num%5 ==0:
            return "Buzz"      
# x=Fizz_Buzz(15)
# print(x)

#############################################
# p3 -- Write a function which has an input of a string from user then it
# will return the same string reversed.
def reversed_str (strr):
    strr =input("enter your str :")
    return strr[::-1]

# print(reversed_str(""))

# p4 -- Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email
# or not
def form_validation (name , email):
    c1=True
    c2=True
    while (c1==True or c2 ==True):
        name=input("Enter your name :")
        if isinstance (name , str):
            print("Name confirmed ")
            c1=False
            email = input ("Enter your email :")
            if "@" in email :
                print ("confirmed mail ")
                c2=False
                print("please re enter valid mail")
                return f"your name is {name} \nand your email is {email}"           
# v=form_validation("","")
# print(v)

###########################################
# p5 --Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in
# alphabetical order is: abdu
 
def find_longest_substring(input_string):
    longest_substring = ""
    current_substring = input_string[0]

    for i in range(1, len(input_string)):
        if input_string[i] >= input_string[i - 1]:
            current_substring += input_string[i]
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = input_string[i]

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring

# print(find_longest_substring("abdullrahmabn"))
##########################################

#p6 -- Write a program which repeatedly reads numbers until the user
# enters “done”.
# ○ Once “done” is entered, print out the total, count, and
# average of the numbers.
# ○ If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.
def reads_numbers ():
    count=0
    total=0
    arr=[]
    flag=True
    while flag :
        n=input("enter a number :")
        if n=="done":
            flag=False
            continue
        else:
            try:
                number = int(n)
                count += 1
                total += number
            except ValueError:
                print("Invalid input. Please enter a valid number or 'done'.")
    avg=total/count
    return f"the total is {total} and the count of entered value is {count} , the average is {avg}"
# print(reads_numbers())

##########################################################33
##p7--Word guessing game (hangman)
# ○ A list of words will be hardcoded in your program, out of
# which the interpreter will
# ○ choose 1 random word.
# ○ The user first must input their names
# ○ Ask the user to guess any alphabet. If the random word
# contains that alphabet, it  will be shown as the output(with correct placement)
# ○ Else the program will ask you to guess another alphabet.
# ○ Give 7 turns maximum to guess the complete word.


def hangman ():
    list_of_words=["mohamed","ahmed","magnam","preprocess"]
    random_word = rd.choice(list_of_words)
    name = input("Kindly Enter Your name :")
    for i in range(len(random_word)+7):
        char = input ("kindly guess a character of the word :")
        if char in random_word :
            print("great you got it right")
            random_word=random_word.replace(char,"")
            print(f"only {len(random_word)} chars left ro guess it all right")
            
            if len(random_word)== 0:
                print("*******congrates you win********")
        else:
            x=(len(random_word)+7)-i
            print(f"wrong guess guess again you have {x} trials left")
            if x<1 :
                print("!!!Game Over!!!")
                break
    return random_word
print(hangman())


#### needed above ### handle inputs

def sumnum(num1:int, num2:int):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError('num1 and num2 must be integers ')
    return  num1 + num2





