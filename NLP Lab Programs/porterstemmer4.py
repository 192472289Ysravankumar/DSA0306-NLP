class PorterStep4:

    def step4(self, word):

        suffixes = [
            "ement", "ment", "ance", "ence",
            "able", "ible", "ant", "ent",
            "al", "er", "ic", "ou",
            "ism", "ate", "iti",
            "ous", "ive", "ize"
        ]

        for suffix in suffixes:

            if word.endswith(suffix):
                return word[:-len(suffix)]

        if word.endswith("ion"):

            if len(word) > 3 and word[-4] in ['s', 't']:
                return word[:-3]

        return word


obj = PorterStep4()

word = input("Enter a word: ")

print("Stemmed Word:", obj.step4(word))
