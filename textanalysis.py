from collections import Counter

def wordcounter(text):

    c = Counter()
    with open(text, 'rb') as f:
        for ln in f:
            c.update(ln.split())
    f.close()

    return sum(c.values())
