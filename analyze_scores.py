def get_average(people):
    total = 0
    for person in people:
        total += person["score"]
        average = total / len(people)
    
    return average
    
def get_max(people):
    max_score = 0
    for person in people:
        if person["score"] > max_score:
            max_score = person["score"]
    
    return max_score

def passed_filter(people):
    passed_people = []
    for person in people:
        if person["label"] == "Pass":
            passed_people.append(person)

    return passed_people

def get_people(lines):
    people = []
    for line in lines:
        person = {}
        person["name"], person["score"] = line.strip().split(",")
        person["score"] = int(person["score"])
        if person["score"] >= 70:
            person["label"] = "Pass"
        else:
            person["label"] = "Fail"
        people.append(person)
    return people

with open("scores.csv", "r") as f:
    lines = f.readlines()

people = get_people(lines)
average = get_average(people)
max_score = get_max(people)
passed_count = len(passed_filter(people))
passed_percent = passed_count / len(people) * 100
print(f"平均点: {average}点")
print(f"最高点: {max_score}点")
print(f"Passの人数: {passed_count}人")
print(f"Pass率: {passed_percent:.1f}%")