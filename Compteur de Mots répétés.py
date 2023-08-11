def count_repeated_words(text):
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    repeated_words = {word: count for word, count in word_count.items() if count > 1}
    
    return repeated_words

# Changez la valeur de text en insérant votre texte :
print("Entrez votre texte :")
text = str(input())
repeated_words = count_repeated_words(text)

for word, count in repeated_words.items():
    print(f"Le mot '{word}' est répété {count} fois.")
