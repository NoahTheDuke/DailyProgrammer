choice = int(input("1) Binary to letters; 2) Letters to binary.\n> "))
if choice == 1:
    text = input("Gimme the binary, bro.\n> ")
    print("".join([chr(int(text[x:x + 8], 2)) for x in range(0, len(text), 8)]))
else:
    text = input("Let's get convertin'.\n> ")
    print("".join([bin(ord(x)).split('b')[1].zfill(8) for x in text]))
