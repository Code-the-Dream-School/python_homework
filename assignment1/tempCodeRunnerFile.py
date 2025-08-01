def pig_latin(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = word.split().lower()
    pig_latin_words = []
    for w in words:
        if w.startswith("qu"):
            pig_latin_words.append(w[2:] + "qu")
        elif w[0] in vowels:
            pig_latin_words.append(w + "ay")
        else:
            for i,char in enumerate(w):
                if char in vowels:
                    pig_latin_words.append(w[i:] + w[:i] + "ay")
                    break
    return" ".join(pig_latin_words)
