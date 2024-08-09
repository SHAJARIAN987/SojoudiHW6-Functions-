alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def func_1(func_1_string):
    upper = 0
    lower = 0
    func_1_string = func_1_string.replace(" ", "")
    for char in func_1_string:
        if char.isalpha():
            if char.isupper():
                upper += 1
            else:
                lower += 1
    print("Upper: ", upper)
    print("Lower: ", lower)

def func_2(func_2_list):
    func_2_list = set(func_2_list)
    func_2_list = list(func_2_list)
    print(func_2_list)

def func_3(func_3_list):
    func_3_output = []
    for char in func_3_list:
        if char%2 == 0:
            func_3_output.append(char)
    print(func_3_output)

def func_4(func_4_string):
    palindrome = True
    func_4_string = func_4_string.replace(" ", "")
    if (len(func_4_string))%2 == 1:
        func_4_string.replace(func_4_string[int(str(((len(func_4_string)-1)/2))[0])], "")
    for i in range(int(str((len(func_4_string)/2))[0])):
        if func_4_string[i] != func_4_string[-1*(i+1)]:
            palindrome = False
    if palindrome:
        print("This string is a palindrome!")
    else:
        print("This string is not a palindrome.")

def func_5(func_5_string):
    pangram = True
    func_5_string.lower()
    for char in alphabet:
        if not(char in func_5_string):
            pangram = False
    if pangram:
        print("This string is a pangram!")
    else:
        print("This string is not a pangram.")

def func_6(func_6_list):
    highest_number = func_6_list[0]
    for char in func_6_list:
        if char > highest_number:
            highest_number = char
    return highest_number

def func_7(func_7_int):
    sum = 0
    for char in str(func_7_int):
        sum += int(char)
    return sum

def func_8(func_8_int):
    digital_root = func_8_int
    while len(str(digital_root)) != 1:
        digital_root = func_7(digital_root)
    print("The digital root of this number is ", digital_root)

def func_9(func_9_string_1, func_9_string_2):
    differ = False
    shorter_string = ""
    longer_string = ""
    if len(func_9_string_2) > len(func_9_string_1):
        shorter_string = func_9_string_1
        longer_string = func_9_string_2
    else:
        shorter_string = func_9_string_2
        longer_string = func_9_string_1
    while len(shorter_string) < len(longer_string):
        shorter_string += " "
    for i in range(len(shorter_string)):
        if shorter_string[i] != longer_string[i]:
            print("The strings differ first on character ", i+1)
            differ = True
            break
    if differ == False:
        print("-1")

def func_10(func_10_string):
    new_string = ""
    for char in func_10_string:
        if char.isalpha():
            if char.islower():
                new_string += char.upper()
            elif char.isupper():
                new_string += char.lower()
        else:
            new_string += char
    print(new_string)

def func_11(func_11_list, func_11_n):
    list = func_11_list
    while func_6(list) > func_11_n:
        list.remove(func_6(list))
    print("The largets number of the list that is less than n is ", func_6(list))

def func_12(n):
    prime = True
    for i in range (2, n):
        if n%i == 0:
            prime = False
    if n == 0 or n == 1:
        prime = False
    return(prime)

def func_13():
    prime_numbers = []
    for i in range (0, 100000):
        if func_12(i):
            prime_numbers.append(i)
    return prime_numbers

#--------------------------------------------------------------------------------------------------------#

func_1_input = input("Enter a string to find out how many uppercase and lowercase letters it has!")
func_1(func_1_input)

func_2_input = [8, 9, 8, "a", "a", 10]
func_2(func_2_input)

func_3_input = [8, 9, 8, 10]
func_3(func_3_input)

func_4_input = input("Enter a string to find out if it is a palindrome!")
func_4(func_4_input)

func_5_input = input("Enter a string to find out if it is a pangram!")
func_5(func_5_input)

func_6_input = [8, 34, 8, 1, 4, 95, 2, 0, 51, 3, 4]
print("The largest number in this list is ", func_6(func_6_input))

func_7_input = int(input("Enter a number to find out the sum of all its digits!"))
print("The sum of this number is ", func_7(func_7_input))

func_8_input = int(input("Enter a number to calculate its digital root!"))
func_8(func_8_input)

func_9_input_1 = input("Enter to see where two strings first differ! String 1: ")
func_9_input_2 = input("String 2: ")
func_9(func_9_input_1, func_9_input_2)

func_10_input = input("Enter a string to invert its letters!")
func_10(func_10_input)

func_11_input_list = [1, 6, 3, 9, 11]
func_11_input_n = 8
func_11(func_11_input_list, func_11_input_n)

func_12_input = int(input("What number would you like to check if it is prime?"))
print(func_12(func_12_input))

print(func_13())