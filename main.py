def main():
    filepath = "books/frankenstein.txt"
    content = get_book_text(filepath)
    wordcount = count_words(content)
    charcount = count_characters(content)
    print_report(filepath, wordcount, charcount)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)
 
def count_characters(text):
    text_lower = text.lower()

    # prepare dictionary from a-z
    chars = {}
    for i in range(97, 123):
        chars[chr(i)] = 0

    # iterate through text_lower and count in dictionary 
    for char in text_lower:
        if char in chars:
            chars[char] += 1    
    
    return chars

def print_report(path, wordcount, charcount):
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document\n")

    for char in charcount:
        print(f"The {char} character was found {charcount[char]} times")

    print("--- End report ---")

main()
