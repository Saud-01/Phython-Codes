while True:
    nstr = ""
    str1 = input("Input your String: ")
    char = input("Which character would you like to be truncated from your string: ")
    for count in range(len(str1)):
        str2 = str1[count]
        if str2 != char:
            nstr += str2
    print(nstr)
    con = input("Do you want to continue (Y/N)?: ")
    if con == "N":
        break