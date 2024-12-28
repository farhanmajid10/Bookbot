def main():
    path_text = "books/frankenstein.txt"
    file_content = get_book_text(path_text)
    #print(file_content)
    num_of_words = len(file_content.split())
    print(f"{num_of_words} words in the Document.")
    dict = get_character_count(file_content)
    #print(dict)
    print_character_count(dict)

def get_character_count(file_content):
    dict = {}
    file_lower_case = file_content.lower()
    for i in range(len(file_content)):
        if file_lower_case[i] in dict:
            dict[file_lower_case[i]] += 1
        else:
            dict[file_lower_case[i]] = 1
    return dict

def print_character_count(dict):
    print("---Character count:---")
    for key, value in sorted(dict.items()):
        if key <= 'z' and key >= 'a':
            print(f"The '{key}' character was found {value} times.")
    print("---Character Count over.---")

def get_book_text(path):
    with open(path) as file:
        return file.read()
    
main()