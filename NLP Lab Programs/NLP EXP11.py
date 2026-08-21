grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}


def parse(symbol, words, position):
    if symbol not in grammar:
        if position < len(words) and symbol == words[position]:
            return position + 1
        return None

    for rule in grammar[symbol]:
        pos = position

        for item in rule:
            pos = parse(item, words, pos)

            if pos is None:
                break

        if pos is not None:
            return pos

    return None


sentence = input("Enter sentence: ")
words = sentence.lower().split()

result = parse("S", words, 0)

if result == len(words):
    print("Sentence is grammatically valid.")
else:
    print("Sentence is not valid.")
