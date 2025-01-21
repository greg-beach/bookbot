def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    def sort_on(dict):
        return dict["value"]

    character_dict = {}
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in file_contents.lower(): 
        if letter not in alphabet:
            continue
        if letter in character_dict.keys():
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    
    dict_list = []

    for letter, value in character_dict.items():
        dict_list.append({'letter': letter, "value": value})

    dict_list.sort(reverse=True, key=sort_on)



if __name__ == "__main__":
    main()