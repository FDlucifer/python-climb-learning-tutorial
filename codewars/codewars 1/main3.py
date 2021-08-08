# Stop gninnipS My sdroW!

def spin_words(sentence):
    words = sentence.split(" ")
    return " ".join([word[::-1] if len(word) >= 5 else word for word in words])