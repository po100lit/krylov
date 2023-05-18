def stop_words():
    with open('stopwords.txt', 'r', encoding='utf-8') as file:
        words = set(file.read().split())
        return words
