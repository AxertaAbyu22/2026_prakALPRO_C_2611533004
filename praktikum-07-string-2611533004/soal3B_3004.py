text = "Muhammad Abiyyu Haidar Arhab"
count = 0
for char in text.lower():
    if char in "aiueo":
        count = count + 1
print("Vowels:", count)