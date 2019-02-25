'''
Pig Latin – Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is 
transposed to the end of the word and an ay is affixed 
(Ex.: "banana" would yield anana-bay).

https://www.youtube.com/watch?v=QUBftlqlF3w
'''
vowels = ['a', 'e', 'i', 'o', 'u']
def pig_latinize(my_string):
    '''
    This program converts a given string to pig latin format.
    Parameters: my_string String
    Returns: String
    '''
    first_letter = my_string[0].lower()
    rest_word = my_string[1:]

    def string_splitter(rest_word):
        for letter in rest_word:
            if letter in vowels:
                return letter, rest_word.split(letter)

        

    '''
    For words that begin with consonant sounds, all letters before the initial 
    vowel are placed at the end of the word sequence. Then, "ay" is added
    '''
    if my_string[0].lower() not in vowels:
        if rest_word[0].lower() not in vowels:
            new_word = string_splitter(my_string)            
            return new_word[0] + new_word[1][1] + new_word[1][0] + 'ay'
        else:
            return rest_word + first_letter + 'ay'

    else:
        return my_string + 'ay'

    '''
    When words begin with consonant clusters (multiple consonants that form one sound), 
    the whole sound is added to the end when speaking or writing.
    '''
    # else if my_string[0].lower() not in vowels and rest_word[0].lower() not in vowels:
    '''
    For words that begin with vowel sounds, one just adds "way" or "yay" 
    to the end (or just "ay").
    '''

    # assert(my_string, )
    
    
    # return f"Pig Latin of {my_string} is {rest_word}{first_letter}{'ay'}"

def main():
    t = []
    i = input("Enter the string: ")
    words = i.split(" ")
    # print(k)
    for word in words:
        # word.upper()
        t.append(pig_latinize(word))
        

    print(" ".join(t))    
    # print(pig_latinize(i))




if __name__ == "__main__":
    main()


