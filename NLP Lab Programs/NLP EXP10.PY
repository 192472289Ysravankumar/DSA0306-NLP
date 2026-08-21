def initial_tagging(words):
    result = []

    for word in words:
        if word.lower() in ["the", "a", "an"]:
            tag = "DT"
        elif word.endswith("ing"):
            tag = "NN"
        else:
            tag = "NN"

        result.append([word, tag])

    return result


def transformation_rule(tags):
    for item in tags:
        word = item[0]

        # Transformation rule:
        # Words ending in "ing" are verbs
        if word.endswith("ing"):
            item[1] = "VBG"

    return tags


sentence = input("Enter a sentence: ")

words = sentence.split()

tags = initial_tagging(words)
tags = transformation_rule(tags)

print("\nTransformation-Based Tags:")
for word, tag in tags:
    print(word, "->", tag)
