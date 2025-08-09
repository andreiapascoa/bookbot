from stats import get_book_text, count_words, create_dictionary, sort_list_chars

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_contents)
    # print(f"{num_words} words found in the document")
    chars_dic = create_dictionary(file_contents)
    # print(chars_dic)
    sorted_list = sort_list_chars(chars_dic)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for elem in sorted_list:
        for c in elem:
            print(f"{c}: {elem[c]}")


main()
