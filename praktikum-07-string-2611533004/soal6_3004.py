# Name: MUHAMMAD ABIYYU HAIDAR ARHAB
# NIM: 2611533004
# Question 6

full_name = "MUHAMMAD ABIYYU HAIDAR ARHAB"
nim = "2611533004"

clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first + nim[-3:]
print(username)