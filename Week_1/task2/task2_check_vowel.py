#Write a Python program to test whether a passed letter is a vowel or not.

vowels = "aAeEiIoU"

text = input("Enter string: ")

ls = [vowel for vowel in text if vowel in vowels]

if ls:
    print("Vowels found: {}".format(ls))
else:
    print(text)