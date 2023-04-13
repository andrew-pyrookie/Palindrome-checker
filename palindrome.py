word = input("Type in the word or the phrase : ")

def checker(word):
     # Remove any non-alphanumeric characters and convert to lowercase
    word = ''.join(filter(str.isalnum, word)).lower()
    print(word)

     # Compare the first and last characters, then the second and second-to-last, and so on
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            print("Not a palindrome")
            break
    else:
        print("It's a palindrome")


checker(word)
