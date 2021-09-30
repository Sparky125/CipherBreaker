def main(word):
    convert = word.lower()      #converting the word to lowercase, this is needed because ASCII codes for capital letters are different than lowercase
    newword = word              # 
    alphabet = "abcdefghijklmnopqrstuvwxyz" #getting a string of alphabetic characters, will use this later
    letters = []     #empty list for letters
    newletters = []  #empty list for new letters
    for i in convert:
        if i not in letters:   #removing all duplicate characters from the word before adding to a list
            letters.append(i)  
    i = 0
    while i < len(letters):
        newletters.append(alphabet[i]) #appending the index of each letter to their index in alphabet, we needed to remove duplicates so one letter doesnt receive two different letters
        i += 1
    laststring = "" #empty string, converting the list of the encoded letter into a string
    for i in convert:
        deez = letters.index(i)
        laststring += (newletters[deez])
    print(newword) #printing the word you inputted
    print(laststring) #printing the word you receive
    return laststring

def helper(word):                 #this entire function is the same as main(), just without printing so it's cleaner when called from part2()
    convert = word.lower()
    newword = word
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    newletters = []
    for i in convert:
        if i not in letters:
            letters.append(i)
    i = 0
    while i < len(letters):
        newletters.append(alphabet[i])
        i += 1
    laststring = ""
    for i in convert:
        deez = letters.index(i)
        laststring += (newletters[deez])
    return laststring                  #only returning, no printing in this function



#only run this for part 2
def part2(word):
    converted = helper(word)                      #creating a variable for the helper function of the word, this is more efficient
    f = open("word_alpha.txt", "r")               #than running the helper function every time you want to convert the word
    newlist = []   #creating a new list
    for i in f:                                   #opening the word file, make sure the program and file are in the same folder!
        if len(i) == len(word)+1:               #seeing if the lengths of every word are the same as the one being compared from the list
            newlist.append(i)                   #appending them all to one list before checking if the patterns match
    listy = []                                  #creating a new list for the matching patterns
    for t in newlist:
        listy.append(t.replace("\n", ""))       #replacing the newlines for all of the strings in the list
    finallist = []
    for thing in listy:
        if converted == helper(thing):         #if function, if the converted word you want to find matches for is equal to any of the words
            finallist.append(thing)            #then you append the matching converted words to the list
    print("Finding duplicates for: ",word)     #what word you asked for
    print(finallist)                           #the list of duplicates found
    f.close()


def start():
    deez = input("Do you want to input text or read from file?\n Option 1 for Input text\n Option 2 for Reading from file\nInput: ")
    if deez == "1":
        word = input("input word you want to convert: ")
    elif deez == "2":
        line = int(input("Input which line of the file you want to read from (Index starts at 0) "))
        f = open("word_alpha.txt", "r")
        cackle = f.readlines()
        word = cackle[line]
        word = word.strip() #stripping the newline character from the string, as it was messing with the words

    print("Select 1 for the word converted into the pattern\nSelect 2 for a list of all similar words.")
    ask = input("Select 1 or 2: ")
    if ask == "1":
        main(word)
    elif ask == "2":
        part2(word)                                          #this whole thing is just a prompt asking what the user wants to do
    else:
        print("Invalid, please try again.")
        start()
start()
