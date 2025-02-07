def count_word_occurrences(txt):
    words = txt.split() 
    word_count = {}

    for word in words:
        word = word.lower().strip(".,!?") 
        word_count[word] = word_count.get(word, 0) + 1 
    return word_count
txt = input("Enter a text: ")

word_counts = count_word_occurrences(txt)
print("\nWord occurrences:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
