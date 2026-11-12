# Name: MUHAMMAD ABIYYU HAIDAR ARHAB
# NIM: 2611533004
# Bonus Question

sentence = input("Kalimat: ")
clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")