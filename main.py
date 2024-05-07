def wordcount(text):
    words = text.split()
    return len(words)
    
'''
def lettercount(text):
    lowered_text = text.lower()
    letters = {}
    for letter in lowered_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
'''

def alphabetize(text):
    lowered_text = text.lower()
    alpha_list = {}
    for letter in lowered_text:
        if letter.isalpha():
            if letter in alpha_list:
                alpha_list[letter] += 1
            else:
                alpha_list[letter] = 1   
        else:
            pass
    return alpha_list



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = wordcount(file_contents)

        sorted_list = alphabetize(file_contents)
        list_of_dicts = [{'letter': letter, 'count': count} for letter, count in sorted_list.items()]
        list_of_dicts.sort(key=lambda item: item['count'], reverse=True)
   
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document\n")
        #loop iterating over list, printing each letter and it's count
        for item in list_of_dicts:
            print(f"The '{item['letter']}' character was found {item['count']} times")
        print("--- End report ---")
main()