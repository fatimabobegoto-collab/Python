#project 1

def get_average(students):
    total = 0
    count = 0
    for s,u in students.items():
        total += u
        count += 1
    average = total / count
    return average


#project suite
def get_passed_students(students):
    return [k for k,u in students.items() if u >= 70]

def get_unique_scores(students):
    return {students.values()} #set(students.values())






