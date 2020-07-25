x = False
while True:
    word = ""

    str1 = input("Enter your String: ")

    for count in range(len(str1), 0, -1):
        letter = str1[count-1]
        word += letter

    print(word)
    con = input("""
    Do you want to continue (Y/N) ?:""")
    if con == "N":
        x = True
        break
