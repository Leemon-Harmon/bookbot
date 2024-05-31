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

def listOfD(d):
    list = []
    for i in d:
        if i.isalpha():
            list.append({"name":i,"num":d[i]})
    #print(*list,sep='\n')
    return list

def sortOn(d):
    return d["num"]

def printSortedList(l):
    l.sort(reverse=True, key=sortOn)
    #print(*l,sep='\n')
    for i in l:
        print(f"The '{i['name']}' character was found {i['num']} times")

def totalWords(bookContent):
    words = bookContent.split()
    return len(words)

def main():
    path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as file:
        contents = file.read()
    #print(contents[:100])
    #print(totalWords(contents))
    #print(countChars(contents))
    print(f"--- Begin report of {path} ---")
    print(f"{totalWords(contents)} words found in the document")
    print("\n")
    printSortedList(listOfD(countChars(contents)))
    print("--- End report ---")
main()
