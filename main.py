def main():
    path_text = "books/frankenstein.txt"
    file_content = get_book_text(path_text)
    print(file_content)
    num_of_words = len(file_content.split())
    print(f"{num_of_words} words in the Document.")


def get_book_text(path):
    with open(path) as file:
        return file.read()
    
main()