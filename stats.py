def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    count = {}
    for c in text:
        lower = c.lower()
        if lower in count:
            count[lower] += 1
        else:
            count[lower] = 1
    return count

def sort_on(items):
    return items["num"]

def sort_dicts(char_dict):
    res = []
    for c in char_dict:
        res.append({
            "char": c,
            "num": char_dict[c]
        })
    res.sort(key=sort_on, reverse=True)
    return res