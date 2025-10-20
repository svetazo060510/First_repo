import string
def count_words (text: str) -> dict:
    lower_text = text.lower()
    cleaned_text = lower_text.replace('.', '').replace(',', '').replace('?', '').replace('!', '')
    words_list = cleaned_text.split()
    word_counts = {}
    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1
        else: 
            word_counts[word] = 1

    return word_counts

def main():
    user_input = input("Enter a word or phrase: ")
    counts = count_words(user_input)

    print("--- Word Counts ---")
    for word, count in counts.items():
        print(f"{word}: {count}")   
    
if __name__ == "__main__":
    main()

