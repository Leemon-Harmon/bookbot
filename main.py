contents = None

def main():
    with open("books/frankenstein.txt") as file:
        contents = file.read()
    print(contents[:100])

if __name__=="__main__":
    main()
