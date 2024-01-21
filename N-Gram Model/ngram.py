import random
import json

def generate_ngrams(text, n):
    words = text.split()
    ngrams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    return ngrams

def build_ngram_model(text, n):
    ngram_model = {}
    ngrams = generate_ngrams(text, n)
    
    for ngram in ngrams:
        prefix = tuple(ngram[:-1])
        suffix = ngram[-1]
        
        if prefix in ngram_model:
            ngram_model[prefix].append(suffix)
        else:
            ngram_model[prefix] = [suffix]
    
    return ngram_model

def generate_text(ngram_model, seed, length):
    current = seed.split()[-(n-1):] if n > 1 else [seed]
    generated_text = current.copy()

    for _ in range(length):
        if tuple(current) in ngram_model:
            next_word = random.choice(ngram_model[tuple(current)])
            generated_text.append(next_word)
            current = current[1:] + [next_word]
        else:
            break

    return ' '.join(generated_text)

def read_text():
    with open('Torah.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    full_text_list = []
    for key, value in data.items():
        for section in value:
            full_text_list += section
    
    return full_text_list


text_corpus = "This is an example sentence for building a text generator. The generator should predict the next word based on the given context."
n = 2  # You can choose the value of n (e.g., 2 for bigrams, 3 for trigrams, etc.)

ngram_model = build_ngram_model(text_corpus, n)
seed_word = "predict"
generated_text = generate_text(ngram_model, seed_word, length=10)

print(f"Generated Text: {generated_text}")
