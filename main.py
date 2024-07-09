def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if(char.isalpha()):
            if(char in char_count):
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def convert_to_list_of_dicts(char_count):
    list_of_dicts = []
    
    for char, num in char_count.items():
        list_of_dicts.append({"char": char, "num": num})
    
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

def main():
    #path to the file 
    path_to_file = "books/frankenstein.txt"

    # open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)


    char_count = count_characters(file_contents)

    list_of_dicts = convert_to_list_of_dicts(char_count)
    list_of_dicts.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    for item in list_of_dicts:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

main()