con = True

while True:
    alnum = noalphnum = 0
    str1 = input("Input your String: ")
    str1 = str1.lower()

    for count in range(len(str1)):
        let = str1[count]
        if let < "a" or let > "z":
            noalphnum += 1
        else:
            alnum += 1

    print(alnum, "Alphabets in your String")
    print(noalphnum, "Non Alphabets in your String")
    choice = input("""
    Do you want to continue ?(Y/N):""")

    if choice == "N":
       con = False
       break
