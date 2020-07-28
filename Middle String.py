while True:
    str1 = input("""Input a three word string so that the middle word can be seperated and printed.
    Enter your string ?: """)

    sp = str1.rfind(" ")
    first2words = str1[0:sp]

    sp = first2words.rfind(" ")
    middle = first2words[sp+1:len(first2words)]
    print(middle, "is the middle word in your String")

    con = input("Do you want to continue (Y/N) ?: ")
    if con == "N":
        break