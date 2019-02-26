def check_palindrome(my_string):
    if my_string[::-1] == my_string:
        return True


def main():
    i = input("Enter String: ")
    if check_palindrome(i):
        print(f"Yes! {i} is a palindrome")
    else:
        print(f"No! {i} is not a palindrome")


if __name__ == "__main__":
    main()