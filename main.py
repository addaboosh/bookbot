def main():
    with open('./books/frankenstein.txt') as f:
        book = f.read()
        print(book)
    print(word_count(book))

    # Print char counts
    char_dict = char_count(book)
    for key in char_dict:
        print(f"The '{key}' character was found {char_dict[key]} times")




def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    for i in text.lower():
        if not i.isalpha():
            continue
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict


main()
