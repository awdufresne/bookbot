def wordcount(text):
    words = text.split()
    #print("Placeholder world count result")
    return len(words)
    
def lettercount(text):
    lowered_text = text.lower()
    letters = {}
    for letter in lowered_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = wordcount(file_contents)
        total_letters = lettercount(file_contents)
        print(f"Total word count: {total_words}")
        print(total_letters)
main()