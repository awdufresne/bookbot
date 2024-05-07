def wordcount(text):
    words = text.split()
    #print("Placeholder world count result")
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
        #total_letters = lettercount(file_contents)
        total_letters = alphabetize(file_contents)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document\n")
        print(total_letters)
        print("--- End report ---")
main()