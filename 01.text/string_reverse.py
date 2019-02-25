# Reverse a String

def reverse( my_string):
'''
Function reverses a given string
Objective: To reverse a string
Parameters: my_string String
Returns: String
'''
    return my_string[::-1]

def main():
    i = input("Enter the string: ")
    print(reverse(i))


if __name__ == "__main__":
    main()