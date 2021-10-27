"""Count words in file."""


# put your code here.

word_dict = {}
def count_words(filename):
    data = open(filename)

    for line in data:
        line = line.rstrip().split(" ")

        for word in line:
            word_dict[word] = word_dict.get(word, 0) + 1
    
    for item, count in word_dict.items():
        print(f"{item} {count}")



count_words("test.txt")