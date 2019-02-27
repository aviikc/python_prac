

vowels = ['a', 'e', 'i', 'o', 'u']

collected_vowels = []
collected_letters = {}

def vowel_collector(my_string):
    for letter in my_string:
        if letter in vowels:
            collected_vowels.append(letter)
    return collected_vowels, len(collected_vowels)

def vowel_counter(my_vowels):
    for k in my_vowels:
        for vowel in vowels:
            collected_letters[vowel] = my_vowels.count(k)
    return collected_letters


def main():
    i = input("Enter String: ").strip().lower()
    print("The number of vowels in the text: ", vowel_collector(i)[1])
    print(vowel_collector(i)[0])
    print(vowel_counter(vowel_collector(i)[0]))


if __name__ == "__main__":
    main()
