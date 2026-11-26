semua_siswa = input("semua siswa :").split()
submitted = input("submitted :").split()

submitted_set=set(submitted)
submitted_count=len(submitted_set)
not_submitted=set(semua_siswa) - (submitted_set)

print("Submitted:", submitted_count, "students")
print("Not submitted:", len(not_submitted), "students")

for siswa in semua_siswa:
    if siswa not in submitted_set:
        print(siswa)