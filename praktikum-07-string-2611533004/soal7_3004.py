# Name: MUHAMMAD ABIYYU HAIDAR ARHAB
# NIM: 2611533004
# Question 7

name = "muhammad abiyyu haidar arhab"
nim = "2611533004"

space = name.find(" ")
if space == -1:
    first_name = name
else:
    first_name = name[:space]

username = first_name + nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)