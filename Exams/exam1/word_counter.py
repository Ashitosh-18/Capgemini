def count_words(sentence):
    
    words = sentence.lower().split()  # Convert to lowercase and split into words

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts
    
def main():
    sentence = input("Enter a sentence: ")
    word_counts=count_words(sentence)
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    
main()
    
    