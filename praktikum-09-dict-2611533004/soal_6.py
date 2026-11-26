schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a
busiest_day = ""
max_courses = 0

for day, courses in schedule.items():
    if len(courses) > max_courses:
        busiest_day = day
        max_courses = len(courses)

print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# 6b
target_course = input("Course name: ")
day_count = 0

for courses in schedule.values():
    if target_course in courses:
        day_count += 1

print(f"{target_course}: {day_count} days")