contents = None

def countChars(testString):
    dict = {}
    lowerCaseString = testString.lower()
    for i in lowerCaseString:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


def totalWords(bookContent):
    words = bookContent.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as file:
        contents = file.read()
    print(contents[:100])
    print(totalWords(contents))
    print(countChars(contents))

main()
