word_count = {}

def word_counter(my_string):
    split_string = my_string.lower().split(" ")    
    print(split_string)

    for word in split_string:
        # print(word)
        word_count[word] = split_string.count(word)
    print(word_count)




if __name__ == "__main__":
    f = "The different world consists of up to five castles each of which has up to seven rooms. The world of the game is to visit different rooms and gain as many treasure "
    word_counter(f)
