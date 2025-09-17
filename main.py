from stats import get_num_words, sort_dict
import sys

arguments = sys.argv
if len(arguments) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

book_path = arguments[1]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    content = get_book_text(book_path)
    word_count, chars_count = get_num_words(content) 
    
    sorted_dict = sort_dict(chars_count)
    print('============ BOOKBOT ============')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for count in sorted_dict:
        if count['char'].isalpha():
            print(f'{count['char']}: {count['num']}')
    print('============= END ===============')


main()
