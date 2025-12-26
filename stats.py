def count_words(text):
    return len(text.split())

def count_chars(text):
    result = {}

    for char in text.lower():
        try:
            result[char] += 1
        except KeyError:
            result[char] = 1

    return result

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    result = []

    for entry in chars:
        result.append({"char": entry, "num": chars[entry]})

    result.sort(reverse = True, key=sort_on)

    return result
